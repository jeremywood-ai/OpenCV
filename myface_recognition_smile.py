# face Recognition practice / Adding Smile Dectection (parameter tuning)

# importing libraries
import cv2  # only need cv2 for OpenCV

# loading the cascades (XML files need for call)
# that are series of filters to be applied to an image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Part 2 - Defining the functions
# Defining the detection functions
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # values good for webcams
    for (x, y, w, h) in faces: # my tuple
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)# faces
        roi_gray = gray[y:y+h, x:x+w] # zone of interest - gray
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22) # good values for eye detection to up 22
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22) # improved scale and neighbors
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
    return frame

# Using the webcam for facial recognition
video_capture = cv2.VideoCapture(0) # 0 internal webcam, 1 external
while True: # loop until capture is stopped (break)
    _, frame = video_capture.read() # want only the 2nd option of the read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # find the grayscale
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas) #superimpose
    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to stop
        break

video_capture.release() # release camera
cv2.destroyAllWindows() # stop all cv2