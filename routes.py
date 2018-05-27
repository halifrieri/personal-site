from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('layout.html')

@app.route("/snake")
def snake():
	return render_template('snake.html')