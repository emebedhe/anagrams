import pyautogui,time
from pynput import keyboard
delay=0.025

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


pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = False


with open('csw216.txt', 'r') as file:
    word_list = file.read().splitlines()

letter_coords = [38,103,170,235,305,367]
letter_y = 779

enter_coords = (201,580)


def is_subanagram(word, anagram):
    temp_letters = list(anagram)
    for char in word:
        if char in temp_letters:
            temp_letters.remove(char)
        else:
            return False
    return True

def find_subanagrams(word):
    subs = []
    for word2 in word_list:
        if is_subanagram(word2, word):
            subs.append(word2)
    return subs



def sort_by_length(wordlist):
    wordlist.sort(key=len, reverse = True)
    return wordlist
    
i = input("Enter a word, in order: ").upper()
letterlist = list(i)
subs2 = find_subanagrams(i)
subs = []
for w in subs2:
    if len(w) >= 5:
        subs.append(w)

letter_coord_pairs = {}

for idx, letter in enumerate(letterlist):
    # Map each index position to its correct coordinate
    letter_coord_pairs.setdefault(letter, []).append(letter_coords[idx])


print(letter_coord_pairs)

words = sort_by_length(subs)
count = 0
print(words)
print(len(words))
pyautogui.click(194,632)
pyautogui.click(194,632)


# Precompute click sequences
click_sequences = []
for word in words:
    temp = {k: v.copy() for k, v in letter_coord_pairs.items()}
    seq = [(temp[letter].pop(0), letter_y) for letter in word]
    click_sequences.append(seq)

for seq in click_sequences:
    if stop:
        break

    for x, y in seq:
        pyautogui.click(x, y)
        # time.sleep(delay)

    pyautogui.click(enter_coords)



