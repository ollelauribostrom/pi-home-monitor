from flask import Flask, jsonify, request, abort, send_file
from os.path import join, dirname
from src.Bot import Bot
from src.Log import Log
from src.Radio import Radio
from src.NumberService import NumberService
from src.MotionDetector import MotionDetector
from src.config import config

# Create instances
app = Flask(__name__)
log = Log()
numbers = NumberService(config, log)
radio = Radio()
bot = Bot(config, numbers, radio)
monitor = MotionDetector(config)

## Start monitor and subscribe to motion events
monitor.start()
monitor.listen('motion', bot.motion_handler)

@app.route('/')
def root():
  return jsonify({ 'message': 'Monitor API is up and running' })

@app.route('/message', methods=['POST'])
def message():
  return bot.reply(request.form)

@app.route('/video/<filename>', methods=['GET'])
def video(filename):
  token = request.args.get('token')
  if numbers.is_valid_token(token):
    return send_file(join(dirname(__file__), '../data/{}'.format(filename)))
  else:
    abort(401)