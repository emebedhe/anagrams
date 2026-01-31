def remove_word(file,word):
    with open(file,"r") as f:
        lines = f.readlines()
    with open(file,"w") as f:
        for line in lines:
            if line.strip("\n") != word:
                f.write(line)

def add_word(file,word):
    with open(file,"a") as f:
        f.write(word+"\n")