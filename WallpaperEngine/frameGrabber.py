import cv2
vidcap = cv2.VideoCapture(r'C:\Users\thetr\Pictures\Camera Roll\original.mp4')
success,image = vidcap.read()
print(success)
count = 0
while success:
  cv2.imwrite(r"C:\Users\thetr\Documents\pictSave\frame%d.png" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1