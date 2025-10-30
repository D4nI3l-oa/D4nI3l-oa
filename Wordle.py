# Input - How do we get the user's guesses?
guess = input("Enter a 5 letter guess: ")

# Input - Read a bunch of 5 letter words from a file!
words = open("words.txt", "r")
print(words.read())

guess = ''
attempts = 2
answer = 'colab'

if guess == answer and attempts <= 6:
  print("You Won! That took " + str(attempts) + " guess(es).")
else:
  print("You lost. The answer was " + answer + ".")

red = '🚨'
yellow = '🚧'
green = '💚'

letter_in_answer_word = True
letter_in_correct_position_in_answer_word = True

if letter_in_answer_word and letter_in_correct_position_in_answer_word:
  print(green)
elif letter_in_answer_word:
  print(yellow)
else:
  print(red)

guess = ""
attempts = 0

while guess != answer and attempts < 6:
  guess = input("Enter a 5 letter guess: ")
  attempts += 1

  # Show the output for how “close” the guess was!

if guess == answer and attempts <= 6:
  print("You Won! That took " + str(attempts) + " guess(es).")
else:
  print("You lost. The answer was " + answer + ".")

guess = 'crabs'
answer = 'colab'
index = 0

letter = guess[index]
if letter == answer[index]:
    print(letter + " - " + "💚")
elif letter in answer:
    print(letter + " - " + "🚧")
else:
    print(letter + " - " + "🚨")

red = '🚨'
yellow = '🚧'
green = '💚'

guess = 'crabs'
answer = 'colab'
index = 0
color = ''

while index < len(answer):
  letter = guess[index]
  if letter == answer[index]:
      color = green
  elif letter in answer:
      color = yellow
  else:
      color = red

  print(f"{letter} - {color}")

  index = index + 1

import random

file = open("words.txt", "r")

# Let’s say this is how you get a LIST of the words read from the input file
words = [word.strip() for word in file.readlines()]
print(words)

answer = random.choice(words)
print(answer)

def get_answer_word():
  # Read the input file of 5-letter words.
  file = open("words.txt", "r")
  words = [word.strip() for word in file.readlines()]

  # Set the answer word to be a random one!
  return random.choice(words)

# Notice this function doesn't have a return, it just prints to the console!
def print_guess_colors(guess, answer):
  index = 0
  while index < len(answer):
    letter = guess[index]
    if letter == answer[index]:
        color = '💚'
    elif letter in answer:
        color = '🚧'
    else:
        color = '🚨'

    print(f"{letter} - {color}")
    index = index + 1

# Set the answer word!
answer = get_answer_word()

# Play the game!
guess = ""
attempts = 0

while guess != answer and attempts < 6:
  guess = input("Enter a 5 letter guess: ")
  attempts = attempts + 1

  print_guess_colors(guess, answer)

# Tell the user if they won or lost!
if guess == answer and attempts <= 6:
  print("You Won! That took " + str(attempts) + " guess(es).")
else:
  print("You lost. The answer was " + answer + ".")
