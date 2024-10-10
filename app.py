from flask import Flask
from blue_prints.init_data_dp import init_data_dp
from blue_prints.statistics_dp import statistics_bp
from utils.import_data import init_data

app = Flask(__name__)
app.register_blueprint(init_data_dp)
app.register_blueprint(statistics_bp)
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
