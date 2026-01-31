import pyautogui
import time

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
from PIL import ImageGrab
import easyocr
import numpy as np
from remove_word import remove_word, add_word
from threading import Timer
import os


import warnings
warnings.filterwarnings(
    "ignore",
    message=".*pin_memory.*MPS.*"
)


go = False
def cont():
    global go
    print("timeout")
    go = True

letter_coords = [38,103,170,235,305,367]
letter_y = 779

enter_coords = (201,580)
score_coords = (245,384,375,415)

import pyautogui

def check_all_words(wordlist,letters):
    if type(letters) is str: letters = list(letters.strip())
    score = 0
    for word in wordlist:
        if go:
            break
        letters = [l.upper() for l in letters]
        click_sequences = []
        letter_coord_pairs = {}
        for idx, letter in enumerate(letters):
        # Map each index position to its correct coordinate
            letter_coord_pairs.setdefault(letter, []).append(letter_coords[idx])

        temp = {k: v.copy() for k, v in letter_coord_pairs.items()}
        seq = [(temp[letter].pop(0), letter_y) for letter in word]
        click_sequences.append(seq)
        for x,y in seq:
            time.sleep(0.05)
            pyautogui.click(x,y)
            
        pyautogui.click(enter_coords[0],enter_coords[1])
    time.sleep(1)
    return read_score()


def check_word(word,letters,currentscore):
    if type(letters) is str: letters = list(letters.strip())
    score = currentscore
    if len(word) == 5:
        inc = 1200
    elif len(word) == 6:
        inc = 2000
    word = word.upper()
    letters = [l.upper() for l in letters]
    click_sequences = []
    letter_coord_pairs = {}
    for idx, letter in enumerate(letters):
    # Map each index position to its correct coordinate
        letter_coord_pairs.setdefault(letter, []).append(letter_coords[idx])

    temp = {k: v.copy() for k, v in letter_coord_pairs.items()}
    seq = [(temp[letter].pop(0), letter_y) for letter in word]
    click_sequences.append(seq)
    for x,y in seq:
        time.sleep(0.05)
        pyautogui.click(x,y)
        
    pyautogui.click(enter_coords[0],enter_coords[1])
    new_score = read_score()
    return True, new_score

reader = easyocr.Reader(['en'], gpu=False)

def read_score():
    image = ImageGrab.grab(bbox=score_coords)
    numpy_image = np.array(image)
    #image.show()
    result = reader.readtext(numpy_image, detail=0, paragraph=False)

    if result:
        try:
            return int(result[0].replace(",", ""))
        except:
            return 0

    return 0
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
    s=0

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
    timer = Timer(50,cont)
    timer.start()
    go = False
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
        subs = [s for s in subs if len(s)>=5]
    print("Anagram: ", anas)
    if anas != []:
        score = find_score(anas[0])
        print(f"Score: {score}")

    expected_score = 0
    for w in subs:
        if len(w) == 5:
            expected_score += 1200
        elif len(w) == 6:
            expected_score += 2000

    print(go, subs)
    subs.sort(key=len,reverse=True)
    s = check_all_words(subs, letters)


    

    time.sleep(delay)
    pyautogui.hotkey('command', '1')
    time.sleep(delay)
    pyautogui.click(msg)
    time.sleep(delay)
    if score>100000:
        pyautogui.typewrite('triple purple, 5-6 '+ str(s) + "csw score " + str(expected_score))
        triple+=1
        if triple >= 2:
            break   
    elif score>75000:
        pyautogui.typewrite('double purple, 5-6 '+ str(s) + "csw score " + str(expected_score))
        double+=1
    elif score>65000:
        pyautogui.typewrite('single purple, 5-6 '+ str(s) + "csw score " + str(expected_score))
        single += 1
    elif anas != []:
        pyautogui.typewrite(anas[0].lower() + ' 5-6 '+ str(s) + " csw score " + str(expected_score))
    pyautogui.press('enter')
    count += 1
    timer.cancel()




print(str(count) + " rounds.")
print("Triples: " + str(triple))
print("Doubles: " + str(double))
print("Singles: " + str(single))