all_letters = []
vert_board = []
horiz_board = []
while True:
    board_input = input('Enter the horizontal letters: ')
    if board_input.lower() == 'exit' or len(board_input) == 0:
        break
    else: horiz_board.append(board_input.lower())

while True:
    board_input = input('Enter the vertical letters: ')
    if board_input.lower() == 'exit' or len(board_input) == 0:
        break
    else: vert_board.append(board_input.lower())
    
while True:
    board_input = input('Enter the solo letters: ')
    if board_input.lower() == 'exit' or len(board_input) == 0:
        break

    else: 
        for letter in board_input: 
            horiz_board.append(letter.lower())
            vert_board.append(letter.lower())

print(horiz_board)
print(vert_board)

with open('csw21.txt', 'r') as file:
    word_list = file.read().splitlines()

word_list = [word.lower() for word in word_list]

temp_vert_board = []
for item in vert_board:
    if len(item) == 2:
        temp_vert_board.append(item)
temp_vert_board_storage = temp_vert_board.copy()

horizpossiblewords = []
horizposs = []
horiz_with_double = []
for item in word_list:
    item = item.lower()
    temp_horiz_board = horiz_board.copy() 
    temp_vert_board = temp_vert_board_storage.copy()

    possibleword = True
    hasdouble = False
    doubles = []
    i = 0
    while i < len(item):
        letter = item[i]
        found = False

        if letter in temp_horiz_board:
            temp_horiz_board.remove(letter)
            found = True
            i += 1
        else:
            if i + 1 < len(item):
                pair = letter + item[i+1]
                if pair in temp_horiz_board:
                    temp_horiz_board.remove(pair)
                    found = True
                    i += 2
                else: 
                    for lk in temp_vert_board:
                        if letter in lk:

                            temp_vert_board.remove(lk)
                            found = True
                            hasdouble = True
                            doubles.append(lk)
                            doubles.append(letter)
                            i += 1

        if found == False:
            possibleword = False
            break
    if possibleword and len(item) <= 8: 
        horizpossiblewords.append(item)
        horizposs.append([item, [temp_horiz_board, temp_vert_board]])
        if hasdouble: horiz_with_double.append([item, doubles])

temp_horiz_board = []
for item in horiz_board:
    if len(item) == 2:
        temp_horiz_board.append(item)
temp_horiz_board_storage = temp_horiz_board.copy()
print(temp_horiz_board_storage)

vert_with_double = []
vertposs = []
vertpossiblewords = []
for item in word_list:
    item = item.lower()
    temp_vert_board = vert_board.copy()
    temp_horiz_board = temp_horiz_board_storage.copy()
    possibleword = True
    hasdouble = False
    doubles = []
    i = 0
    while i < len(item):
        letter = item[i]
        found = False

        if letter in temp_vert_board:
            temp_vert_board.remove(letter)
            found = True
            i += 1
        else:
            if i + 1 < len(item):
                pair = letter + item[i+1]
                if pair in temp_vert_board:
                    temp_vert_board.remove(pair)
                    found = True
                    i += 2
                else: 
                    for lk in temp_horiz_board:
                        if letter in lk:
                            temp_horiz_board.remove(lk)
                            found = True
                            hasdouble = True
                            doubles.append(lk)
                            doubles.append(letter)
                            i += 1
        if found == False:
            possibleword = False
            break
            
    if possibleword and len(item) <= 9: 
        vertpossiblewords.append(item)
        vertposs.append([item, [temp_horiz_board, temp_vert_board]])
        if hasdouble: vert_with_double.append([item, doubles])

horizpossiblewords.sort(key=len, reverse=True)
print(f'Possible words: {len(horizpossiblewords)}')
for i in range(10):
    print(horizpossiblewords[i])

vertpossiblewords.sort(key=len, reverse=True)
print(f'Possible words: {len(vertpossiblewords)}')
for i in range(10):
    print(vertpossiblewords[i])

# for item in horiz_with_double:
#     print(f'{item[0]}: {item[1]}')

print(str(int(len(horiz_with_double)) * 100/int(len(horizpossiblewords))) + '% of horiz')
print(str(int(len(vert_with_double)) * 100/int(len(vertpossiblewords))) + '% of vert')

