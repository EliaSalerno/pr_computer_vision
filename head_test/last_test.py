import cv2

# Carica il classificatore Haar Cascade pre-addestrato per i volti
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carica un'immagine (modifica il percorso con la tua immagine)
img = cv2.imread('images/folla.jpg')

# Converte l'immagine in scala di grigi
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Rileva i volti nell'immagine
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Disegna un rettangolo attorno ai volti rilevati
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostra il risultato
cv2.imshow('Volti rilevati', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
