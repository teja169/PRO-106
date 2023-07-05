import cv2 

img = cv2.imread("boy.jpg")

gray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

size = face_cascade.detectMultiScale( gray , 1.1 , 5 )
print(size)

for ( x, y , w , h) in size :
    cv2.rectangle(img , (x,y) , (x+w , y+h) , ( 78 , 222 , 34 ) , 5 )
    roi = img[y:y+h , x:x+w ]
    cv2.imwrite("face.jpg" , roi)

    
cv2.imshow("img" , img)
cv2.waitKey(0)
