from flask import Flask,request,render_template , jsonify

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def calculator():
    if(request.method == 'POST'):
        operation= request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if operation == 'add':
            r= num1 + num2
            addresult=f'sum of {num1} + {num2} is {r}'

        elif operation == 'subtract':
            r= abs(num1 - num2)
            addresult=f'subtractio of {num1} - {num2} is {r}'

        elif operation == 'multiply':
            r= num1*num2
            addresult=f'multiplication of {num1} * {num2} is {r}'

        elif operation == 'divide':
            r= num1/num2
            addresult=f'Division of {num1} / {num2} is {r}'
    else:
        addresult =f'(operation) is either not arithmetic or its not supported'
        return render_template('result.html',result=addresult)
        

        return render_template('results.html',result = addresult)

    

# @app.route("/")
# def hello_world():
#     return"<h1>Hello, Swanand, Its Your first Web!</h1>"

@app.route("/About")
def About():
    return"<h1>Hello, About myself!</h1>"


@app.route("/login")
def My_Login():
    return"<h1>login to my web!</h1>"


@app.route("/test")
def test():
    data = request.args.get('x')
    return "This is the data input from my url {}".format(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
