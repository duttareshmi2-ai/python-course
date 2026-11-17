# STICKER MAKER: freeze the camera picture, click any object, and save it as a see-through sticker (PNG).
# Run it from this folder:  python sticker_maker.py      (the 4 SAM model files must sit next to this file)
# Lines marked (given) are done for you. Your job is TODO 1 to TODO 5. Do them in order, and run the program after each one.
# Keys in the camera window: SPACE = freeze / back to live   click = this   right-click = not this   m = part / whole
#                            s = save the sticker   q or Esc = quit
# Errors appear in this terminal, not in the camera window.

import os
import subprocess
import sys
import threading
import time

# (given) A: install the 3 packages if they are missing, then load SAM: two AI models that run on your laptop.
HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--disable-pip-version-check", "-r", os.path.join(HERE, "requirements.txt")])
import cv2                                          # opencv-python, numpy and onnxruntime: installed by the line above
import numpy as np
import onnxruntime

options = onnxruntime.SessionOptions()
options.enable_cpu_mem_arena = False                # give memory back after each run (SAM is big)
encoder = onnxruntime.InferenceSession(os.path.join(HERE, "vision_encoder_uint8.onnx"), options)              # SAM part 1: studies the photo
decoder = onnxruntime.InferenceSession(os.path.join(HERE, "prompt_encoder_mask_decoder_uint8.onnx"), options)  # SAM part 2: outlines
# (given) B: the colour averages SAM learned with (ImageNet), and the colours for drawing.
MEAN, STD = np.array([0.485, 0.456, 0.406], np.float32), np.array([0.229, 0.224, 0.225], np.float32)
FONT, WHITE, YELLOW, GREEN, RED = cv2.FONT_HERSHEY_SIMPLEX, (255, 255, 255), (0, 255, 255), (0, 220, 0), (0, 0, 255)


def study(photo):                                   

    x = (cv2.cvtColor(cv2.resize(photo, (1024, 1024)),cv2.COLOR_BGR2RGB)/255-MEAN)/STD
    features = encoder.run(None , {"pixel_values": x.astype(np.float32).transpose(2 , 0 , 1)[None]})                                       # (given) placeholder: SAM never finishes studying. Replace it.
    # (given) C: keep SAM's 3 notes about the photo (only if the photo is still frozen), named the way part 2 wants them.
    if state["photo"] is photo:                     # still the same frozen photo: keep SAM's notes, named for part 2
        state["features"] = {f"image_embeddings.{i}": feature for i, feature in enumerate(features)}


def ask_sam(features, size, clicks):                # fast: SAM's 3 guesses for these clicks (label 1 = this, 0 = not this)
    points = np.array([[x * 1024 / size[1], y * 1024 / size[0]] for x, y, label in clicks], np.float32)  # scale to 1024 x 1024
    labels = np.array([label for x, y, label in clicks], np.float64)
    feeds = {"input_points": points[None,None],"input_labels": labels[None,None], "input_boxes" : np.zeros((1,0,4), np.float32)}

    return decoder.run(None, {**feeds, **features})[1][0,0]   # (given) placeholder: 3 empty guesses. Replace it.


def pick(guesses, size, clicks, level):             # one guess, as big as the photo, only the pieces you clicked
    guess = sorted(guesses, key=lambda g: (g > 0).sum())[level]    # choose the level-th guess
    mask = (cv2.resize(guess , (size[1], size[0]))>0).astype(np.uint8)              # (given) placeholder: an empty outline. Replace it.
    # (given) D: remove specks, then keep only the pieces you clicked on.
    count, pieces = cv2.connectedComponents(cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)))   # specks removed
    keep = [pieces[y, x] for x, y, label in clicks if label == 1 and pieces[y, x]]
    return np.isin(pieces, keep) if keep else mask > 0


