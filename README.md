# Multi-Level Number Guessing Game


A modular command-line interface (CLI) guessing game built with Python. The game challenges players to guess a randomly generated number within a limited number of attempts, featuring dynamic difficulty levels and comprehensive input validation.


## Features


- **Modular Architecture:** The codebase is cleanly separated into a main application script and a helper module for game logic.


- **Dynamic Difficulty Levels:** Offers 4 distinct difficulty configurations:
  - **Easy:** 3 attempts, numbers 1-10
  - **Medium:** 3 attempts, numbers 1-20
  - **Hard:** 4 attempts, numbers 1-50
  - **Very Hard:** 5 attempts, numbers 1-100


- **Strict Input Validation:** Gracefully handles invalid choices, non-numeric strings (`ValueError`), and out-of-range numbers without crashing the session.


- **Replayability Option:** Allows players to instantly restart a game within their chosen difficulty level or return to the main menu.


## Project Structure


To run this project properly, ensure your local files are arranged as follows:


```text
├── moduls.py       # Contains game logic, generation, and validation functions
└── main.py         # Main entry point holding the game menus and loops
```
## How it Works


The game relies on structured conditional loops to manage the state.


### Logic Breakdown


1. **Random Generation:** Uses Python's native `random.randint` to pick a secret target number based on the selected level.


2. **Feedback System:** Provides real-time hints after each incorrect guess, letting the player know if their submitted number is higher or lower than the target.


3. **State Tracking:** Monitors remaining attempts and updates the user dynamically after every turn.


## How to Run


### Prerequisites
Make sure you have Python 3.x installed.


### Steps


1. Create a file named `moduls.py` and paste the logic functions inside it.


2. Create a second file named `main.py` in the same directory for the interface menu.


3. Open your terminal and execute:


   ```bash
   python main.py
