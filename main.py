from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('sign_up.html')

# verifies user input
@app.route("/", methods=['POST'])
def user_validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    email_error = ""
    verify_error = ""
    pass_error = ""
    user_error = ""

#verifies username
    if len(username) == 0:
        user_error = "Cannot be left blank"
        username = ""

    if len(username) < 3 and len(username) >= 1:
        user_error = "Must contain more than 3 characters"
        username = ""
    
    if len(username) > 20:
        user_error = "Must be less than 20 characters"
        username = ""

    for char in username:
        if char.isspace():
            user_error = "Cannot contain spaces"
            username = ""

#verifies password
    if len(password) == 0:
        pass_error = "Cannot be left blank"
        password = ""

    if len(password) < 3 and len(password) >= 1:
        pass_error = "Must contain more than 3 characters"
        password = ""
    
    if len(password) > 20:
        pass_error = "Must be less than 20 characters"
        password = ""

    for char in password:
        if char.isspace():
            pass_error = "Cannot contain spaces"
            password = ""

#verifies password verification
    if len(verify) < 1:
        verify_error = "Cannot be left blank"
        verify = ""

    if password != verify:
        verify_error = "Passwords must match"
        verify = ""

#checks for optional input email validation
    if len(email) >= 1 and "@" and "." not in email:
        email_error = "Not a valid email"
        email = ""

#redirects to welcome page if no errors
    if not email_error and not pass_error and not user_error and not verify_error:
        return render_template("welcome.html", username=username)

    
    return render_template('sign_up.html', username=username, user_error=user_error, 
        password=password, pass_error=pass_error, verify=verify, verify_error=verify_error, email=email, 
        email_error=email_error)


app.run()
