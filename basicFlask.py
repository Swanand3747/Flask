from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<h1>Hello, Swanand, Its Your first Web!</h1>"

@app.route("/About")
def About():
    return"<h1>Hello, About myself!</h1>"


@app.route("/login")
def About():
    return"<h1>login to my web!</h1>"


@app.route("/test")
def test():
    data = request.args.get('x')
    return "This is the data input from my url {}".format(data)



if __name__ == '__main__':
    app.run(host="0.0.0.0")