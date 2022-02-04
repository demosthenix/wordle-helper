# wordle-helper

The 'w.txt' file contains rows of five letter words and a number associated with the frequency of appeanrence of the word, seperated by a space and sorted in ascending order.

'main.py' is the solver. This will provide word suggestions according to the available choices.
After evrery suggested word by the program, you need to put enter the word in Wordle. The letters should change colours.
You need to give a input of string lengthed 5 according to the colours that appeared in the wordle.

'b' for black/ white (The letter is not present in the answer)
'o' for orange (The letter is present in the answer but in different place)
'g' for green (The letter is present in the answer and is in the right place)

As an example:
Let's Say the answer is 'SEMEN' 

the program suggested word is: 'PUSSY'
so, 'P', 'U" and 'Y' are not present in the answer. Those letter will turn Black. 
'S' is present but in wrong place, so those will turn orange.

Therefore the input that you need to give would be: 'bboob'

Then, the program will give another suggestion after crossing out all the unpossible words.
Note: Press Enter, if you want to take another suggestion.

Like this... it will run until if you dont find the answer.
