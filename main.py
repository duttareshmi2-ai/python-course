print("Please press 'q' or say 'exit'. To click an image press 's' or say 'click'.")

import cv2
import speech_recognition as sr
import sounddevice as sd

cap = cv2.VideoCapture(0)
cv2.namedWindow("Hello", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hello", 1280, 1030)

if not cap.isOpened():
    print("Can't find camera")
    exit()

recognizer = sr.Recognizer()

while True:
    # Record audio
    audio = sd.rec(int(3 * 16000), samplerate=16000, channels=1, dtype="int16")  # 3 seconds
    sd.wait()

    # Convert to AudioData for recognition
    audio_data = sr.AudioData(audio.tobytes(), 16000, 2)

    try:
        text = recognizer.recognize_google(audio_data).lower()
    except sr.UnknownValueError:
        text = ""
    except sr.RequestError:
        print("Speech recognition service error")
        text = ""

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        print("Error")
        break

    cv2.imshow("Hello", frame)

    if cv2.waitKey(1) & 0xFF == ord('s') or text == "click":
        cv2.imwrite("photo.jpg", frame)
        print("Photo saved as photo.jpg")

    if cv2.waitKey(1) & 0xFF == ord('q') or text == "exit":
        print("Received exit command.")
        break

cap.release()
cv2.destroyAllWindows()
