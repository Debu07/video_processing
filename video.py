import cv2 #import openCV
video=cv2.VideoCapture(0) #here 0 is for web camera if you are using other camera you can use 1,2 etc as per device
count=0 # to count the number of frames generated
while True: #loop for video
    count+=1
    check , frame=video.read() # check and frame are boolean and numpy array data type
    print(check) #it will return true or false
    print(frame) # it will return n-d numpy array 
    cv2.imshow("capturing",frame) #window generated to show video procesing
    key=cv2.waitKey(1) # video generation after every 1 millisecond
    if key==ord('q'): # to exit the loop by pressing q->quit
        break 
print(count) #to print number of frames generated
video.release() #to release the video Stop the web cam
cv2.destroyAllWindows() #to exit the window generated in previous steps
