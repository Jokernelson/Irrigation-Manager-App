from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Login')

@app.route('/login')
    return render_template('dashboard.html')
if __name__ == '__main__':
   app.run()