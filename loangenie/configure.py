from loangenie import app
import os

secrete_key = os.environ.get('SECRETE_KEY')
userPass = os.environ.get('LOAN_GENIE')

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'loangenie3@gmail.com'
app.config['MAIL_PASSWORD'] = userPass
app.config['MAIL_DEFAULT_SENDER'] = 'loangenie@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False