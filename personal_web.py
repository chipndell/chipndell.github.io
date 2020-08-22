from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yfwqfbwjeacwkleavn bwrfbqwlfwenfqwefqwf'

if __name__ == "__main__":
	app.run()




@app.route('/')
def index():
	return render_template('index.html')
