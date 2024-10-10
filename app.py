from flask import Flask
from import_data import init_accident

app = Flask(__name__)

init_accident()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
