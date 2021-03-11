from flask import Flask, render_template, request
import Cookie
app = Flask(__name__, template_folder='templates')


#THis is my home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome')

#this is the login handler: checks if my username and password are correct or not
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    response = ''
    if username == 'joey':
        response += 'Username is correct. <br>'
    else:
        response += 'Username is incorrect. Please try again. <br>'
    if password == '1234':
        response += 'Password is correct. <br>'
    else:
        response += 'Password is incorrect. Please try again. <br>'
    return response


#   return render_template('dashboard.html')


if __name__ == '__main__':
   app.run()