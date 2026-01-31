from PIL import ImageGrab
import easyocr
import time
import numpy as np
from remove_word import remove_word, add_word
from asjdlk import find_subanagrams
from threading import Timer
import os
def exit_program():
    os._exit(0)
timer = Timer(50,exit_program)
timer.start()
letter_coords = [38,103,170,235,305,367]
letter_y = 779

enter_coords = (201,580)
score_coords = (248,384,338,415)

import pyautogui


def check_word(word,letters):
    if type(letters) is str: letters = list(letters.strip())

    score = read_score()
    if len(word) == 3:
        inc = 100
    elif len(word) == 4:
        inc = 400
    elif len(word) == 5:
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
        time.sleep(0.2)
        pyautogui.click(x,y)
        
    pyautogui.click(enter_coords[0],enter_coords[1])
    time.sleep(1)
    new_score = read_score()
    if new_score - score == inc:
        remove_word('csw_6_unsure.txt',word)
        add_word('csw_6_yes.txt',word)
        return True, new_score
    else: 
        remove_word('csw_6_yes.txt',word)
        add_word('csw_6_no.txt',word)
        return False, score

reader = easyocr.Reader(['en'])

def read_score():
    image = ImageGrab.grab(bbox=score_coords)
    numpy_image = np.array(image)
    result = reader.readtext(numpy_image, detail=0, paragraph=False)

    if result:
        try:
            return int(result[0].replace(",", ""))
        except:
            return 0

    return 0

        
# board = input("-->")
# pyautogui.click(70,915)
# print(find_subanagrams(board))
# for i in find_subanagrams(board):
#     print(check_word(i,board))