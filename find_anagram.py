with open('csw216.txt', 'r') as file:
    word_list6 = file.read().splitlines()

with open('csw217.txt', 'r') as file:
    word_list7 = file.read().splitlines()


def find_anagrams(word):
    if len(word) == 6:
        return [w for w in word_list6 if sorted(w.upper()) == sorted(word.upper())]
    elif len(word) == 7:
        return [w for w in word_list7 if sorted(w.upper()) == sorted(word.upper())]
