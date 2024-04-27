import cv2

#instalisasi detector wajah..!
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
camera = cv2.VideoCapture(0) # unutk mengakses camera utama

while True:
    # baca frame dari videoStreaming
    _,frame = camera.read()

    # konversi frame ke skala abu-abu
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # deteksi wajah dalam frame
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(50, 50))
    
    # gambar kotak setiap pada wajah yang terdeteksi
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x , y), (x + w,y + h), (0,255,0), 1)

    # tampilkan frame 
    cv2.imshow("pyFace", frame)

    # hentikan loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# tutup video streaming dan jendela video
camera.release()
cv2.destroyAllWindows()


