import os, time

from os import listdir

from joblib import Parallel, delayed

from multiprocessing import Process

import pymysql as py, logging, inspect

import datetime

#from etlconnect import *

from dateTime import *

#from tableOp import *

from datetime import timedelta

from app import db

from dbmodels import *

from sqlalchemy import *
    

def file():

    try:
        file_logger = function_logger(logging.DEBUG, logging.ERROR)

        file_logger.debug('Checking if file exist')
        
        os.makedirs('file', exist_ok=True)

        file_logger.warn('file exist already')

        os.makedirs('Archive', exist_ok=True)

        file_logger.info('file created')
        
    except Exception as e:

        file_logger.critical('file can not be created')

        file_logger.error(str(e))
    

def Directory(*direc):

    try:

        file_logger = function_logger(logging.DEBUG, logging.ERROR)
    
        lis = os.listdir(*direc)[:251]
        
        lisarr = []

        for ext in lis:
            
            if ext.endswith('.unl'):
                
                lisarr.append(ext)
                
        return lisarr
    
    except Exception as e:

        file_logger.error(str(e))

        print(str(e))

    
def removeFileExist(con):

    try:

        engine = create_engine('mysql+pymysql://root:@localhost/etldb')
        metadata = MetaData(bind=engine)

        curDir = Directory()

        cur = con.cursor()

        fileexis = engine.execute("SELECT file_name FROM file_status")

        rows = cur.fetchall()

        data = []

        for row in rows:

            data.append(row[0])

        dataset = set(data)

        curDirset = set(curDir)

        curfile = curDirset - dataset

        for x in curDirset:

            if x in dataset:

                os.remove(x)

            else:

                pass

        n =  list(curfile)

        n.sort()

        return n

    except Exception as e:

        print(str(e))


def paraprocess(loadSessionId,streamName,refDate,Id,numm,numy,lisarr,i):

    file_logger = function_logger(logging.DEBUG, logging.ERROR)

    #con = py.connect('localhost','root','','etldb')

    start_tim = time.clock()

    start_time = timedelta(seconds=start_tim)

    file_logger.info('The start time for '+str(i)+' is '+str(start_time))

    file_logger.debug('process running #'+str(i))
                
    os.makedirs('file/'+str(i),exist_ok=True)
                
    fout = open('file/'+str(i)+'/out'+str(Id)+'.unl','w')

    numy = numy + numm

    numm = 0

    loop = range(numy,len(lisarr))

    file_logger.debug('transforming process start')

    timeStamp = currentDateTimeFor()

    stage = 'transforming process start'

    #generateHistoryUpdate(con,Id,timeStamp,stage)

    g  = GenerateHistory.query.filter_by(generate_session_id = Id).first()

    g.timestamp = timeStamp

    g.stage = stage

    db.session.commit()

    for num in loop:

        try:

            filename = lisarr[num]

            fileinfo = os.stat(filename)

            filesize = fileinfo.st_size

            f = open(filename)

            filedate = filename[3:11]

            timeStamp = currentDateTimeFor()

            stage = 'writing into output file start'

            #generateHistoryUpdate(con,Id,timeStamp,stage)
            ###flash
            g  = GenerateHistory.query.filter_by(generate_session_id = Id).first()

            g.timestamp = timeStamp

            g.stage = stage

            db.session.commit()

            countLine = 0

            for line in f:

                fout.write(filename+'|'+filedate+'|'+line)

                countLine+=1

            f.close()

            file_logger.debug('Moving File into Archive')

            os.rename(filename,"Archive/"+filename)

            file_logger.info('File Successfully moved')

            try:

                archived = 0

                #fileStatus(con,streamName,filename,refDate,countLine,Id,loadSessionId,filesize,archived)
                streamId = stream.query.filter_by(name = streamName).first()

                db.session.add(fileStatus(filename,streamId,refDate,countLine,Id,loadSessionId,filesize,archived))

                timeStamp = currentDateTimeFor()

                stage = 'Moving File into Archive'

                #generateHistoryUpdate(con,Id,timeStamp,stage)

                g  = GenerateHistory.query.filter_by(generate_session_id = Id).first()

                g.timestamp = timeStamp

                g.stage = stage

                db.session.commit()

                timeStamp = currentDateTimeFor()

                stage = 'File Successfully moved'

                #generateHistoryUpdate(con,Id,timeStamp,stage)

                g  = GenerateHistory.query.filter_by(generate_session_id = Id).first()

                g.timestamp = timeStamp

                g.stage = stage

                db.session.commit()

            except Exception as e:

                file_logger.critical(str(e))

            numm+=1
                        
            if numy < 190:

                if numm == 10:

                    break

            else:

                pass

        except Exception as e:

            file_logger.error(str(e))

            pass

    fout.close()

    file_logger.info('Successfully wrote file')

    timeStamp = currentDateTimeFor()

    stage = 'Successfully wrote file'

    #generateHistoryUpdate(con,Id,timeStamp,stage)

    g  = GenerateHistory.query.filter_by(generate_session_id = Id).first()

    g.timestamp = timeStamp

    g.stage = stage

    db.session.commit()

    end_time = time.clock()

    end_time = timedelta(seconds=end_tim)

    file_logger.info('The end time for '+str(i)+' is '+str(end_time))
                
    work_tim = end_time - start_time

    work_time = timedelta(seconds=work_tim)

    file_logger.info('The work time for '+str(i)+' is '+str(work_time))

    #act_time += work_time 
            

