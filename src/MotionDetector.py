import numpy as np
import cv2
import imutils
import time
from os.path import join, dirname
from threading import Timer

class MotionDetector:

  def __init__(self, frame_width = 500):
    self.observers = []
    self.camera = None
    self.buffer = []
    self.movement = False
    self.timer = None
    self.frame_width = frame_width
    
  def start(self):
    if self.camera is None:
      self.camera = cv2.VideoCapture(0)
      time.sleep(1)

    prev_frame = self.capture()
    self.frame_height = prev_frame.shape[0]

    while True:
      frame = self.diff(prev_frame)
      if self.movement:
        self.buffer.append(frame)
      elif self.buffer:
        self.save()
      prev_frame = frame

  def stop(self):
    if self.camera:
      self.camera.release()

  def capture(self):
    frame = self.camera.read()[1]
    return imutils.resize(frame, width = self.frame_width)

  def smooth(self, frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.GaussianBlur(gray, (21, 21), 0)

  def timeout(self):
    self.movement = False

  def diff(self, prev_frame):
    frame = self.capture()
    delta = cv2.absdiff(self.smooth(prev_frame), self.smooth(frame))
    threshold = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations = 2)
    contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    for countour in contours:
      if cv2.contourArea(countour) > 50:
        self.movement = True
        if self.timer:
          self.timer.cancel()
        self.timer = Timer(5, self.timeout)
        self.timer.start()
    return frame

  def save(self):
    filename = '../movements/{}.mp4'.format(str(time.time()))
    path = join(dirname(__file__), filename)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    output = cv2.VideoWriter(path, fourcc, 20.0, (500, self.frame_height))
    for frame in self.buffer:
      output.write(frame)
    output.release()
    self.buffer = []
    self.notify(filename)

  def subscribe(self, observer):
    self.observers.append(observer)

  def notify(self, path):
    for observer in self.observers:
      observer(path)