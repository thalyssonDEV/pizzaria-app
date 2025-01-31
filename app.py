from flask import Flask, render_template, request, redirect, url_for, session
import conn

# Server Flask
app = Flask(__name__)

@app.route('/')
def home() -> None:
    return render_template('index.html')

conn.connect_to_db()