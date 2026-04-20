import cv2
# Create a camera object  
cam =cv2.VideoCapture(0)

# Read image from camera object 
while True:
    success, img = cam.read()

    if not success:
        print("Reading Camera is not working !")
        break
    cv2.imshow("Image Window",img)
    # press 'q' to exit
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        break   # Pause here for 1ms before you read the next image
cam.release()
cv2.destroyAllWindows
