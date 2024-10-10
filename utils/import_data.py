import csv
from database.db import accident_db, injuries_db
from datetime import datetime
def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)

def init_accident():
    accident_db.drop()
    injuries_db.drop()

    for row in read_csv('./data/Traffic_Crashes.csv'):

            accident = {
                'accident_date': parse_date(row['CRASH_DATE']),
                'prim_contributory': row['PRIM_CONTRIBUTORY_CAUSE'],
                'accident_area': row['BEAT_OF_OCCURRENCE'],
                'injuries_id': ""
            }

            inserted_accident = accident_db.insert_one(accident)
            accident_id_db = inserted_accident.inserted_id

            injuries = {
                'accident_id': accident_id_db,
                'injuries_total': row['INJURIES_TOTAL'],
                'injuries_fatal': row['INJURIES_FATAL']
            }

            inserted_injuries = injuries_db.insert_one(injuries)
            injuries_id_db = inserted_injuries.inserted_id
            accident_db.update_one({'_id': accident_id_db},
                                   {'$set': {'injuries_id': injuries_id_db}})
