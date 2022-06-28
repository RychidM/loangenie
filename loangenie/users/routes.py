from datetime import datetime
import pickle
import re
from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, current_user,logout_user, login_required
from flask_mail import Message
from itsdangerous import SignatureExpired, URLSafeTimedSerializer
import numpy as np
from loangenie import db, bcrypt, mail
from loangenie.models import Users, Candidates
from loangenie.configure import secrete_key

users = Blueprint('users', __name__)

s = URLSafeTimedSerializer(secrete_key)


model = pickle.load(open('dtModel.pkl', 'rb'))

@users.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    else:
        fullname = request.form['Fullname']
        userName = request.form['Username']
        emailAddress = request.form['emailAddress']
        org = request.form['org']
        password2 = request.form['conPass']
        password1 = request.form['Password']
        
        if not check_password(password1):
            flash('Invalid password')
            return redirect(url_for('users.register'))
        elif password2 != password1:
            flash('Password mismatch')
            return redirect(url_for('users.register'))

        else: 

            hashedPassword = bcrypt.generate_password_hash(password2).decode('utf-8')

            newUser = Users(name=fullname, username=userName, email=emailAddress,
             organization=org, password=hashedPassword)
      
            oldUser = Users.query.filter_by(username = userName).first()
            if oldUser:
                    return render_template('register.html', errormsg= 'Username is taken')

            try:
                db.session.add(newUser)
                db.session.commit()
                token = s.dumps(emailAddress)
                msg = Message('Verify Email')
                msg.add_recipient(emailAddress)
                link = url_for('users.confirm_email', token=token, _external=True)
                msg.body = 'Please follow link to verify your email address {}'.format(link)
                mail.send(msg)
            except:
             return "Unable to register you at the momment :( , please wait a while and try again"
            return redirect(url_for('users.email_confirmation'))
            
    # return render_template('register.html', errorMsg = 'password mismatch')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        userIn = Users.query.filter_by(username = request.form['userName']).first()
        if userIn:
            
            if userIn and bcrypt.check_password_hash(userIn.password, request.form['password']):
                login_user(userIn)
                
                return redirect(url_for('users.dashboard'))

        return render_template('login.html', errormsg = 'invalid email or password')
    else:

        return render_template('login.html')


@users.route('/user-account')
@login_required
def userAccount():
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('userAccount.html', image_file =image_file, name= current_user.name, org = current_user.organization,
     emailAdd=current_user.email, passWord=current_user.password)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, max_age=900)
    except SignatureExpired:
        return '<h2>Link expired</h2>'
    return redirect(url_for('users.login'))

@users.route('/email-confirmation')
def email_confirmation():
    return render_template('email_confirmation.html')

@users.route("/predict", methods=['POST', 'GET'])
@login_required
def predict():

    if request.method == 'GET':
        return render_template('predict.html')

    if request.method == 'POST':

        CandName = request.form['Fullname']
        CandEmail = request.form['emailAddress']
        CandTel = request.form['telNumber']

        d1 = request.form['Married']
        if d1 == 'No':
            d1 = 0
        else:
            d1 = 1
        d2 = request.form['Gender']
        if (d2 == 'Male'):
            d2 = 1
        else:
            d2 = 0
        d3 = request.form['Education']
        if (d3 == 'Graduate'):
            d3 = 1
        else:
            d3 = 0
        d4 = request.form['Self_Employed']
        if (d4 == 'No'):
            d4 = 0
        else:
            d4 = 1
        d5 = request.form['ApplicantIncome']
        d6 = request.form['CoapplicantIncome']
        d7 = request.form['LoanAmount']
        d8 = request.form['Loan_Amount_Term']
        d9 = request.form['Credit_History']
        if (d9 == 'All debts paid'):
            d9 = 1
        else:
            d9 = 0
        d10 = request.form['Property_Area']
        if (d10 == 'Urban'):
            d10 = 2
        elif (d10 == 'Rural'):
            d10 = 0
        else:
            d10 = 1
        d11 = request.form['Dependents']
        if (d11 == '3+'):
            d11 = 3
        elif (d11=='2'):
            d11 = 2
        elif (d11=='1'):
            d11 = 1
        else:
            d11 = 0
        arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9,d10,d11]])

        pred = model.predict(arr)
        newCand = Candidates(candidateName=CandName, candidateEmail=CandEmail, candidateTell=CandTel, loanAmount=d7, loanStatus = pred)
        
        try:
            db.session.add(newCand)
            db.session.commit()
        except:
            return "error"
        
        if pred == 1:
            
            flash("Candidate is eligible for loan")
            return render_template('predict.html')
        else:
            flash("Candidate is not eligible for Loan")
            return render_template('predict.html')
    
    newCand = Candidates(candidateName=CandName, candidateEmail=CandEmail, candidateTell=CandTel, loanAmount=d7)   
    try:
        db.session.add(newCand)
        db.session.commit()
    except:
         return "error"

@users.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    candidates = Candidates.query.all()
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('dashboard.html', candidates = candidates,
    name=current_user.username, image_file =image_file, dateCrr = datetime.utcnow)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com',
    recipients=[user.email])
    msg.body = f'''Kindly follow link to reset your password.
{url_for('users.resetToken', token = token, _external=True )}

If you did not make this request, please ignore this message and no change will be made.
    
'''
    mail.send(msg)

def check_password(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)
    mat = re.search(pat, password)

    if mat:
        return password
    else:
        return None

@users.route('/reset-password', methods=['POST', 'GET'])
def resetRequest():

    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('users.dashboard'))
        return render_template('request_reset.html')
        
    else:
        emailAddress = request.form['emailAdd']
        user = Users.query.filter_by(email= emailAddress).first()
        if user is None:
            return render_template('request_reset.html', noUser="No user found with this email address")
        else:
            send_reset_email(user)
            flash("An email with a password reset link has been sent to the email address you provided.")
        return render_template('request_reset.html')

@users.route('/reset-password/<token>', methods=['POST', 'GET'])
def resetToken(token):
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('users.dashboard'))
        user = Users.verify_reset_token(token)

        if not user:
            flash('Invalid or expired token', 'danger')
            return redirect(url_for('users.resetRequest'))
    else:
        user = Users.verify_reset_token(token)

        password = request.form['password']
        password1 = request.form['ConPassword']

        if not check_password(password1):
            flash('Invalid password')
            return redirect(url_for('users.resetToken', token=token))
        elif password != password1:
            flash('Password mismatch')
            return redirect(url_for('users.resetToken', token = token))
        else:
            hashed_password = bcrypt.generate_password_hash(password1).decode('utf8')
            user.password = hashed_password
            db.session.commit()
            flash('Password changed', 'warining')
            return redirect(url_for('users.login'))  
    return render_template('reset_password.html')


@users.route('/reset', methods=['POST', 'GET'])
def reset():
    return render_template('reset_password.html')