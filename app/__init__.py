from flask import Flask, render_template, url_for


app = Flask(__name__)


# from flask_mail import Mail
# from flask_bootstrap import Bootstrap


# Bootstrap(app)
# mail = Mail(app)
# form = FeedbackForm()


if __name__ == "__main__":
	app.run(debug=True)

