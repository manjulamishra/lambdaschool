from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/birthday')
def birthday():
	return '<head><title>My Birthday</title></head><h2>January 11 1989</h2>'

@app.route('/<x>')
def name(x):
	return '<head><title>Greetings!</title></head>Hello %s!' % (x)

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
	x = num1 + num2
	return '<h2>The sum of %s and %s is %s</h2>'	% (num1, num2, x)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
	x = num1 * num2
	return '<h2>%s multiplied by %s equals %s</h2>' % (num1, num2, x)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
	x = num1 - num2
	return '<h2>%s minus %s is %s</h2>' % (num1, num2, x)

@app.route('/favoritefoods')
def favoritefoods():
	x = ['pizza', 'sushi', 'burgers', 'gummies', 'whiskey']
	x = jsonify(x)
	return x
	