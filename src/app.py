from flask import Flask, render_template, request, redirect, url_for
from config import config

app=Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        print(request.form['email'])
        print(request.form['password'])
        return render_template('auth/register.html')
    else:
        return render_template('auth/register.html')

if __name__ =='__main__':
    app.config.from_object(config['development'])
    app.run()