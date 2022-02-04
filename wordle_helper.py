# creating functions
def open_words():
    file = open("5_letter_words.txt", "r")
    data = file.read()
    file.close()
    v_letter_words = data.split('\n')
    return v_letter_words


def includes(a, *b):
    for i in b:
        if i not in a:
            return False
    else:
        return True


def find_words(a, *l):
    words = []
    for i in a:
        if includes(i, *l):
            words.append(i)
        else:
            pass
    return words


def isMatched(a, b):
    for j in range(len(b)):
        if b[j] != '*' and a[j] != b[j]:
            return False
    else:
        return True


def wordle_helper():
    print("hi, this is wordle helper")
    print("Enter yellow letters with a space in between.")
    print('\n')
    print('''Optionally if you have green letters input them like - 
    *(green letter)*** 
    before yellow lettr inputs''')
    print('\n')
    print("Input Examples: '*a*** a b c' or 'a b c'")
    print('\n')
    inp = input("Submit your inputs: ").split()
    if ('*' in inp[0]):
        a = inp[1:]
        ws = inp[0]
    else:
        a = inp

    word_data = open_words()
    words_found = find_words(word_data, *a)
    matched_words = [w for w in words_found if isMatched(w, ws)]
    print(matched_words)


# Calling main function
wordle_helper()
