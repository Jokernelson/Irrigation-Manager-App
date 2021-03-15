from flask import *
import logging
logging.basicConfig(level=logging.INFO)
app = Flask(__name__, template_folder='templates')

LOGIN_TOKEN = 'oq3it4jqioej4tgoiehrlisherg'

#This is my home page
@app.route('/')
@app.route('/index')
def index():
    logging.info('LOGIN_SESSION_TOKEN:')
    logging.info(request.cookies.get('login_session'))

    if request.cookies.get('login_session') == LOGIN_TOKEN:
        return redirect('/dashboard')
    else:
        return render_template('index.html', title='Welcome')

#this is the login handler: checks if my username and password are correct or not
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    username_correct = False
    password_correct = False
    response = ''
    if username == 'joey':
        response += 'Username is correct. <br>'
        username_correct = True
    else:
        response += 'Username is incorrect. Please try again. <br>'

    if password == '1234':
        response += 'Password is correct. <br>'
        password_correct = True
    else:
        response += 'Password is incorrect. Please try again. <br>'
    
    if username_correct == True and password_correct == True:
        resp = make_response(redirect('/dashboard'))
        resp.set_cookie('login_session', str(LOGIN_TOKEN), max_age=None, httponly=True)

        logging.info('LOGIN_SESSION_TOKEN:')
        logging.info(request.cookies.get('login_session'))
        logging.info('redirecting...')
        return resp
    else:
        return response

@app.route('/dashboard')
def dashboard():
    if request.cookies.get('login_session') != LOGIN_TOKEN:
        return redirect('/')
    else:
        return render_template('dashboard.html', title='Dashboard')

@app.route('/dashboard/map')
def dashboard_map():
    if request.cookies.get('login_session') != LOGIN_TOKEN:
        return redirect('/')
    else:
        return render_template('map.html', title='Map')

@app.route('/dashboard/settings')
def dashboard_settings():
    if request.cookies.get('login_session') != LOGIN_TOKEN:
        return redirect('/')
    else:
        return render_template('settings.html', title='Settings')

@app.route("/logout")
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('login_session', '', max_age=None, httponly=True)
    return resp

@app.route("/info")
def info():
    return "info page"

if __name__ == '__main__':
   app.run()