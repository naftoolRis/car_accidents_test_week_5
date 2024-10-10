from flask import Flask
from utils.import_data import init_accident

app = Flask(__name__)

init_accident()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
