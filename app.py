from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

app.route('/tabla', methods=["GET"])
def tabla():
    return render_template('tabla.html')

plants = [
    {"name": "Monstera", "type": "Szobanövény", "feature": "Nagyméretű levelek"},
    {"name": "Bambusz", "type": "Dísznövény", "feature": "Gyors növekedés"},
    {"name": "Kaktusz", "type": "Pozsgás", "feature": "Szárazságtűrő"}
]


