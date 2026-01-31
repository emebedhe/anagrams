with open('csw_6_unsure.txt', 'r') as file:
    word_list = file.read().splitlines()

def is_subanagram(word, anagram):
    temp_letters = list(anagram)
    for char in word:
        if char in temp_letters:
            temp_letters.remove(char)
        else:
            return False
    return True

def find_subanagrams(word):
    word = word.upper()
    subs = []
    for word2 in word_list:
        if is_subanagram(word2, word):
            subs.append(word2)
    return subs

# print(find_subanagrams("LISTEN"))