file = open("words_alpha.txt", "r")
data = file.readlines()
file.close()
Vletters = []
for i in range(len(data)):
    if(len(data[i]) == 6):
        Vletters.append(data[i])

nfile = open("5_letter_words.txt", "w")
nfile.writelines(Vletters)
nfile.close()
