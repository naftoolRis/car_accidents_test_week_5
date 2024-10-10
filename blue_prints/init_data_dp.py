from flask import Blueprint
from utils.import_data import init_data

init_data_dp = Blueprint('init_data', __name__)

@init_data_dp.route('/init_data', methods=['POST'])
def init_data_from_csv():
    result = init_data()
    if result:
        return 'data inserted successfully'
    else:
        return 'data insertion failed'