# doubleswap = []
# for item in horiz_with_double:
#     if len(item[1]) == 2:
#         tempitem = item[0]
#         double = item[1][0]
#         if double.index(item[1][1]) == 1:
#             alt_letter = double[0]
#         else: alt_letter = double[1]
#         print(item[0].index(item[1][1]))
#         index = item[0].index(item[1][1])
#         print(tempitem[:index] + alt_letter + tempitem[index+1:])
#         if tempitem[:index] + alt_letter + tempitem[index+1:] in word_list:
#             print(f'Found alternative: {tempitem[:index] + alt_letter + tempitem[index+1:]}')
#             doubleswap.append([tempitem[:index] + alt_letter + tempitem[index+1:], item[1], item[0]])
#         else: 
#             print(f'{tempitem[:index] + alt_letter + tempitem[index+1:]} is not a word.')
        
# for item in vert_with_double:
#     if len(item[1]) == 2:
#         tempitem = item[0]
#         double = item[1][0]
#         if double.index(item[1][1]) == 1:
#             alt_letter = double[0]
#         else: alt_letter = double[1]
#         print(item[0].index(item[1][1]))
#         index = item[0].index(item[1][1])
#         print(tempitem[:index] + alt_letter + tempitem[index+1:])
#         if tempitem[:index] + alt_letter + tempitem[index+1:] in word_list:
#             print(f'Found alternative: {tempitem[:index] + alt_letter + tempitem[index+1:]}')
#             doubleswap.append([tempitem[:index] + alt_letter + tempitem[index+1:], item[1], item[0]])
#         else: 
#             print(f'{tempitem[:index] + alt_letter + tempitem[index+1:]} is not a word.')
        
print('hi')
        
# for item in doubleswap:
#     print(item[0], item[1])

# all_words = []
# for item in horizpossiblewords:
#     all_words.append(item)
# for item in vertpossiblewords:
#     all_words.append(item)

# all_words.sort(key=len, reverse=True)

# for item in all_words:
#     print(item)

# for word in all_words:
#     for letter in word:
#         if word[:word.index(letter)] + word[word.index(letter)+1:] in all_words:
#             print(f'{word[:word.index(letter)] + word[word.index(letter)+1:]} is a word coming from {word} by removing {letter}')

# combos = []
# addwords = []
# cc=0
# for item in vertposs:
#     for double in item[1]:
#         for item2 in double:
#             for letter2 in item2:
#                 for i in range(len(item[0]) + 1):
#                     cc+=1
#                     if cc % 1000 == 0: print(cc)
#                     if item[0][:i] + letter2 + item[0][i:] in word_list:

#                         addwords.append([item[0],item[0][:i] + letter2 + item[0][i:]])
#                         print(f'Found {item[0][:i] + letter2 + item[0][i:]} by adding {letter2} to {item[0]} at position {i} with double {item2}.')
#                 #else: print(f'{item[0][:i] + letter + item[0][i:]} is not a word.')
# cc=0
# for item in horizposs:
#     for double in item[1]:
#         for item2 in double:
#             for letter in item2:
#                 for i in range(len(item[0]) + 1):
#                     cc+=1
#                     if cc % 1000 == 0: print(cc)
#                     if item[0][:i] + letter + item[0][i:] in word_list:
#                         addwords.append([item[0],item[0][:i] + letter2 + item[0][i:]])
#                         print(f'Found {item[0][:i] + letter + item[0][i:]} by adding {letter} to {item[0]} at position {i} with double {item2}.')
#                 #else: print(f'{item[0][:i] + letter + item[0][i:]} is not a word.')

# for pair in addwords:
#     for letter in pair[1]:
#         word = pair[1]
#         if word[:word.index(letter)] + word[word.index(letter)+1:] in all_words and word[:word.index(letter)] + word[word.index(letter)+1:] != pair[0]:
#             print(f'{word[:word.index(letter)] + word[word.index(letter)+1:]} is a word coming from {pair[0]} by removing {letter} from {pair[1]}')
#             combos.append([pair[0], pair[1], word[:word.index(letter)] + word[word.index(letter)+1:]])

# combos.sort(key=lambda x: len(x[0]), reverse=True)
# for i in range(20):
#     if i < len(combos):
#         print(combos[i])