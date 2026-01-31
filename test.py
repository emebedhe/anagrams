with open("six_letter_word_scores.txt","r") as f:
    lines = f.readlines()

with open('csw216.txt', 'r') as file:
    word_list6 = file.read().splitlines()
words = []
for line in lines:
    word, score = line.strip().split(": ")
    words.append((word, int(score)))

final = []
def fa(word):
    for w in word_list6:
        if len(w) == 6 and sorted(w.upper()) == sorted(word.upper()):
            return w
c = 0
for word in words:
    c += 1
    print(c)
    final.append([fa(word[0]), word[1]])

print(final)
with open("final_six_letter_word_scores.txt","a") as f:
    for word, score in final:
        f.write(f"{word}: {score}\n")