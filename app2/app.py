from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World from app2!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0')

