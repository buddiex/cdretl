import time, os

from app import db

from sqlalchemy import *

def processquery(con,noOfthreads):

    noOfthreads = noOfthreads
    
    with con:

        at_time = time.ctime(time.time())

        os.makedirs('Archive/LoadedFile', exist_ok=True)

        loadData(con,noOfthreads)
        
        
def loadData(db.Model,dat):

    for i in range(1,21):

        os.makedirs('Archive/LoadedFile/'+str(i)+'/'+dat, exist_ok=True)

        __tablename__ = "blueEtlData"+str(i)
        
        id = db.Column(db.Integer, primary_key=True)
        FILENAME = db.Column(db.String(50))
        FILEDATE = db.Column(db.String(50))
        SERIALNO = db.Column(db.String(50))
        SUBSEQUENCE = db.Column(db.String(50))
        TIMESTAMP = db.Column(db.String(50))
        SERVICEKEY = db.Column(db.String(50))
        CHARGINGPARTYNUMBER = db.Column(db.String(50))
        REQUESTACTION = db.Column(db.String(50))
        CHARGETYPE = db.Column(db.String(50))
        SERVICETYPE = db.Column(db.String(50))
        BEAREDSERVICE = db.Column(db.String(50))
        SPID = db.Column(db.String(50))
        CATEGORYID = db.Column(db.String(50))
        CONTENTID = db.Column(db.String(50))
        SERVICEID = db.Column(db.String(50))
        ORIGINALNETWORKTYPE= db.Column(db.String(50))

        CHARGEAMOUNT = db.Column(db.String(50))
        BRANDID = db.Column(db.String(50))
        SUBCOSID = db.Column(db.String(50))
        PAYTYPE = db.Column(db.String(50))
        BILLCYCLEID = db.Column(db.String(50))
        SERVICEBEGINTIME = db.Column(db.String(50))
        SERVICEENDTIME = db.Column(db.String(50))
        USAGEAMOUNT = db.Column(db.String(50))
        SERVICEUNIT = db.Column(db.String(50))
        CHARGINGTIME = db.Column(db.String(50))
        TRANSITIONID = db.Column(db.String(50))
        USERSTATE = db.Column(db.String(50))
        SUBSCRIBERID = db.Column(db.String(50))
        RESERVED1 = db.Column(db.String(50))
        RESERVED2 = db.Column(db.String(50))
        RESULTCODE = db.Column(db.String(50))
        CHARGEOFITEMSACCOUNTS = db.Column(db.String(50))

        CHARGEOFDURATIONACCOUNTS = db.Column(db.String(50))
        CHARGEOFFUNDACCOUNTS = db.Column(db.String(50))
        CHARGEFROMPREPAID = db.Column(db.String(50))
        PREPAIDBALANCE = db.Column(db.String(50))
        CHARGEFROMPOSTPAID = db.Column(db.String(50))
        POSTPAIDBALANCE = db.Column(db.String(50))
        ACCOUNTID = db.Column(db.String(50))
        CURRENCYCODE = db.Column(db.String(50))
        RESERVED3 = db.Column(db.String(50))
        ACCOUNTTYPE1 = db.Column(db.String(50))
        FEETYPE1 = db.Column(db.String(50))
        CHARGEAMOUNT1 = db.Column(db.String(50))
        CURRENTACCTAMOUNT1 = db.Column(db.String(50))
        ACCOUNTTYPE2 = db.Column(db.String(50))
        FEETYPE2 = db.Column(db.String(50))
        CHARGEAMOUNT2 = db.Column(db.String(50))
        CURRENTACCTAMOUNT2 = db.Column(db.String(50))
        ACCOUNTTYPE3 = db.Column(db.String(50))

        FEETYPE3 = db.Column(db.String(50))
        CHARGEAMOUNT3 = db.Column(db.String(50))
        CURRENTACCTAMOUNT3 = db.Column(db.String(50))
        ACCOUNTTYPE4 = db.Column(db.String(50))
        FEETYPE4 = db.Column(db.String(50))
        CHARGEAMOUNT4 = db.Column(db.String(50))
        CURRENTACCTAMOUNT4 = db.Column(db.String(50))
        ACCOUNTTYPE5 = db.Column(db.String(50))
        FEETYPE5 = db.Column(db.String(50))
        CHARGEAMOUNT5 = db.Column(db.String(50))
        CURRENTACCTAMOUNT5 = db.Column(db.String(50))
        ACCOUNTTYPE6 = db.Column(db.String(50))
        FEETYPE6 = db.Column(db.String(50))
        CHARGEAMOUNT6 = db.Column(db.String(50))
        CURRENTACCTAMOUNT6 = db.Column(db.String(50))
        ACCOUNTTYPE7 = db.Column(db.String(50))
        FEETYPE7 = db.Column(db.String(50))
        CHARGEAMOUNT7 = db.Column(db.String(50))
        CURRENTACCTAMOUNT7 = db.Column(db.String(50))
        ACCOUNTTYPE8 = db.Column(db.String(50))
        FEETYPE8 = db.Column(db.String(50))
        CHARGEAMOUNT8 = db.Column(db.String(50))
        CURRENTACCTAMOUNT8 = db.Column(db.String(50))
        ACCOUNTTYPE9 = db.Column(db.String(50))
        FEETYPE9 = db.Column(db.String(50))
        CHARGEAMOUNT9 = db.Column(db.String(50))
        CURRENTACCTAMOUNT9 = db.Column(db.String(50))
        ACCOUNTTYPE10 = db.Column(db.String(50))
        FEETYPE10 = db.Column(db.String(50))
        CHARGEAMOUNT10 = db.Column(db.String(50))
        CURRENTACCTAMOUNT10 = db.Column(db.String(50))
        BONUSVALIDITY1 = db.Column(db.String(50))
        BONUSVALIDITY2 = db.Column(db.String(50))
        BONUSVALIDITY3 = db.Column(db.String(50))
        BONUSVALIDITY4 = db.Column(db.String(50))
        BONUSVALIDITY5 = db.Column(db.String(50))
        BONUSVALIDITY6 = db.Column(db.String(50))
        BONUSVALIDITY7 = db.Column(db.String(50))
        BONUSVALIDITY8 = db.Column(db.String(50))
        BONUSVALIDITY9 = db.Column(db.String(50))
        BONUSVALIDITY10 = db.Column(db.String(50))
        RESERVED4 = db.Column(db.String(50))
        RESERVED5 = db.Column(db.String(50))
        RESERVED6 = db.Column(db.String(50))
        RESERVED7 = db.Column(db.String(50))
        ADDTIONALINFO = db.Column(db.String(50))
        CHARGEMODE = db.Column(db.String(50))
        CDRPRODUCTID = db.Column(db.String(50))
        CDRCHARGEMODE = db.Column(db.String(50))
        CDRTIMES = db.Column(db.String(50))
        CDRDURATION = db.Column(db.String(50))
        CDRVOLUME = db.Column(db.String(50))
        CDRCDRTYPE = db.Column(db.String(50))
        CDRSERVICETYPE = db.Column(db.String(50))
        CDRBEGINTIME = db.Column(db.String(50))
        CDRENDTIME = db.Column(db.String(50))
        CDRPKGSPID = db.Column(db.String(50))
        CDRPKGSERVICEID = db.Column(db.String(50))
        CDRPKGPRODUCTID = db.Column(db.String(50))
        CDRSPNAME = db.Column(db.String(50))
        CDRSERVICENAME = db.Column(db.String(50))
        STARTTIMEOFBILLCYCLE = db.Column(db.String(50))

                
        con.execute("LOAD DATA INFILE 'C:/Users/alozw_000/PycharmProjects/etl/file/"+str(i)+"/out.unl' \
                    INTO TABLE dataInfo"+str(i)+" FIELDS TERMINATED BY '|' ENCLOSED BY '\"' ESCAPED BY '\\\\'")


def filepath(dat,noOfthreads):

    for i in range(1,noOfthreads):
    
        curFilepath = "file/"+str(i)+"/out.unl"

        newFilepath = "Archive/LoadedFile/"+str(i)+"/"+dat+"/out.unl"
                
        os.rename(curFilepath,newFilepath)


def main():

    noOfthreads = int(input('Enter the number of table in the database'))

    noOfthreads += 1

    engine = create_engine('mysql+pymysql://root:@localhost/etldb')
    metadata = MetaData(bind=engine)

    con = engine.connect()

    curtime = time.localtime()

    dat = time.strftime('%Y%m%d%H%M%S',curtime)

    processquery(con,noOfthreads)

    filepath(dat,noOfthreads)


if __name__ == "__main__":

    main()
