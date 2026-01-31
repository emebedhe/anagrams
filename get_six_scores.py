with open("csw216_only56.txt","r") as f:
    lines = f.readlines()

def is_subanagram(word, anagram):
    temp_letters = list(anagram)
    for char in word:
        if char in temp_letters:
            temp_letters.remove(char)
        else:
            return False
    return True
seen = set()
for word in lines:
    if (seen.__contains__(''.join(sorted(word.strip())))):
        continue
    word = ''.join(sorted(word.strip()))
    seen.add(word)

scores = []
c = 0
for line in seen:
    c += 1
    if c%100 == 0: print(c)
    word_score = 0
    if len(line.strip()) == 6:
        for word in lines:
        
            if is_subanagram(word.strip(), line.strip()):
                if len(word.strip()) == 5:
                    word_score += 1200
                elif len(word.strip()) == 6:
                    word_score += 2000
        scores.append((line.strip(), word_score))
    
scores.sort(key=lambda x: x[1], reverse=True)
for word, score in scores:
    print(f"{word}: {score}")
with open("six_letter_word_scores.txt","w") as f:
    for word, score in scores:
        f.write(f"{word}: {score}\n")