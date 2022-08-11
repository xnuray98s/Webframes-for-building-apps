import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Simple route that return a static text
@app.route('/')
def index():
	return 'This is the index'

# Simple route that return a dynamic text
@app.route('/user/<username>')
def greet_user(username):
	return f'Hello {username}'

# Simple route that return a static page
@app.route('/home')
def homepage():
	return render_template('homepage.html')

model = pickle.load(open("savemodel.sav", 'rb'))

# Simple route that return JSON
@app.route('/predict', methods=["POST"])
def predict():
	body = request.get_json()

	sepal_length = body.get('sepal_length')
	sepal_width = body.get('sepal_width')
	petal_length = body.get('petal_length')
	petal_width = body.get('petal_width')

	prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
	classes = ['setosa', 'versicolor', 'virginica']
	return {
		"prediction": classes[prediction]
	}