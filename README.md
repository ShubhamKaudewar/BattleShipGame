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
2. Run the Python script `battleship.py`:
   ```bash
   python battleship.py
