# Read a Video from web cam using opencv
# Face Detection in video

import cv2

# Create a camera object  
cam =cv2.VideoCapture(0)

# model
model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

# Read image from camera object 
while True:
    success, img = cam.read()
    
    if not success:
        print("Reading Camera is not working !")
        break

    faces = model.detectMultiScale(img,1.3,5)

    for f in faces:
        x,y,w,h = f
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Image Window",img)
    # press 'q' to exit
    key = cv2.waitKey(10) 
    if key == ord('q'):
        break   # Pause here for 1ms before you read the next image

    # Release the camera and destroy all windows
cam.release()
cv2.destroyAllWindows()


