



  
def drawFigure(index):
  if index == 0:
    step1()
  if index == 1:
    step2()
  











import random 

wordList = ["help","food","pizza","cheese","beach"]
currentWord = random.choice(wordList)

print("Welcome to Hangman")

myString = []
guessedLetters = []
print("Here is your word:")
for x in range(len(currentWord)):
  myString.append('_')
print(myString)
drawingIndex = 0

def checkLetter(letter):
  for index in range(len(currentWord)):
    if letter == currentWord[index]:
      myString[index] = letter
  print(myString)

while True:
  userGuess = input("Please guess a letter").lower()
#Only 1 character
  if len(userGuess) != 1 and userGuess != " ":
    print("Please enter only one character!")
#No numbers
  elif userGuess.isalpha() == False:
    print("Please only enter a letter!")
  else:
    if userGuess in guessedLetters:
      print("You've already guessed that letter!")
    elif userGuess in currentWord:
      checkLetter(userGuess)
    else:
      drawFigure(drawingIndex)
      drawingIndex += 1



'''
Processing
-no numbers
-1 character
-lower case
-not a blank string
-no special characters.
cant guess letters that you've already guessed.
'''










