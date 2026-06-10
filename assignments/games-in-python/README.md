
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that uses string manipulation, loops, conditionals, and user input to let players guess a hidden word.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a Hangman game that randomly selects a hidden word from a list and prepares the initial game state.

#### Requirements
Completed program should:

- Define a list of possible words.
- Randomly choose one word for the player to guess.
- Initialize a display version of the word using underscores for each hidden letter.
- Track letters guessed by the player.

### 🛠️ Letter Guessing and Progress Display

#### Description
Allow the player to guess letters, update the display state, and show correct progress after each guess.

#### Requirements
Completed program should:

- Accept one letter guess from the player at a time.
- Reveal letters in the hidden word when the guess is correct.
- Show the current progress using a spaced format like `_ a _ _ m a n`.
- Prevent repeated guesses from affecting the game state.

### 🛠️ Game Loop and Win/Lose Conditions

#### Description
Create the main game loop to track incorrect guesses, detect win or loss, and display final results.

#### Requirements
Completed program should:

- Allow a limited number of incorrect guesses.
- Count and display remaining attempts.
- End the game when the player guesses the whole word or runs out of attempts.
- Display a clear win or lose message at the end.
