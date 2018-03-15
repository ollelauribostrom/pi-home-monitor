import cv2

def smooth(frame):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  return cv2.GaussianBlur(gray, (21, 21), 0)

def is_movement(frame_a, frame_b):
  delta = cv2.absdiff(smooth(frame_b), smooth(frame_a))
  threshold = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
  threshold = cv2.dilate(threshold, None, iterations = 2)
  contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
  for countour in contours:
    if cv2.contourArea(countour) > 100:
      return True
  return False