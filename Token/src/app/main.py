from flask import Flask, render_template, request, session, make_response, jsonify, redirect, url_for
from . import jwt_handler as jwt
import os

app = Flask(__name__)

with open('pass.txt', 'r') as password:
	passwd = password.read()

def checkuser():
    if request.cookies.get('session'):
        cookie = request.cookies.get('session')
        decode = jwt.decode(cookie)
        if decode:
            user = jwt.extract(decode, 'user')
            return user
    else:
        return None
    
@app.route('/')
def home():
    return render_template('register.html')
	
	
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if name == 'admin':
        return 'User already exists, nice try', 400
    elif name and email and password:
        token = jwt.create(name, email)
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('session', token.decode('utf-8'))
        return response
    else:
        return 'All fields are required', 400

@app.route('/welcome')
def welcome():
	user = checkuser()
	if user:
		return render_template('welcome.html', username=user)
	else:
		return redirect(url_for('home'))

@app.route('/admin')
def admin():
    if (checkuser() == 'admin'):
        return render_template('admin.html', output="")
    else:
        return redirect(url_for('welcome'))
        
@app.route('/exec', methods=['POST'])
def exec():
    if (checkuser() == 'admin'):
        code = request.form.get('command')
        try:
            result = eval(code)
            return render_template('admin.html', output=result)
        except Exception as e:
            return render_template('admin.html', ouput=f"{e}")	
    else:
         return redirect(url_for('welcome'))	
		
    
if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=5000)
