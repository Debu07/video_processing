import cv2
video=cv2.VideoCapture(0)
count=0
while True:
    count+=1
    check , frame=video.read()
    print(check)
    print(frame)
    cv2.imshow("capturing",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(count)
video.release()
cv2.destroyAllWindows()
