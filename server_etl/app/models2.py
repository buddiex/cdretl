from app import db

# class Buildings(db.Model):
#     __table__ = db.Model.metadata.tables['BUILDING']
#
#     def __repr__(self):
#         return self.DISTRICT
#
#
#


class GenerateSession(db.Model):
    __table__ = db.Model.metadata.tables['generate_session']

    def __repr__(self):
        return self.DISTRICT
