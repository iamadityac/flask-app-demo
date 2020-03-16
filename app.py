
from flask import Flask, render_template, request, redirect, url_for, session
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "MyFlaskAPP"

@app.route('/')
def index():
    return render_template('about.html')
if __name__ == '__main__':
	app.run(debug=True)