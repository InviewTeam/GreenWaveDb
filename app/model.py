from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
db = SQLAlchemy()

class LightsInfo(db.Model):
    __tablename__ = "greenwave"

    record_id = db.Column('record_id', db.Integer, primary_key=True, autoincrement=True)
    light_id = db.Column('light_id', db.Integer)
    interval = db.Column('interval', db.Integer)
    date = db.Column('date', db.DateTime)
    success_counter = db.Column('success_counter', db.Integer)
    fail_counter = db.Column('fail_counter', db.Integer)

    def __init__(self, light_id, interval, date, success_counter, fail_counter):
        self.light_id = light_id
        self.interval = interval
        self.date = date
        self.success_counter = success_counter
        self.fail_counter = fail_counter

    @staticmethod
    def dump_datetime(value):
        if value is None:
            return None
        return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

    def serialize(self):
        print(self.__dict__)
        return {
            'record_id': self.record_id,
            'light_id': self.light_id,
            'interval': self.interval,
            'date': LightsInfo.dump_datetime(self.date),
            'success_counter': self.success_counter,
            'fail_counter': self.fail_counter
        }

def init_db():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    init_db()
