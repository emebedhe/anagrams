with open('csw21.txt', 'r') as file:
    word_list = file.read().splitlines()


def dup_check(word):
    twocount = 0
    for char in word:
        if word.count(char) >= 3:
            return True
        elif word.count(char) == 2:
            twocount += 1
    if twocount > 2:
        return True
    return False


with open('csw217.txt','w') as file:
    for word in word_list:
        if len(word) <= 7 and len(word) >= 3:
            if not dup_check(word):
                file.write(word + '\n')

