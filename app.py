from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/history')
def historypage():
	return render_template("history.html")

@app.route('/gallery')
def cartpage():
	return render_template("gallery.html")

@app.route('/API')
def aboutpage():
	return render_template("API.html")

#####################


if __name__ == '__main__': app.run(host='0.0.0.0', debug=True )