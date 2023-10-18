import cv2
print('Imported!')
# img = cv2.imread('resources/R.jpeg')
# cv2.imshow('Output',img)
# cv2.waitKey(0)

# cap=cv2.VideoCapture('resources/d.mp4')
#
# while True:
#     sucess, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap=cv2.VideoCapture(0)
cap.set(3,640)#Comprimento
cap.set(4,480)#Altura
cap.set(10,100)#Brilho
while True:
    sucess, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break