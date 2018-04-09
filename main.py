from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/validate-inputs')
def display_form():
    return render_template('SignUp.html',username='', username_error='',
        password='', password_error='', 
        verify_password='', verify_password_error='', 
        email='', email_error='')
#may not need to show all above

@app.route('/validate-inputs', methods=['POST'])
def validate_inputs():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = 'Username must be 3-20 characters'
        username = ''
        password = ''
        verify_password = ''
    elif ' ' in username:
        username_error = 'Username cannot contain spaces'
        username = ''
        password = ''
        verify_password = ''
    else:
        username = username

    if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be 3-20 characters'
        password = ''
        verify_password = ''
    else:
        password = password

    if password != verify_password:
        verify_password_error = 'Passwords do not match!'
        verify_password = ''
        password = ''

    if len(email) == 0:
        email=email
        email_error=''
    elif '@' in email and '.' in email and len(email) > 2 and len(email) < 21:
        email=email
        email_error=''
    else:
        email_error='Invalid email address'
        email = email
        password = ''
        verify_password = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
        return 'Welcome, '+username+'!'   
    else:
        return render_template('SignUp.html',username=username, password=password, 
        username_error=username_error, password_error=password_error, verify_password=verify_password, 
        verify_password_error=verify_password_error, email=email,
        email_error=email_error)

app.run()