# (given) E: when the photo has been studied, a click or right-click becomes a prompt for SAM.
def on_mouse(event, x, y, flags, extra):
    if event in (cv2.EVENT_LBUTTONDOWN, cv2.EVENT_RBUTTONDOWN) and state["features"] is not None:
        state["clicks"].append((x, y, 1 if event == cv2.EVENT_LBUTTONDOWN else 0))
        state["guesses"] = ask_sam(state["features"], state["photo"].shape[:2], state["clicks"])
        print("SAM's 3 guesses cover", sorted(int((g > 0).sum()) for g in state["guesses"]), "of 65536 small pixels")
        state["mask"] = pick(state["guesses"], state["photo"].shape[:2], state["clicks"], state["level"])


# (given) F: what the program remembers, the camera, and the window that hears the mouse.
state = {"photo": None, "features": None, "clicks": [], "guesses": None, "level": 2, "mask": None}
message, message_until = "", 0
video = cv2.VideoCapture(0)
cv2.namedWindow("Sticker Maker")
cv2.setMouseCallback("Sticker Maker", on_mouse)
while True:                                         # (given) G: show the live camera or the frozen photo, with SAM's outline
    ok, frame = video.read()
    if not ok:
        break
    view = cv2.flip(frame, 1) if state["photo"] is None else state["photo"].copy()
    if state["mask"] is not None:                   # SAM's outline: yellow inside, white edge, a dot per click
        view[state["mask"]] = (view[state["mask"]] * 0.5 + np.array(YELLOW) * 0.5).astype(np.uint8)
        cv2.drawContours(view, cv2.findContours(state["mask"].astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], -1, WHITE, 2)
    for x, y, label in state["clicks"]:
        cv2.circle(view, (x, y), 7, GREEN if label == 1 else RED, -1)
    help_line = ("Point the camera at something, then SPACE to freeze it    q quit" if state["photo"] is None else
                 "SAM is studying your photo" + "." * (int(time.time() * 3) % 4) if state["features"] is None else
                 f"click: this   right-click: not this   m: {['a part', 'bigger', 'the whole thing'][state['level']]}   s: save sticker   SPACE: live")
    cv2.rectangle(view, (0, 0), (view.shape[1], 34), (30, 30, 30), -1)
    cv2.putText(view, message if time.time() < message_until else help_line, (10, 23), FONT, 0.5, WHITE, 1)
    cv2.imshow("Sticker Maker", view)
    # (given) H: the keys. Caps Lock does not matter.
    key = chr(cv2.waitKey(1) & 255).lower()
    if key in ("q", "\x1b") or cv2.getWindowProperty("Sticker Maker", cv2.WND_PROP_VISIBLE) == 0:
        break
    if key == " ":                                  # freeze (SAM starts studying) or back to live
        photo = None if state["photo"] is not None else cv2.flip(frame, 1)
        state.update(photo=photo, features=None, clicks=[], mask=None)
        if photo is not None:
            threading.Thread(target=study, args=(photo,)).start()   # Python waits for it before closing
    if key == "m" and state["clicks"]:              # SAM's next guess: a part, something bigger, the whole thing
        state["level"] = (state["level"] + 1) % 3
        state["mask"] = pick(state["guesses"], state["photo"].shape[:2], state["clicks"], state["level"])
    if key == "s" and state["mask"] is not None:
        x, y, w, h = cv2.boundingRect(state["mask"].astype(np.uint8))
        
        sticker = np.dstack([state["photo"],cv2.GaussianBlur(state["mask"].astype(np.uint8)*255, (3, 3), 0)])[y:y+h, x:x+w]                  # (given) placeholder: the whole photo, nothing see-through. Replace it.
        name = time.strftime("sticker_%H%M%S.png")
        cv2.imwrite(os.path.join(HERE, name), sticker)  # PNG keeps the see-through background
        message, message_until = f"Saved {name}: SAM cuts anything you point at, not only people", time.time() + 3
video.release()
cv2.destroyAllWindows()
