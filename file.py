'''
import random
#Step 1 - Create a list of words to choose from and pick one at random
'''
'''
VARIABLES
keep track of letters already guessed - list
Track what stage we're at in the drawing - Int
Keep track of the word were trying to guess
Keeping track of what letters have and have not been guessed.

-Ensure that player only inputs a single letter
-Only letters can be entered, no numbers or punctuation.
-Can't enter multiple letters
-Track sCore

STEPS:
import random
create a list of 5-6 words (strings)
figure out how to pick a random word from the list and store it in a variable.

Define a function called "checkLetters"
Use a for loop based on the length of the chosen word to print out a corresponding number of underscores

'''

print("Welcome to Mr. Russ Hangman Game")
userInput = input("Please Enter a Letter")





wordList = ["help","food","pizza","cheese","beach"]
currentWord = random.choice(wordList)






guessedLetters = []
currentWord = random.choice(wordList)
currentWord = "pizza"
lenOfCurrentWord = len(currentWord)


#print("The quick brown fox jumped over the lazy dog")
#print("This is the song that doesn't end")

print("Welcome to Mr. Russ' Hangman Game!")
print("A word has already been chosen for you. It has "+str(lenOfCurrentWord)+" letters.")

def checkLetters(letter):
  myString = ""
  for x in range(lenOfCurrentWord):
    if currentWord[x] == letter:
      myString += letter+" "
    else:
      myString += "_ "
  print(myString)

userGuess = input("Guess A Letter")

# Length of the guess should be 1
if len(userGuess) != 1:
  print("Your guess must be 1 character")
# only letters
elif userGuess.isalpha() == False:
  print("Your guess must be a letter!")
# You can't guess a letter twice, we need to keep track of the letters guessed so far
else:
  if userGuess in guessedLetters:
    print("You already guessed that letter")
  else:
    guessedLetters.append(userGuess)
    checkLetters(userGuess)



# account for capitalization.

# if the player has guessed the word
print(userGuess)







'''
WHAT CODE DO WE NEED?
input - ask to guess single letters, not numbers, and not more than 1 character.

variables - check to see if the letter is in the word, no guessing a letter twice
if the letter is not in the word, then we advance the body part drawing by 1 step.

function to write the letter in the word (fill in the blanks)

list of words to choose from 

'''