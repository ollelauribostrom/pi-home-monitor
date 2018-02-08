from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify({ 'message': 'Monitor API is up and running' })
