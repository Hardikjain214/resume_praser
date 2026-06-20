from flask import Flask, render_template, request, jsonify
from parser import parse_resume
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():

    file = request.files['resume']

    filepath = os.path.join("resumes", file.filename)

    file.save(filepath)

    result = parse_resume(filepath)

    return render_template(
    "result.html",
    data=result
)

if __name__ == "__main__":
    app.run(debug=True)