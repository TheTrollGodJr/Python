# Necessary imports
import cv2
import numpy as np
#from google.colab.patches import cv2_imshow

# Creating face_cascade and eye_cascade objects
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
imgOverlap = 5

# Loading the image
img = cv2.imread('C:/Users/thetr/Pictures/Pictures/133.png')

# Converting the image into grayscale
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Creating variable faces
faces= face_cascade.detectMultiScale (gray, 1.1, 4)
# Defining and drawing the rectangle around the face
for(x , y,  w,  h) in faces:
  cv2.rectangle(img, (x,y) ,(x+w, y+h), (0,255,0), 3)

# Creating two regions of interest
roi_gray=gray[y:(y+h), x:(x+w)]
roi_color=img[y:(y+h), x:(x+w)]

# Creating variable eyes
eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, imgOverlap)
while True:
   #print(len(eyes), imgOverlap)
   if imgOverlap < 0:
      print("No Face Found")
      exit(1)
   elif len(eyes) > 2:
      imgOverlap += 1
      eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, imgOverlap)
   elif len(eyes) < 2:
      imgOverlap -= 1
      eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, imgOverlap)
   elif imgOverlap > 500:
      break
   else:
      break
imgOverlap = 5

index=0
# Creating for loop in order to divide one eye from another
for (ex , ey,  ew,  eh) in eyes:
  if index == 0:
    eye_1 = (ex, ey, ew, eh)
  elif index == 1:
    eye_2 = (ex, ey, ew, eh)
# Drawing rectangles around the eyes
  cv2.rectangle(roi_color, (ex,ey) ,(ex+ew, ey+eh), (0,0,255), 3)
  index = index + 1

if eye_1[0] < eye_2[0]:
   left_eye = eye_1
   right_eye = eye_2
else:
   left_eye = eye_2
   right_eye = eye_1

# Calculating coordinates of a central points of the rectangles
left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
left_eye_x = left_eye_center[0] 
left_eye_y = left_eye_center[1]
 
right_eye_center = (int(right_eye[0] + (right_eye[2]/2)), int(right_eye[1] + (right_eye[3]/2)))
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]
 
cv2.circle(roi_color, left_eye_center, 5, (255, 0, 0) , -1)
cv2.circle(roi_color, right_eye_center, 5, (255, 0, 0) , -1)
cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),3)

if left_eye_y > right_eye_y:
   A = (right_eye_x, left_eye_y)
   # Integer -1 indicates that the image will rotate in the clockwise direction
   direction = -1 
else:
   A = (left_eye_x, right_eye_y)
  # Integer 1 indicates that image will rotate in the counter clockwise  
  # direction
   direction = 1 

cv2.circle(roi_color, A, 5, (255, 0, 0) , -1)
 
cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),3)
cv2.line(roi_color,left_eye_center, A,(0,200,200),3)
cv2.line(roi_color,right_eye_center, A,(0,200,200),3)
#cv2.imwrite("img.jpg", img)

delta_x = right_eye_x - left_eye_x
delta_y = right_eye_y - left_eye_y
angle=np.arctan(delta_y/delta_x)
angle = (angle * 180) / np.pi

# Width and height of the image
h, w = img.shape[:2]
# Calculating a center point of the image
# Integer division "//"" ensures that we receive whole numbers
center = (w // 2, h // 2)
# Defining a matrix M and calling
# cv2.getRotationMatrix2D method
M = cv2.getRotationMatrix2D(center, (angle), 1.0)
# Applying the rotation to our image using the
# cv2.warpAffine method
rotated = cv2.warpAffine(img, M, (w, h))

#--------------------------------------------------------------------------------------------------------

# calculate distance between the eyes in the first image
#dist_1 = np.sqrt((delta_x * delta_x) + (delta_y * delta_y))
dist_1 = 455.0890022841686
dist_2 = np.sqrt((delta_x * delta_x) + (delta_y * delta_y))
ratio = dist_1 / dist_2

# Defining the width and height
h, w, c = img.shape
# Defining aspect ratio of a resized image
dim = (int(w * ratio), int(h * ratio))
# We have obtained a new image that we call resized3
resized = cv2.resize(rotated, dim)
cv2.imwrite("imgA.png", resized)
