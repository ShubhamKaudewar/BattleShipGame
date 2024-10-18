# Battleship Game

This project implements a simple battleship game where two players (PlayerA and PlayerB) compete to destroy each other's ships by firing missiles at random coordinates.

## Game Features

- NxN battlefield (user-defined size) divided between two players.
- Ships are placed on the battlefield based on player input.
- Each player takes turns firing missiles at random coordinates in the opponent's zone.
- The game continues until one player has no ships left.

## Classes

### 1. **GameController**
   - Manages the game flow and player turns.
   - Starts the game and switches between players.
   - Handles missile firing and checks for hits and misses.

### 2. **Battlefield**
   - NxN grid representation of the battlefield.
   - Marks the grid with ships placed by each player.
   - Displays the battlefield with ships during the game.

### 3. **Player**
   - Represents a player with a fleet of ships.
   - Keeps track of ships and fired missile coordinates.

### 4. **Ship**
   - Represents a ship on the grid with a specific size and coordinates.
   - Checks whether it has been hit by a missile.

## How to Run

1. Clone the repository.
2. Run the unit test
3. Run the Python script `module_1.py`:
   ```bash
   python -m unittest tests\module_1.py

## Sample Response



<details>
  <summary>Click to expand Sample Game Response</summary>

```bash
Provide fleet details for player: 1
Provide fleet details for player: 2
Player1’s turn: Missile fired at (2, 9). Miss
Player1’s turn: Missile fired at (2, 9). Miss
Player1’s turn: Missile fired at (2, 9). Hit. Player2’s ship with id “SH3b” destroyed.
Player1’s turn: Missile fired at (2, 9). Miss
Player1’s turn: Missile fired at (2, 9). Miss
Player2’s turn: Missile fired at (0, 1). Miss
Player2’s turn: Missile fired at (0, 1). Miss
Player2’s turn: Missile fired at (0, 1). Miss
Player2’s turn: Missile fired at (0, 1). Miss
Player2’s turn: Missile fired at (0, 1). Miss
Player1’s turn: Missile fired at (7, 8). Miss
Player1’s turn: Missile fired at (7, 8). Miss
Player1’s turn: Missile fired at (7, 8). Hit. Player2’s ship with id “SH4b” destroyed.
Player1’s turn: Missile fired at (7, 8). Miss
Player2’s turn: Missile fired at (8, 4). Miss
Player2’s turn: Missile fired at (8, 4). Miss
Player2’s turn: Missile fired at (8, 4). Miss
Player2’s turn: Missile fired at (8, 4). Miss
Player2’s turn: Missile fired at (8, 4). Hit. Player1’s ship with id “SH5a” destroyed.
Player1’s turn: Missile fired at (7, 6). Miss
Player1’s turn: Missile fired at (7, 6). Miss
Player1’s turn: Missile fired at (7, 6). Miss
Player2’s turn: Missile fired at (1, 0). Miss
Player2’s turn: Missile fired at (1, 0). Miss
Player2’s turn: Missile fired at (1, 0). Miss
Player2’s turn: Missile fired at (1, 0). Miss
Player1’s turn: Missile fired at (8, 7). Miss
Player1’s turn: Missile fired at (8, 7). Miss
Player1’s turn: Missile fired at (8, 7). Miss
Player2’s turn: Missile fired at (6, 4). Miss
Player2’s turn: Missile fired at (6, 4). Miss
Player2’s turn: Missile fired at (6, 4). Miss
Player2’s turn: Missile fired at (6, 4). Miss
Player1’s turn: Missile fired at (0, 5). Hit. Player2’s ship with id “SH1b” destroyed.
Player1’s turn: Missile fired at (0, 5). Miss
Player1’s turn: Missile fired at (0, 5). Miss
Player2’s turn: Missile fired at (9, 0). Miss
Player2’s turn: Missile fired at (9, 0). Miss
Player2’s turn: Missile fired at (9, 0). Miss
Player2’s turn: Missile fired at (9, 0). Miss
Player1’s turn: Missile fired at (7, 9). Miss
Player1’s turn: Missile fired at (7, 9). Miss
Player2’s turn: Missile fired at (3, 4). Miss
Player2’s turn: Missile fired at (3, 4). Miss
Player2’s turn: Missile fired at (3, 4). Miss
Player2’s turn: Missile fired at (3, 4). Miss
Player1’s turn: Missile fired at (5, 5). Miss
Player1’s turn: Missile fired at (5, 5). Miss
Player2’s turn: Missile fired at (7, 3). Miss
Player2’s turn: Missile fired at (7, 3). Miss
Player2’s turn: Missile fired at (7, 3). Miss
Player2’s turn: Missile fired at (7, 3). Miss
Player1’s turn: Missile fired at (9, 9). Miss
Player1’s turn: Missile fired at (9, 9). Hit. Player2’s ship with id “SH5b” destroyed.
Player2’s turn: Missile fired at (6, 0). Miss
Player2’s turn: Missile fired at (6, 0). Miss
Player2’s turn: Missile fired at (6, 0). Miss
Player2’s turn: Missile fired at (6, 0). Miss
Player1’s turn: Missile fired at (6, 8). Miss
Player2’s turn: Missile fired at (4, 1). Miss
Player2’s turn: Missile fired at (4, 1). Hit. Player1’s ship with id “SH2a” destroyed.
Player2’s turn: Missile fired at (4, 1). Miss
Player2’s turn: Missile fired at (4, 1). Miss
Player1’s turn: Missile fired at (1, 8). Miss
Player2’s turn: Missile fired at (4, 0). Miss
Player2’s turn: Missile fired at (4, 0). Miss
Player2’s turn: Missile fired at (4, 0). Miss
Player1’s turn: Missile fired at (0, 5). Miss
Player2’s turn: Missile fired at (7, 4). Miss
Player2’s turn: Missile fired at (7, 4). Miss
Player2’s turn: Missile fired at (7, 4). Miss
Player1’s turn: Missile fired at (3, 7). Hit. Player2’s ship with id “SH2b” destroyed.
Congratulation 1 you won the war!
```
</details> 
