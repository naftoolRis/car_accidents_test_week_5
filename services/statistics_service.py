from database import db
from datetime import datetime, timedelta


def get_crash_count_by_area(area):
    # קבלת מספר התאונות לפי אזור
    try:
        count = db.accident_db.count_documents({'accident_area': area})
        if count:
            return {'count': count}, 200
        else:
            return {'error': 'No data found for the specified area'}, 404
    except Exception as e:
        return {'error': str(e)}, 500  # החזרת שגיאה עם פרטים


def get_end_time(date_str, period_time):
    # קביעת תאריך סיום בהתבסס על תאריך התחלה ותקופת זמן
    date = datetime.strptime(date_str, '%d-%m-%Y')

    times = {
        'day': date + timedelta(days=1),
        'week': date + timedelta(weeks=1),
        'month': date + timedelta(days=30)
    }
    if period_time in times:
        end_date = times[period_time]
    else:
        raise ValueError("Invalid period time")  # טיפול במקרה של תקופה לא תקינה
    return end_date


def get_count_crash_area_and_period_time(area, date_str, period_time):
    # קבלת מספר התאונות לפי אזור ובתקופת זמן
    start_date = datetime.strptime(date_str, '%d-%m-%Y')  # המרת מחרוזת לתאריך
    end_date = get_end_time(date_str, period_time)

    try:
        count = db.accident_db.count_documents({
            'accident_area': area,
            'accident_date': {
                '$gte': start_date,
                '$lt': end_date
            }
        })

        if count >= 0:
            return {'count': count}, 200
        else:
            return {'error': 'No data found for the specified area'}, 404
    except Exception as e:
        return {'error': str(e)}, 500  # החזרת שגיאה עם פרטים


def get_count_by_contributory(area, contributory):
    try:
        result = db.accident_db.aggregate([
            {'$match': {
                'accident_area': area
            }},
            {'$group': {
                '_id': contributory,
                'count': {'$sum': 1}}}
        ])
        result = list(result)
        if result:
            return {'area': area, 'contributory': contributory, 'count': result[0]['count']}, 200
        else:
            return {'error': 'No data found for the specified area'}, 404
    except Exception as e:
        print(f"Error: {str(e)}")
        return {'error': str(e)}, 500


def get_count_by_injuries(area):
    try:
        result = db.accident_db.aggregate([
            {'$match': {'accident_area': area}},
            {'$lookup': {
                'from': 'injuries',
                'localField': 'accident_id',
                'foreignField': 'injuries_id',
                'as': 'injury_details'
            }},
            {
                '$group': {
                    '_id': None,
                    'total_injuries': {
                        '$sum': {
                            '$subtract': [
                                ['$injury_details.injuries_total'],
                                ['$injury_details.injuries_fatal']
                            ]
                        }
                    },
                    'total_fatal_injuries': {
                        '$sum': ['$injury_details.injuries_fatal']}
                    },
                    'accident_ids': {'$addToSet': '$accident_id'}
            }
        ])


        result = list(result)

        if result:
            return {
                'area': area,
                'total_injuries': result[0].get('total_injuries', 0),
                'total_fatal_injuries': result[0].get('total_fatal_injuries', 0),
                'accident_ids': result[0].get('accident_ids', [])
            }, 200
        else:
            return {'error': 'No data found for the specified area'}, 404

    except Exception as e:
        return {'error': str(e)}, 500
