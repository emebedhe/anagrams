
import time
from PIL import ImageGrab, Image
from pynput import keyboard
import os
from autospammer2 import predict_letter, model, device




# Example usage:

training_dir = 'letters3'

r = 132-25
d=156-132
l1 = 25
l2 = 156
l3 = 287
l4 = 418
l5 = 549
l6 = 680


list1 = [l1,l2,l3,l4,l5,l6]



top = 1523
bottom = 1600

while True:    

    true_anagram = input("Enter the anagram shown: ").upper()

    analetters = list(true_anagram)

    image = ImageGrab.grab()


    for idx, lx in enumerate(list1):
        lx = lx
        crop = image.crop((lx,top,lx+r,bottom))
        # crop = crop.resize((crop.width * 3, crop.height * 3), Image.NEAREST)
        # gray = crop.convert("L")

        true_letter = analetters[idx].lower()

        save_dir = os.path.join(training_dir, true_letter)
        os.makedirs(save_dir, exist_ok=True)

        timestamp = str(time.time()).replace(".", "")
        name = f"{true_letter}_{idx+1}_{timestamp}"
        save_path = os.path.join(save_dir, f"{name}.png")

        crop.save(save_path)
