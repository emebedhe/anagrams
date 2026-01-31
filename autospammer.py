import pyautogui
import time
import pytesseract
from PIL import ImageGrab
from PIL import Image
from pynput import keyboard
import matplotlib.pyplot as plt
from find_anagram import find_anagrams
from eq_checker import check_with_similarity
from anagram_score import find_score
from asjdlk import find_subanagrams
# from autospammer2 import predict_letter, model, device
import os

training_dir = 'letters3'

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = False
delay = 1

count = triple = double = single = 0

stop = False
def on_press(key):
    global stop
    try:
        if hasattr(key, 'char') and key.char == '\\':
            print("STOPPING")
            stop = True
    except:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.daemon = True
listener.start()

plus1 = (56,880)
gp1 = (162,479)
wg = (57,734)
ana = (66  ,744)
send1 = (359,507)
send2 = (359,522)
start = (200,632)
game = (244,722)
msg = (247,856)

r = 132-25
d=156-132
l1 = 25
l2 = 156
l3 = 287
l4 = 418
l5 = 549
l6 = 680

top = 1523
bottom = 1600

list1 = [l1,l2,l3,l4,l5,l6]
pyautogui.click(70,428)

time.sleep(5)
while True:
    if stop:
        break

    time.sleep(delay)
    pyautogui.click(plus1)
    time.sleep(delay)
    pyautogui.click(gp1)
    time.sleep(delay)
    time.sleep(delay)
    pyautogui.click(wg)
    time.sleep(0.5)
    pyautogui.click(ana)
    time.sleep(delay)
    pyautogui.click(send2)
    time.sleep(delay)
    time.sleep(delay + 0.5)
    pyautogui.click(game)
    time.sleep(delay + 0.5)
    pyautogui.click(start)
    time.sleep(delay)
    # image = ImageGrab.grab(bbox=(l1, top, r6, bottom))
    image = ImageGrab.grab()
    letters = []


    # pyautogui.click(920,933)
    # # true_anagram = input("Enter the anagram shown: ").upper()
    # pyautogui.click(start)


    # analetters = list(true_anagram)
    for idx, lx in enumerate(list1):
        lx = lx
        crop = image.crop((lx,top,lx+r,bottom))

        # true_letter = analetters[idx].lower()

        # save_dir = os.path.join(training_dir, true_letter)
        # os.makedirs(save_dir, exist_ok=True)

        # timestamp = str(time.time()).replace(".", "")
        # name = f"{true_letter}_{idx+1}_{timestamp}"
        # save_path = os.path.join(save_dir, f"{name}.png")

        # crop.save(save_path)

        sim = check_with_similarity(crop)
        letter = sim[0]
        score = sim[1]
        print(f"Detected: {letter} with score {score}")
        letters.append(letter)



    print("Row letters:", letters)
    if letters.count(None) >= 1:
        print("unrecognized letters, skipping...")
        continue
    else: 
        anas = find_anagrams("".join(letters))
        subs = find_subanagrams("".join(letters))
    print("Anagram: ", anas)
    if anas != []:
        score = find_score(anas[0])
        print(f"Score: {score}")


    time.sleep(delay)
    pyautogui.hotkey('command', '1')
    time.sleep(delay)
    pyautogui.click(msg)
    time.sleep(delay)
    if score>100000:
        pyautogui.typewrite('triple purple')
        triple+=1
        if triple >= 2:
            break   
    elif score>75000:
        pyautogui.typewrite('double purple')
        double+=1
    elif score>65000:
        pyautogui.typewrite('single purple')
        single += 1
    elif anas != []:
        pyautogui.typewrite(anas[0].lower(), interval=0.1)
    pyautogui.press('enter')
    count += 1



print(str(count) + " rounds.")
print("Triples: " + str(triple))
print("Doubles: " + str(double))
print("Singles: " + str(single))