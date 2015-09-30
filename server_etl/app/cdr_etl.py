from app import app, db
from models import Stream, GenerateSession
import os, zipfile, glob, shutil
import datetime as dt

class cdr_file(object):

    def __init__(self, file_path, session_id, stream_id):
        self.filename = os.path.basename(file_path)
        self.file_path = file_path
        self.no_records = self.set_file_record_count()
        self.file_size = os.path.getsize(file_path)
        self.created_date = os.path.getctime(file_path)
        self.gen_session_id = session_id
        self.stream_id = stream_id 
        self.gen_file_name = ''

    def set_gen_file_name(self, generated_file_name):
        #@TODO: check why this does not uptdate the required variable
        self.gen_file_name =  os.path.basename(generated_file_name)


    def set_file_record_count(self):
        with open (self.file_path) as f:
            for i , I in enumerate(f):
                pass
            return i+1

    # @setattr(object, gen_file_name,generated_file_name )

    

class cdr_log():

    def __init__(self):
        pass

    def startGenSession(self, ref_date, stream_name):
        stream_id = Stream.query.filter(Stream.name == stream_name).first().id
        newGenSession = GenerateSession(ref_date=ref_date, start_time=dt.datetime.now(
        ), status="STARTED", stream_id=stream_id)
        db.session.add(newGenSession)
        db.session.commit()
        self.genSession = newGenSession
        return newGenSession

    def endGenSession(self):
        activeSession = self.genSession
        activeSession.status = "COMPLETED"
        activeSession.end_time = dt.datetime.now()
        diff = activeSession.end_time - activeSession.start_time
        activeSession.duration = diff.seconds
        db.session.add(activeSession)
        db.session.commit()
        self.genSession = activeSession

    def failedSession(self):

        activeSession = self.genSession
        activeSession.status = "FAILED"
        activeSession.end_time = dt.datetime.now()
        diff = activeSession.end_time - activeSession.start_time
        activeSession.duration = diff.seconds
        db.session.add(activeSession)
        db.session.commit()
        self.genSession = activeSession


class cdr_etl():

    def __init__(self, cdr_name, ref_date, session_id):
        self.ref_date = ref_date.strftime("%Y%m%d")
        self.ses_id = session_id
        self.stream = Stream.query.filter(Stream.name == cdr_name).first()
        working_dir = app.config.get('WORKING_DIR')
        self.in_dir = os.path.join( os.path.join(working_dir, self.stream.name), 'in')
        self.load_dir = os.path.join( os.path.join(working_dir, self.stream.name), 'load')
        archive_dir = app.config.get('ARCHIVE_DIR')
        self.archive_dir = os.path.join( os.path.join(archive_dir, self.stream.name), self.ref_date)
        
        # should be passed from db as cdr.search_term
        self.search_term = '*' + self.ref_date + '*'

    def get_cdrs(self):
        in_path = os.path.join(self.in_dir, self.search_term)
        files = [cdr_file(fl, self.ses_id, self.stream.id) for fl in glob.glob(in_path)[:self.stream.files_per_session]]
        # remove loaded files
        # files=remove_loaded(files)
        # check if cdr.is_compressed then uncompress
        return files

    def uncompress(self):
        pass

    def compress(self, file_path):
        file_name_zip = file_path[:-3] + 'zip'
        zout=zipfile.ZipFile(file_name_zip, "w", zipfile.ZIP_DEFLATED)
        zout.write(file_path)
        zout.close()


    def mkdir_recursive(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def move_to_archive(self, files):    
        self.mkdir_recursive(self.archive_dir)
        archive_file_list = []
        for file in files:
            archived_file=os.path.join(self.archive_dir, os.path.basename(file.filename))
            shutil.copy(file.file_path, archived_file)
            # shutil.move(file.file_path, archived_file)
            archive_file_list.append(archived_file)

        for file in archive_file_list:
            self.compress(file)

        for file in archive_file_list:
            os.remove(file.file_path)


    def test(self):
        print self.stream.name
        print self.stream.files_per_session
        print self.stream.no_threads, self.load_dir, self.in_dir, self.search_term

    def distribute(self):
        # import pdb; pdb.set_trace()#

        # create the files -- this will be the array from ls
        files = self.get_cdrs()
        if len(files) == 0:
            raise ValueError('A very specific bad thing happened','pupu')


        # create dir or in this case array that contain the sub dir or array
        # that amount to the number of thread
        cdr_threads = [[] for i in range(self.stream.no_threads)]
        # allocate spaces for the number of files to go into each thread based
        # on the number of files coming
        i = 0

        for file in files:
            cdr_threads[i].append(file)
            i += 1
            if i == self.stream.no_threads:
                i = 0
        return cdr_threads

    def distribute2(self):
        """@TODO :this method aim to distributes files in such so the the files are in the folders sequecially i.e  folder one contains 
        the first 1-10 files and the last folder contains the last set of files i.e the reminder"""

        os.chdir(self.in_dir)
        # create the files -- this will be the array from ls
        files = self.get_cdrs()
        # create dir or in this case array that contain the sub dir or array
        # that amount to the number of thread
        cdr = [[] for i in range(self.stream.no_threads)]
        # allocate spaces for the number of files to go into each thread based
        # on the number of files coming
        interval = self.stream.files_per_session / self.stream.no_threads
        mod_int = self.stream.files_per_session % self.stream.no_threads
        for i in range(self.no_threads):
            for j in range(interval):
                cdr[i].append([])

            if i <= mod_int - 1:
                cdr[i].append([])
                print mod_int, i

        n = 0
        for i in range(self.no_threads):
            cdr[i] = files[n:n + len(cdr[i])]
            n = n + len(cdr[i])

    def process_thread(self, files, thread_no):
        print 'for thread', thread_no + 1, 'there are ', len(files), 'files'
        # set the path to put all_data.txt
        # load_dir=self.load_dir+'/'+self.ref_date
        load_dir = os.path.join(self.load_dir, self.ref_date)
        #@TODO: REPLACE THIS MKDIR -P WITH A PYTHON IMPLEMENTAION
        self.mkdir_recursive(load_dir)

        # set the name of the final files with thread_no and
        # timestamp/session_number/sequence
        data_file = load_dir + '/all_data_' + str(thread_no + 1) + '_' + str(self.ses_id) + '_' + str(self.ref_date) + '.txt'
        if os.path.exists(data_file):
            os.remove(data_file)
        with open(data_file, 'w') as outfile:
            for i in range(len(files)):
                cdrfile = files[i]
                k=0
                with open(cdrfile.file_path) as infile:
                    for line in infile:
                        line = cdrfile.filename + '|' + self.ref_date + '|' + line
                        outfile.write(line)
                        k+=1
                cdrfile.set_gen_file_name(data_file)
                cdrfile.no_records = k

        self.move_to_archive(files)
        rtn = 'done {}'.format(thread_no + 1)
        # archive all_data.txt
        print rtn
        return rtn
