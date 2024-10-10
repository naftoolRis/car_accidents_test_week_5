from flask import Flask
from blue_prints.init_data_dp import init_data_dp

app = Flask(__name__)
app.register_blueprint(init_data_dp)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
