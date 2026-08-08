import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

Cap = cv2.VideoCapture(0)
if not Cap.isOpened():
    print("Error, Could not open webcam.")
    exit()

while True:
    ret, frames = Cap.read()
    if not ret:
        print("Error, failed to capture image.")
        break

    grayscale = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    clean_grayscale = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x, y, w, h) in clean_grayscale:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.putText(frames, f'people: {len(clean_grayscale)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Face Tracking and Counting", frames)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

Cap.release()
cv2.destroyAllWindows()
