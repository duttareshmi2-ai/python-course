# -*- coding: utf-8 -*-
from deep_translator import GoogleTranslator
text=[]
while True:
    try:
        text=input("Please enter your text : ")
        translated=GoogleTranslator(source="en",target="bn").translate(text)
        print(translated)
    except Exception:
        print("Error")