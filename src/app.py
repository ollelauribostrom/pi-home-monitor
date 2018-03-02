import os
from dotenv import load_dotenv
from os.path import join, dirname
from flask import Flask, jsonify, request
from src.Bot import Bot

load_dotenv(join(dirname(__file__), '../.env'))
shared_secret = os.environ.get("SHARED_SECRET")

app = Flask(__name__)
bot = Bot(shared_secret)

@app.route('/')
def root():
  return jsonify({ 'message': 'Monitor API is up and running' })

@app.route('/message', methods=['POST'])
def message():
  return bot.reply(request.form)