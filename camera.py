# Read a Video from web cam using opencv
# Face Detection in video
# Click 20 pictures of the person who comes in the front of camera and save them as numpy 


import cv2

# Create a camera object  
cam =cv2.VideoCapture(0)

# Ask the name 
name = input("Enter the name of the person : ")
dataset_path = "./dataset/" 

# model
model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

# Read image from camera object 
while True:
    success, img = cam.read()
    
    if not success:
        print("Reading Camera is not working !")
        break

#Store the image in gray scale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = model.detectMultiScale(grayImg,1.3,5)

    if len(faces) > 0:
       # sorting the face with largest bounding box 
      faces = sorted(faces, key=lambda f: f[2]*f[3])

       # pick the largest face
      face = faces[-1]

    
      x,y,w,h = face
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

      # crop  and save the largest face

      cropped_face = img[y:y+h, x:x+w]
     
      cv2.imshow("Cropped Face",cropped_face)


    cv2.imshow("Image Window",img)
    # press 'q' to exit
    key = cv2.waitKey(10) 
    if key == ord('q'):
        break   # Pause here for 1ms before you read the next image

    # Release the camera and destroy all windows
cam.release()
cv2.destroyAllWindows()


