import random
#Step 1 - Create a list of words to choose from and pick one at random



print(len("hamburger"))

wordList = ["help","food","pizza","cheese","beach"]
guessedLetters = []
currentWord = random.choice(wordList)
lenOfCurrentWord = len(currentWord)


print("The quick brown fox jumped over the lazy dog")
print("This is the song that doesn't end")

print("Welcome to Mr. Russ' Hangman Game!")
print("A word has already been chosen for you. It has "+str(lenOfCurrentWord)+" letters.")

userGuess = input("Guess A Letter")

def checkLetters():
  
  for x in range(lenOfCurrentWord):
    
    print("_ ")

checkLetters()

# Length of the guess should be 1
if len(userGuess) != 1:
  print("Your guess must be 1 character")
else:
  if userGuess in guessedLetters:
    print("You already guessed that letter")
  else:
    guessedLetters.append(userGuess)
# You can't guess a letter twice, we need to keep track of the letters guessed so far
# account for capitalization.
# only letters

print(userGuess)







'''
WHAT CODE DO WE NEED?
input - ask to guess single letters, not numbers, and not more than 1 character.

variables - check to see if the letter is in the word, no guessing a letter twice
if the letter is not in the word, then we advance the body part drawing by 1 step.

function to write the letter in the word (fill in the blanks)

list of words to choose from 

'''

