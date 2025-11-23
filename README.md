This repository contains a simple Python implementation of the classic Rock, Paper, Scissors game. The player competes against the computer, which randomly selects one of the three options. The game continues for as long as the player wishes, and ends only when the user chooses to exit.
When the game begins, the player is greeted with instructions and asked to enter either rock, paper, or scissors. The input is checked to ensure it is valid. If the user enters something else, the game displays a message indicating the invalid choice and requests another input. The player can exit at any time by typing “exit.”
Each round, the computer randomly selects its move. Once both choices are determined, the game compares the user's selection to the computer’s and announces the outcome. A tie occurs when both players choose the same option. The user wins or loses depending on the classic rules of the game, where rock beats scissors, scissors beats paper, and paper beats rock.
For clarity, the win conditions the game follows are:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock

After each round, the game immediately prompts the user for another input, allowing continuous play without restarting the program. When the user eventually types “exit,” the game ends with a closing message and returns control to the Python environment.
To play the game, simply run the Python script in any terminal or IDE that supports input. The program will guide you automatically through each step.
