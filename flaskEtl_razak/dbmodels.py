from app import db

class stream(db.Model):

    __tablename__ = "stream"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))
    sample_filename = db.Column(db.String(100))
    in_dir = db.Column(db.String(200))
    compressed = db.Column(db.Integer)
    ftp = db.Column(db.Integer)

    def __init__(self, name, sample_filename, in_dir, compressed, ftp):
        self.name = name
        self.sample_filename = sample_filename
        self.in_dir = in_dir
        self.compressed = compressed
        self.ftp = ftp

    def __repr__(self):
        return '{}'.format(self.name)

class fileStatus(db.Model):
    __tablename__ = 'file_status'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(32))
    stream_id = db.Column(db.Integer, nullable=False)
    ref_date = db.Column(db.Date)
    record_count = db.Column(db.Integer)
    generate_session_id = db.Column(db.Integer, nullable=False)
    load_session_id = db.Column(db.Integer)
    size = db.Column(db.Integer)
    archived = db.Column(db.Integer)

    def __init__(self, file_name, stream_id, ref_date, record_count, generate_session_id, load_session_id, size, archived):
        self.file_name = file_name
        self.stream_id = stream_id
        self.ref_date = ref_date
        self.record_count = record_count
        self.generate_session_id = generate_session_id
        self.load_session_id = load_session_id
        self.size = size
        self.archived = archived

    def __repr__(self):
        return '{}'.format(self.file_name)


class ftpTable(db.Model):
    __tablename__ = 'ftp_table'

    id = db.Column(db.Integer, primary_key=True)
    stream_id = db.Column(db.Integer, nullable=False)
    ftp_type = db.Column(db.String(32))
    ip = db.Column(db.String(32))
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    remote_dir = db.Column(db.String(100))
    local_dir = db.Column(db.String(100))
    search_query = db.Column(db.String(32))

    def __init__(self, stream_id, ftp_type, ip, username, password, remote_dir, local_dir, search_query):
        self.stream_id = stream_id
        self.ftp_type = ftp_type
        self.ip = ip
        self.username = username
        self.password = password
        self.remote_dir = remote_dir
        self.local_dir = local_dir
        self.search_query = search_query

    def __repr__(self):
        return '{}'.format(self.username)


class GenerateHistory(db.Model):
    __tablename__ = 'generate_history'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    stage = db.Column(db.String(200))
    generate_session_id = db.Column(db.Integer, nullable=False)

    def __init__(self, timestamp, stage, generate_session_id):
        self.timestamp = timestamp
        self.stage = stage
        self.generate_session_id = generate_session_id

    def __repr__(self):
        return '{}'.format(self.stage)


class GenerateSession(db.Model):
    __tablename__ = 'generate_session'

    id = db.Column(db.Integer, primary_key=True)
    ref_date = db.Column(db.Date)
    start_time = db.Column(db.String(60))
    status = db.Column(db.String(32))
    end_time = db.Column(db.String(60))
    duration = db.Column(db.String(60))
    stream_id = db.Column(db.Integer, nullable=False)

    def __init__(self, ref_date, start_time, status, end_time, duration, stream_id):
        ref_date = ref_date
        start_time = start_time
        status = status
        end_time = end_time
        duration = duration
        stream_id = stream_id
        
    def __repr__(self):
        return '{}'.format(self.duration)
    
    '''def startGenSession(self, ref_date, stream_id): 
        
        newGenSession= GenerateSession (ref_date=ref_date, start_time = dt.datetime.now(), status = "STARTING", stream_id = stream_id)
        session.add(newGenSession)
        session.commit()
        self.genSession=newGenSession'''

        
class LoadSession(Base):
    __tablename__ = 'load_session'

    id = db.Column(db.Integer, primary_key=True)
    stream_id = db.Column(db.Integer, nullable=False)
    ref_date = db.Column(db.Date)
    start_time = db.Column(db.DateTime)
    status = db.Column(db.String(32))
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)

    def __init__(self, strean_id, ref_date, start_time, status,end_time, duration):
        self.stream_id = stream_id
        self.ref_date = ref_date
        self.start_time = start_time
        self.status = status
        self.end_time = end_time
        self.duration = duration
            
    def __repr__(self):
        return '{}'.format(self.duration)



class LoadingHistory(Base):
    __tablename__ = 'loading_history'

    id = db.Column(db.Integer, primary_key=True)
    load_session_id = dbColumn(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime)
    stage = db.Column(db.String(200))

    def __init__(self, load_session_id, timestamp, stage):
        self.load_session_id = load_session_id
        self.timestamp = timestamp
        self.stage = stage
            
    def __repr__(self):
        return '{}'.format(self.stage)



