import os
import json
import datetime
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from app.model import db, init_db, LightsInfo
from attributedict.collections import AttributeDict

load_dotenv(find_dotenv())
app = Flask(__name__)
CORS(app)

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_app(app)
with app.app_context():
    init_db()

@app.route('/get/bytime/', methods=['GET'])
def get_records_by_time():
    date_from = datetime.datetime.strptime(request.args.get('from'), '%Y-%m-%d %H:%M:%S')
    date_to = datetime.datetime.strptime(request.args.get('to'), '%Y-%m-%d %H:%M:%S')
    records = db.session.query(LightsInfo).filter(LightsInfo.date >= date_from, LightsInfo.date <= date_to)
    return jsonify({'error': None, 'records': [record.serialize() for record in records]}), 200

@app.route('/get/all/', methods=['GET'])
def get_all():
    records = LightsInfo.query.all()
    return jsonify({'error': None, 'records': [record.serialize() for record in records]}), 200

@app.route('/add/record', methods=['POST'])
def add_record():
    light_id = str(request.form.get('light_id'))
    interval = str(request.form.get('interval'))
    date = str(request.form.get('date'))
    success_counter = str(request.form.get('success_counter'))
    fail_counter = str(request.form.get('fail_counter'))


    lights_request = LightsInfo(light_id, interval, date, success_counter, fail_counter)
    db.session.add(lights_request)
    db.session.commit()
    
    return jsonify({'error': None}), 200
