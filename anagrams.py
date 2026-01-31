import ast


def find_anagrams(word, word_list):
    sorted_word = sorted(word)
    return [w for w in word_list if w != word and sorted(w) == sorted_word]

with open('csw21.txt', 'r') as file:
    word_list = file.read().splitlines()

print(len(word_list))
i = 0
for num11 in range(1,16):
    
    filtered_word_list = []
    possible_anagrams = []
    true_anagrams = []
    subs = []
    pairs = []
    for word in word_list:
        i += 1
        if i % 10000 == 0:
            print(f'Processed {i} words')
        if len(word) <= num11 and len(word) >= 3:
            filtered_word_list.append(word)
        if len(word) == num11:
            possible_anagrams.append(word)

    print(len(possible_anagrams))
    ana = False
    for word in possible_anagrams:
        doublecount = 0
        for char in word:
            if word.count(char) >= 3:
                ana = False
                break
            if word.count(char) == 2:
                doublecount += 1
            if doublecount >= 4:
                ana = False
                break
            else:
                ana = True
        if ana:
            true_anagrams.append(word)
    i=0
    print(len(true_anagrams))
    for anagram in true_anagrams:
        i += 1
        if i % 10 == 0:
            print(f'Processed {i} anagrams')
        subanagrams = []
        anagram_letters = list(anagram)
        for word in filtered_word_list:
            temp_letters = anagram_letters.copy()
            is_subanagram = True
            for char in word:
                if char in temp_letters:
                    temp_letters.remove(char)
                else:
                    is_subanagram = False
                    break
            if is_subanagram:
                subanagrams.append(word)
        subanagrams.sort(key=len)
        subs.append(subanagrams)
        pairs.append([[anagram], subanagrams])

    pairs.sort(key=lambda x: len(x[1]))
    filepath = "anagram_pairs_" + str(num11) + ".txt"
    with open(filepath, 'w') as f:
        for pair in pairs:
            f.write(f"{pair}\n")




    # Read anagram_pairs.txt and load it back into a list

    restored_pairs = []
    with open(filepath, 'r') as f:
        for line in f:
            restored_pairs.append(ast.literal_eval(line.strip()))



    lowest_scores = []
    highest_scores = []
    scores = []
    possible_anagrams = []
    unique_anagrams = []
    seen = set()
    for pair in restored_pairs:
        anagram = pair[0][0]
        # if 'S' in anagram:
        #     continue
        possible_anagrams.append(anagram)

        sorted_anagram = ''.join(sorted(anagram))
        if sorted_anagram in seen:
            continue
        seen.add(sorted_anagram)
        unique_anagrams.append(anagram)
        score = 0
        for word in pair[1]:
            
            if len(word) == 3: score += 100
            elif len(word) == 4: score += 400
            elif len(word) == 5: score += 1200
            elif len(word) == 6: score += 2000
            elif len(word) == 7: score += 3000
            elif len(word) == 8: score += 4000
            elif len(word) == 9: score += 5000
            elif len(word) == 10: score += 6000
            elif len(word) == 11: score += 7000
            elif len(word) == 12: score += 8000
            elif len(word) == 13: score += 9000
            elif len(word) == 14: score += 10000
            elif len(word) == 15: score += 11000
        scores.append((anagram, score, len(pair[1])))

    # Sort scores by score value
    scores.sort(key=lambda x: x[1])

    # Add 10 lowest scores
    lowest_scores = scores[:200]

    # Add 10 highest scores
    highest_scores = scores[-20:]

    i = 0
    for score in lowest_scores:
        i += 1
        print(str(len(unique_anagrams)-i) + ". " + f"{score[0]}: {score[1]}")
    print("...")
    i = 0
    for score in highest_scores:
        i += 1
        print(str(len(highest_scores)+1-i) + ". " + f"{score[0]}: {score[1]}")
        print("Total words: " + str(score[2]))
        # print(find_anagrams(score[0], possible_anagrams))

    filpath = "anagram_scores_" + str(num11) + ".txt"
    with open(filepath, 'w') as f:
        for score in scores:
            f.write(f"{score[0]}: {score[1]}, {score[2]}\n")