from app import app
from forms import FeedbackForm


@app.route('/')
def home():
	form = FeedbackForm()
	return render_template('index.html', form=form)

