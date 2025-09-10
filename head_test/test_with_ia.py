import cv2
net = cv2.dnn.readNetFromCaffe('deploy.prototxt,'mobilenet_iter_73000.caffemodel')
                               
img=cv2.imread('images/robot.jpg')
(h,w)=img.shape[:2]

blob=cv2.dnn.blobFromImage(cv2.resize(img,(300,300)),0.00784,(300,300),127.5)
net.setInput(blob)
detections=net.forward()

count_people=0

for i in range(detections.shape[2]):
    confidence=detenctions[0,0,i,2]
    if confidence > 0.2:
        idx = int(detections[0,0,i,2])
        if confidence > 0.2 and idx == 15:
            count_people+=1
print(f"Numero di persone rilevate: {count_people}")