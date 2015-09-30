from app import app, db
from models import Stream, FileStatu
from cdr_etl import cdr_etl, cdr_log
import datetime as dt
import multiprocessing as mp
import os


@app.route('/<in_date>/<stream_name>')
def hello_world(in_date, stream_name):
    generate_cdrs(in_date,stream_name)

    # load_cdrs(in_date,stream_name)
  
    return "job in progress"

def generate_cdrs(in_date, stream_name):
    
    in_date = dt.datetime.strptime(in_date, "%Y%m%d").date()
    log = cdr_log()
    session = log.startGenSession(in_date, stream_name)
    try:
        main_generate_parrallel(stream_name, in_date, session.id)
        log.endGenSession()
    except ValueError, e:
        print e.args
        # raise
        # log.failedSession()
    except no_files_found as e:
        details = e.args[0]
        print(details["animal"])
    else:
        pass
    finally:
        pass
    
def main_generate(stream, ref_date, session_id):
    cdrProcessor = cdr_etl(stream, ref_date, session_id)
    files = cdrProcessor.distribute()
    for i in range(len(files)):
        cdrProcessor.process_thread(files[i], i)
#     cdrProcessor.test()


def main_generate_parrallel(stream_name, ref_date, session_id):
    cdrProcessor = cdr_etl(stream_name, ref_date, session_id)
    files = cdrProcessor.distribute()
    # append the class and thread no to the files for each thread
    for i in range(len(files)):
        files[i].append(cdrProcessor)
        files[i].append(i)
    p = mp.Pool(cdrProcessor.stream.no_threads)
    result = p.map_async(process_thread_parallel, files)
#     result.wait()
    ppp = result.get()

    for i in range(len(files)):
        generated_files=(files[i][:-2])
        for k in generated_files:
            cdr_file=FileStatu(file_name=k.filename, stream_id=k.stream_id, ref_date=ref_date,
                               record_count=k.no_records, generate_session_id = k.gen_session_id,
                               size=k.file_size
                               #@TODO: convert incoming date to mysql db formartfile_created_time=k.created_date 
                               )
            db.session.add(cdr_file)
            # print k.filename, k.no_records, k.gen_file_name 
        db.session.commit()
      


def process_thread_parallel(files):
    current = mp.current_process()
    cdr_etl = files.pop(len(files) - 2)
    thread_no = files.pop(len(files) - 1)
    # print current.name
    # print os.getpid()
    # print files[len(files)-1]
    rtn = cdr_etl.process_thread(files, thread_no)
    return rtn

##########################################################################
    