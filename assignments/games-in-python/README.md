
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. By completing this assignment, you will practice core game logic, progress tracking, and handling win or loss outcomes.

## 📝 Tasks

### 🛠️ Set Up Game Data and State

#### Description
Create the foundation for the Hangman game by defining possible words, selecting a random secret word, and setting up variables for guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Define a predefined list with at least 5 words.
- Randomly select one word from the list at the start of the game.
- Initialize a progress display using underscores for unguessed letters (for example: `_ _ _ _`).
- Initialize a counter to track remaining incorrect guesses.

### 🛠️ Implement the Guessing Loop

#### Description
Implement the main game loop to collect letter guesses, update the displayed word, track incorrect attempts, and stop the game with a clear win or lose message.

#### Requirements
Completed program should:

- Prompt the player to enter one letter each turn.
- Reveal all matching letter positions when the guess is correct.
- Decrease remaining attempts only when the guess is incorrect.
- End the game with a win message when the full word is revealed.
- End the game with a lose message when attempts run out, and display the correct word.
