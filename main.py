from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html', name="some name")

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
