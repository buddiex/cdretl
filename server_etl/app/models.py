from app import db


class FileStatu(db.Model):
    __tablename__ = 'file_status'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(32))
    stream_id = db.Column( db.ForeignKey(u'stream.id'), nullable=False, index=True)
    ref_date = db.Column(db.Date)
    record_count = db.Column(db.Integer)
    generate_session_id = db.Column( db.ForeignKey(u'generate_session.id'), nullable=False, index=True)
    load_session_id = db.Column( db.ForeignKey(u'load_session.id'), nullable=False, index=True)
    size = db.Column(db.Integer)
    archived = db.Column(db.Integer)
    gen_file_name = db.Column(db.String(45))
    file_created_time = db.Column(db.Date)

    generate_session = db.relationship( u'GenerateSession', primaryjoin='FileStatu.generate_session_id == GenerateSession.id', backref=u'file_status')
    load_session = db.relationship(u'LoadSession', primaryjoin='FileStatu.load_session_id == LoadSession.id', backref=u'file_status')
    stream = db.relationship(u'Stream', primaryjoin='FileStatu.stream_id == Stream.id', backref=u'file_status')


class FtpTable(db.Model):
    __tablename__ = 'ftp_table'

    id = db.Column(db.Integer, primary_key=True)
    stream_id = db.Column( db.ForeignKey(u'stream.id'), nullable=False, index=True)
    ftp_type = db.Column(db.String(32))
    ip = db.Column(db.String(32))
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    remote_dir = db.Column(db.String(100))
    local_dir = db.Column(db.String(100))
    search_query = db.Column(db.String(32))

    stream = db.relationship(u'Stream', primaryjoin='FtpTable.stream_id == Stream.id', backref=u'ftp_tables')


class GenerateHistory(db.Model):
    __tablename__ = 'generate_history'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    stage = db.Column(db.String(200))
    generate_session_id = db.Column( db.ForeignKey(u'generate_session.id'), nullable=False, index=True)

    generate_session = db.relationship( u'GenerateSession', primaryjoin='GenerateHistory.generate_session_id == GenerateSession.id', backref=u'generate_histories')


class GenerateSession(db.Model):
    __tablename__ = 'generate_session'

    id = db.Column(db.Integer, primary_key=True)
    ref_date = db.Column(db.Date)
    start_time = db.Column(db.DateTime)
    status = db.Column(db.String(32))
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    stream_id = db.Column(  db.ForeignKey(u'stream.id'), nullable=False, index=True)

    stream = db.relationship(  u'Stream', primaryjoin='GenerateSession.stream_id == Stream.id', backref=u'generate_sessions')


class GenerateThreadControl(db.Model):
    __tablename__ = 'generate_thread_control'

    id = db.Column(db.Integer, primary_key=True)
    stream_id = db.Column(
        db.ForeignKey(u'stream.id'), nullable=False, index=True)
    thread = db.Column(db.Integer)
    status = db.Column(db.String(32))
    message = db.Column(db.String(200))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)

    stream = db.relationship(
        u'Stream', primaryjoin='GenerateThreadControl.stream_id == Stream.id', backref=u'generate_thread_controls')


class LoadSession(db.Model):
    __tablename__ = 'load_session'

    id = db.Column(db.Integer, primary_key=True)
    stream_id = db.Column(
        db.ForeignKey(u'stream.id'), nullable=False, index=True)
    ref_date = db.Column(db.Date)
    start_time = db.Column(db.DateTime)
    status = db.Column(db.String(32))
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)

    stream = db.relationship(
        u'Stream', primaryjoin='LoadSession.stream_id == Stream.id', backref=u'load_sessions')


class LoadThreadControl(db.Model):
    __tablename__ = 'load_thread_control'

    id = db.Column(db.Integer, primary_key=True)
    stream_id = db.Column(
        db.ForeignKey(u'stream.id'), nullable=False, index=True)
    thread = db.Column(db.Integer)
    status = db.Column(db.String(32))
    message = db.Column(db.String(200))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)

    stream = db.relationship(
        u'Stream', primaryjoin='LoadThreadControl.stream_id == Stream.id', backref=u'load_thread_controls')


class LoadingHistory(db.Model):
    __tablename__ = 'loading_history'

    id = db.Column(db.Integer, primary_key=True)
    load_session_id = db.Column(
        db.ForeignKey(u'load_session.id'), nullable=False, index=True)
    timestamp = db.Column(db.DateTime)
    stage = db.Column(db.String(200))

    load_session = db.relationship(
        u'LoadSession', primaryjoin='LoadingHistory.load_session_id == LoadSession.id', backref=u'loading_histories')


class Stream(db.Model):
    __tablename__ = 'stream'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    sample_filename = db.Column(db.String(45))
    in_dir = db.Column(db.String(100))
    compressed = db.Column(db.Integer)
    ftp = db.Column(db.Integer)
    files_per_session = db.Column(db.Integer)
    no_threads = db.Column(db.Integer)