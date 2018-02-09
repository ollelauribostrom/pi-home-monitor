from flask import Flask, jsonify, request
from src.sms import sms_reply

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify({ 'message': 'Monitor API is up and running' })

@app.route('/message', methods=['POST'])
def message():
  return sms_reply(request.form)
