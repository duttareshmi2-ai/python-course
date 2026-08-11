import cv2
import sounddevice as sd 
import speech_recognition as sr 
cv2.namedWindow("Controlled Window",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Controlled Window",1780,1034)
cap=cv2.VideoCapture(0)
recognizer=sr.Recognizer()
if not cap.isOpened():
    print("Can't find system camera.")
    exit()
while True:
    audio=sd.rec(int(3*16000),samplerate=16000,channels=1,dtype="int16")
    sd.wait()
    audio_bytes=audio.tobytes()
    text=""
    try:
        text=recognizer.recognize_google(sr.AudioData(audio_bytes,16000,2))
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Can't connect to google server.")
    ret,frame=cap.read()
    if not ret:
        print("Error")
    cv2.imshow("Controlled Window",frame)
    if text=="flip" or cv2.waitKey(1) & 0xFF == ord("f"):
        cv2.flip(frame, 1)
    if text=="exit" or cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if text=="click" or cv2.waitKey(1) & 0xFF == ord("c"):
        cv2.imwrite("controlled.jpg", frame)
    if text=="gray" or cv2.waitKey(1) & 0xFF == ord("g"):
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cap.release()
cv2.destroyAllWindows()