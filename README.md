# Number Guessing Game

This is a number guessing game, can be played by 1/2 players for fun.

## Description

The rules are very simple. Two players play with each other. Each takes turn and 
sets a number between two pre-defined numbers. The other player tries to guess the 
number. In each round, the system shows if the guesses number is too high or too 
low, so the scope for the next guess becomes narrower and gurantees a converence. 
No penalty for invalid guess. The number of guesses required to guess the correct 
number is recorded. The player taking fewer guesses is the winner. 

In 1 player mode, the player plays against the computer. There are no difficulty
levels. When the computer sets the number, say in between 10 and 40, it uses a 
uniform distrubition of [11 39]. Additionally, when the computer guesses in between
two numbers, say 25 and 34, it applies a uniform distribution of [26 33].

## Notes
* Two numbers are set initially. The numbers have to be integer, at least 10 apart.

* If one has to search in between two numbers, say 10 and 40, no penalty added 
for invalid guess. For example, no penaly for gussing 45 in this scenario.



## Author

[Riaz Khan](https://github.com/riazakhan94)


