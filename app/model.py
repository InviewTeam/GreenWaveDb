from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class LightsInfo(db.Model):
    __tablename__ = "greenwave"

    id = db.Column('record_id', db.Integer, primary_key=True, autoincrement=True)
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

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()
