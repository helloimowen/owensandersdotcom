from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route("/")
def hello():


    return render_template("index.html")


@app.route("/fun", methods=['POST', 'GET'])
def fun():

    print(request.cookies.get('fun'))

    if request.cookies.get('fun') is '1':
        response = make_response(render_template('index.html'))
        response.set_cookie('fun', '0')
        return response

    else:
        response = make_response(render_template('fun.html'))
        response.set_cookie('fun', '1')
        return response

    return
