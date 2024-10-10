from flask import Blueprint, jsonify

statistics_bp = Blueprint('statistics', __name__)

@statistics_bp.route('/statistics/<string:area>', methods=['GET'])
def count_crash_area(area):
    """קבלת מספר התאונות לפי אזור"""
    result = get_crash_count_by_area(area)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'No data found'}), 404

@statistics_bp.route('/statistics/<string:area>/<string:period_time>', methods=['GET'])
def count_crash_area_and_period_time(area, period_time):
    """מחזיר את סכום התאונות באותו אזור באותה תקופה"""
    result = get_count_crash_area_and_period_time(area, period_time)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'No data found'}), 404

@statistics_bp.route('/statistics/<string:area>/<string:contributory>', methods=['GET'])
def count_by_contributory(area, contributory):
    """מחזיר כמות תאונות לפי סיבה ואזור"""
    result = get_count_by_contributory(area, contributory)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'No data found'}), 404

@statistics_bp.route('/statistics/injuries/<string:area>', methods=['GET'])
def count_by_injuries(area):
    """מחזיר כמות פציעות לפי אזור ומזהים של התאונות"""
    result = get_count_by_injuries(area)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'No data found'}), 404
