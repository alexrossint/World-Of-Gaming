# World of Games

## About
I am building World of Games (WoG), a Python console application with three games. It is the first stage of a cumulative DevOps project, so I am building it step by step, and each stage adds a new layer on top of the previous one.

## Scope of Part 1
In this stage I build the foundations: a working console application with a menu, input validation and three playable games. Each game runs one round and returns a win or a loss.

## The games
### Memory Game
I see a sequence of numbers for 0.7 seconds, then I have to type it back from memory.

### Guess Game
I try to guess the secret number the computer picked.

### Currency Roulette
I estimate the ILS value of a random USD amount. The exchange rate comes from a currency API.

## Project structure
- MainGame.py is the entry point
- Live.py holds the welcome message, the game menu and difficulty selection
- GuessGame.py, MemoryGame.py and CurrencyRouletteGame.py hold the rules of each game
- requirements.txt lists the external Python dependencies

## Design principles
I keep the menu and the game rules in separate modules. Every game exposes a play(difficulty) function that returns True for a win and False for a loss. Invalid input never crashes the application or starts a game.

## Roadmap
In the next stages I add persistent scores, a web service, containers, automation and deployment.

## Status
Part 1 is in progress.