import cv2
import imutils
import time
from os.path import join, dirname
import os
import threading
from src.EventEmitter import EventEmitter
from src.utils.image_utils import is_movement

class MotionDetector(threading.Thread, EventEmitter):

  def __init__(self, config):
    threading.Thread.__init__(self)
    EventEmitter.__init__(self)
    self.camera = None
    self.recording = False
    self.movement_timeout = None
    self.file_format = config['file_format']
    self.frame_width = config['frame_width']
    self.fourcc = cv2.VideoWriter_fourcc(*config['fourcc'])
    self.fps = config['fps']

  def __del__(self):
    self.stop_camera()
    if self.output:
      self.output.release()
      
  def run(self):
    if self.camera is None:
      self.start_camera()
    if not os.path.exists(join(dirname(__file__), '../data')):
      os.makedirs(join(dirname(__file__), '../data'))
      
    self.detect()

  def detect(self):
    prev_frame = self.capture()
    self.frame_height = prev_frame.shape[0]
    while True:
      frame = self.capture()
      self.movement = is_movement(frame, prev_frame)
      if self.movement and not self.recording:
        self.out_start()
      if self.recording:
        self.out_write(frame)
      prev_frame = frame

  def start_camera(self):
    self.camera = cv2.VideoCapture(0)
    time.sleep(1)

  def stop_camera(self):
    if self.camera:
      self.camera.release()

  def capture(self):
    frame = self.camera.read()[1]
    return imutils.resize(frame, width = self.frame_width)

  def out_start(self):
    self.recording = True
    self.outname = '{}.{}'.format(str(time.time()), self.file_format)
    path = join(dirname(__file__), '../data/{}'.format(self.outname))
    self.output = cv2.VideoWriter(path, self.fourcc, self.fps, (self.frame_width, self.frame_height))
    self.movement_timeout = threading.Timer(5, self.out_end)
    self.movement_timeout.start()

  def out_write(self, frame):
    self.output.write(frame)
    if self.movement and self.movement_timeout is not None:
      self.movement_timeout.cancel()
      self.movement_timeout = None
    elif self.movement_timeout is None:
      self.movement_timeout = threading.Timer(10, self.out_end)
      self.movement_timeout.start()

  def out_end(self):
    self.recording = False
    self.output.release()
    self.emit('motion', self.outname)