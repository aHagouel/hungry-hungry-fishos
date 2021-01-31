#!/usr/bin/python
from time import sleep
from lobe import ImageModel
import subprocess
import tflite_runtime.interpreter

# Learning mostly from https://blog.paperspace.com/tensorflow-lite-raspberry-pi/
# and https://github.com/microsoft/TrashClassifier.
# Took some code from my old project: https://github.com/aHagouel/MauiBot4000/blob/master/src/bot.py
# SHoutout Lobe team for helping debug my execution environment.

model_folder = "/home/pi/Development/hungry-hungry-fishos/utilities/model/"

# Load Lobe.ai TF model. Requires TF Lite & Lobe installation. Please check out readme for more info.
model = ImageModel.load(model_folder)

def take_picture(file_path = '/home/pi/Development/hungry-hungry-fishos/current_state/last_picture'):
    command = "fswebcam -S 2 -r 980x540 --no-banner " + file_path + '.jpg'
    process = subprocess.call(command.split(), stdout=subprocess.PIPE)
    return file_path + '.jpg'

while True:
    photo_path = take_picture()
    # Run photo through Lobe TF model
    result = model.predict_from_file(photo_path)
    print(result)
    if(result=="Hungry"):
        #TODO: Email or tweet it!
        print("Where is my human?")
    sleep(10)
