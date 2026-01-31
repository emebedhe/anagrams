with open ("verified_6_letter_scores.txt","r") as f:
    lines2 = f.readlines()
lines = []
for line in lines2:
    line = line.strip().split("\t")
    a = line.pop()
    b = line.pop()
    c = line.pop()
    d = line.pop()
    a=a.replace(",","")
    d = d.upper()
    line.append(d)
    line.append(int(c))
    line.append(int(b))
    line.append(int(a))
    lines.append(line)

with open("csw216_only56.txt","r") as f:
    words2 = f.readlines()

words = []
for w in words2:
    words.append(w.strip())

# print(lines)


from collections import Counter

def find_subanagrams(word, words):
    word_count = Counter(word.upper())
    result = []

    for w in words:
        w_count = Counter(w.upper())
        if not (w_count - word_count):
            result.append(w)

    return result

b = []
with open("vbrubwords.txt","r") as f:
    jkl = f.readlines()
for w in jkl:
    b.append(w.strip().upper())

badwords = set()

for word_pair in lines:
    a = (find_subanagrams(word_pair[0],words))
    if (len(a)) == word_pair[1] + word_pair[2]:
        print(word_pair[0])
    else:
        diff = list(set(a)-set(b))
        if len(diff) == 0:
            print(len(a))
            print(word_pair[1])
            print(word_pair[2])
        print(word_pair[0] + " , " + ", ".join(diff))
        for d in diff:
            badwords.add(d)

print(badwords)

# unverified = []
# with open ("verifiednot56.txt","r") as f:
#     unverified2 = f.readlines()

# for w in unverified2:
#     unverified.append(w.strip())

# for word in unverified:
#     g = True
#     for char in word:
#         h = False
#         combo = word.replace(char,"",1)
#         for w in b:
#             if sorted(w.lower()) == sorted(combo.lower()):
#                 # print(combo)
#                 h = True
#         if not h:
#             g = False
#             print(combo)
#     if g:
#         print(word)
    