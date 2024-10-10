import csv
from db import accident_db
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

   for row in read_csv('Traffic_Crashes.csv'):
       accident = {
           'accident_id': row['CRASH_RECORD_ID'],
           'accident_date': parse_date(row['CRASH_DATE']),
           'prim_contributory': row['PRIM_CONTRIBUTORY_CAUSE'],
           'injuries': {'injuries_total': row['INJURIES_TOTAL'],
                        'injuries_fatal': row['INJURIES_FATAL']},
           'accident_location': row['LOCATION']
       }
       accident_db.insert_one(accident)

