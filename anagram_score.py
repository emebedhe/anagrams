with open('anagram_pairs_6.txt', 'r') as file:
    word_list = file.read().splitlines()

def find_score(word):
    for word_pair in word_list:
        pair = word_pair.split(',')
        if pair[0][:6] == word:
            return int(pair[0].split(': ')[1])
        

# print(find_score("ABLEST"))