def function_logger(file_level, console_level = None):
    
    function_name = 'log/'+inspect.stack()[1][3]
    
    logger = logging.getLogger(function_name)
    
    logger.setLevel(logging.DEBUG) #By default, logs all messages
    

    if console_level != None:
        
        ch = logging.StreamHandler() #StreamHandler logs to console
        
        ch.setLevel(console_level)
        
        ch_format = logging.Formatter('%(asctime)s - %(message)s')
        
        ch.setFormatter(ch_format)

        logger.addHandler(ch)

    fh = logging.FileHandler("{0}.log".format(function_name))

    fh.setLevel(file_level)

    fh_format = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname)-8s - %(message)s')

    fh.setFormatter(fh_format)

    logger.addHandler(fh)

    return logger

    
if __name__=="__main__":

    try:

        '''con = proconnect()

        creatTables(con)'''

        #create db and all db tables
        db.create_all()

        os.makedirs('log', exist_ok=True)

        f = open('session.info')

        Id = int(f.read())

        f.close()

        refDate = curentDateFor()

        timeStamp = currentDateTimeFor()

        stage = 'Initializing'

        start_tim = time.time()

        start_time = timedelta(seconds=int(start_tim))

        #generateHistory(con,Id,timeStamp,stage)

        file()

        streamName = input('Enter stream name')

        streamId = stream.query.filter_by(name = streamName).first()

        db.session.add(GenerateSession(refDate,start_time,'none','none','none',streamId))

        db.session.add(GenerateHistory(timestamp, stage, Id))
    
        numm = 0

        numy = 0

        act_time = 0

        loadSessionId = 0

        lisarr = removeFileExist(con)

        #file_logger.debug('generating process start')

        timeStamp = currentDateTimeFor()

        stage = 'generating process start'

        #generateHistoryUpdate(con,Id,timeStamp,stage)

        g  = GenerateHistory.query.filter_by(generate_session_id = Id).first()

        g.timestamp = timeStamp

        g.stage = stage

        db.session.commit()
        
        jobs = []

        if len(lisarr) > 0:
        
            for i in range(1,21):

                p = Process(target=paraprocess,args=(loadSessionId,streamName,refDate,Id,numm,numy,lisarr,i))

                jobs.append(p)

                p.start()

                p.join()

                print(p.name,p.pid)

        #if p.exitcode != None: 

        #file_logger.info('The total time for the process is '+str(act_time))

        end_tim = time.time()

        end_time = timedelta(seconds=int(end_tim))

        duratn = end_time - start_time

        duration = timedelta(seconds=int(duratn))

        d = int(Id) + 1

        f = open('session.info','w')

        f.write(str(d))

        f.close()

        status = 'Success'

        gSession = GenerateSession.query.filter_by(id = Id).first()

        gSession.status = status

        gSession.end_time = end_time

        gSession.duration = duration

        

    except Exception as e:

        print(str(e))
    
