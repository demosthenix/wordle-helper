import random
import sys
guess_words = dict()

with open("/Users/Demosthenix/JOJO/Wordle-Solver/w.txt", 'r') as f:
    words_line = [line.rstrip() for line in f]

word_dict = dict()
for line in reversed(words_line):
    l = line.split()
    word_dict[l[0]] = int(l[1])

#print(list(word_dict.keys())[-1], words_line[0])

guess_words = list(word_dict.keys())
#guess = random.choice(['adieu', 'audio','tears', 'irate'])
guess = 'arose'
print("\nTry the first word: " + guess.upper())

c = 6
count_av_guess = len(guess_words)
while c > 0 and count_av_guess > 1:
    result = input("Enter the state of the word: ").lower()
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

    while result == '':
        guess = random.choice(guess_words)
        print("Try: " + guess.upper())
        result = input("Enter the state of the word: ").lower()
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    status = ''
    for i in range(5):
        if result[i] == 'b':
            status += "\033[1;100m"+guess[i].upper()+"\033[0m"
        elif result[i] == 'o':
            status += "\033[1;41m"+guess[i].upper()+"\033[0m"
        elif result[i] == 'g':
            status += "\033[1;42m"+guess[i].upper()+"\033[0;0m"
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K") 
    sys.stdout.write(status)
    print()

    for  i in range(5):
        if result[i] == 'b':
            for word in guess_words[:]:
                if guess[i] in word:
                    guess_words.remove(word)
        elif result[i] == 'o':
            for word in guess_words[:]:
                if (guess[i] not in word):
                    guess_words.remove(word)
                else:
                    if word[i] == guess[i]:
                        guess_words.remove(word)
        elif result[i] == 'g':
            for word in guess_words[:]:
                if word[i] != guess[i]:
                    guess_words.remove(word)
    
    #print(guess_words)
    guess = guess_words[0]
    count_av_guess = len(guess_words)
    if count_av_guess > 1:
        print("Total Number of available choice: ", count_av_guess)
        print("The suggested word is: ", guess.upper())
    else:
        print("The Answer is: ", guess.upper())

    result = ''
    c -= 1