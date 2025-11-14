Blackjack & Wordle Text-Based Adventure Game
Project Overview
This is a text-based adventure game combining two classic games: Blackjack and Wordle. Developed as a freshman year project, this program demonstrates fundamental programming concepts including user input handling, game logic implementation, random number generation, and control flow structures.
Features
Blackjack

Classic card game simulation where players compete against the dealer
Goal: Get a hand value as close to 21 as possible without going over
Card values: Number cards (2-10) worth face value, face cards (J, Q, K) worth 10, Aces worth 1 or 11
Player can choose to "hit" (draw another card) or "stand" (keep current hand)
Dealer follows standard rules: must hit on 16 or below, must stand on 17 or above
Automatic win/loss detection for blackjack (21), bust (over 21), or standard scoring

Wordle

Word-guessing puzzle game based on the popular Wordle format
Player has 6 attempts to guess a 5-letter word
Color-coded feedback system:

Green: Correct letter in the correct position
Yellow: Correct letter in the wrong position
Gray: Letter not in the word


Word validation to ensure valid 5-letter guesses
Tracks guess history throughout the game

How to Play
Starting the Game

Run the program from the command line or terminal
Choose which game you want to play: Blackjack (1) or Wordle (2)
Follow the on-screen prompts for your selected game

Blackjack Gameplay

You and the dealer are dealt two cards initially
Decide whether to "hit" or "stand" based on your hand value
If your hand exceeds 21, you bust and lose automatically
If you stand, the dealer reveals their hand and plays according to rules
Winner is determined by who has the higher value without exceeding 21

Wordle Gameplay

A random 5-letter word is selected from the word list
Type your 5-letter guess and press Enter
Review the color-coded feedback
Use the information to narrow down your next guess
Win by guessing the correct word within 6 attempts

Technical Requirements

Python 3.x (or specify your programming language)
Standard library only (no external dependencies)
Terminal/Command line interface for text-based interaction

Installation & Setup
bash# Clone or download the project files
# Navigate to the project directory
cd blackjack-wordle-game

# Run the program
python main.py
Project Structure
project-folder/
│
├── main.py              # Main game launcher and menu
├── blackjack.py         # Blackjack game logic
├── wordle.py            # Wordle game logic
├── words.txt            # Word list for Wordle (optional)
└── README.md            # This file
Learning Objectives
This project demonstrates:

Control Structures: If/else statements, loops, and conditional logic
Data Structures: Lists, dictionaries for card decks and word management
Functions: Modular code design with reusable functions
User Input: Handling and validating player input
Randomization: Using random number generation for card shuffling and word selection
Game Logic: Implementing rules and win/loss conditions
String Manipulation: Character comparison and formatting for Wordle

Future Enhancements

Add betting system for Blackjack
Implement difficulty levels for both games
Create a scoring/statistics system
Add multiplayer functionality
Expand word list with categories or themes
Include sound effects or ASCII art for visual enhancement

Credits
Developed by  Daniel Onuoha-Amaechi as a Freshman Year Programming Project

License
This project is created for educational purposes.
