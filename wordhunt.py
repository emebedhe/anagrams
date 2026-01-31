import math
with open('csw21.txt', 'r') as file:
    word_list = file.read().splitlines()

while True:
    board_input = input('Enter the board letters: ')
    if len(board_input) == 16 or len(board_input) == 25:
        break
board_input = board_input.lower()
board_letters = list(board_input)
word_list2 = []

for item in word_list:  
    item = item.lower()
    word_list2.append(item)
word_list = word_list2
filtered_word_list = []
for word in word_list:
    if len(word) >= 3:
        filtered_word_list.append(word)

print(f'Filtered word list contains {len(filtered_word_list)} words')

filtered_word_list2 = []
for word in filtered_word_list:
    for letter in word:
        if letter.lower() not in board_letters:
            break
    else:
        filtered_word_list2.append(word)

print(f'Filtered word list 2 contains {len(filtered_word_list2)} words')
possible_words = []
start_end_list = []
def check_word(board_letters, word):
    def search(path, idx):
        if idx == len(word):
            return path  
        last = path[-1]
        for i, letter in enumerate(board_letters):
            coord = [i % 4 + 1, math.floor(i / 4) + 1]
            if letter == word[idx] and coord not in path:
                if abs(coord[0] - last[0]) <= 1 and abs(coord[1] - last[1]) <= 1:
                    result = search(path + [coord], idx + 1)
                    if result:
                        return result
        return None

    for i, letter in enumerate(board_letters):
        if letter == word[0]:
            start = [i % 4 + 1, math.floor(i / 4) + 1]
            result = search([start], 1)
            if result:
                # Print start and end coordinates
                # print(f"{word}: start {result[0]}, end {result[-1]}")
                start_end_list.append((word, result[0], result[-1]))
                return True
    return False

possible_words = []

for word in filtered_word_list2:
    if check_word(board_letters, word):
        possible_words.append(word)

possible_words.sort(key=len)

start_end_list.sort(key=lambda x: (x[1][0], x[1][1]))
for word in possible_words:
    print(word)