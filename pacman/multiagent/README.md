# Multi-Agent Search Project

## Overview
This project implements adversarial and stochastic search algorithms in a multi-agent Pacman environment. Pacman now faces multiple ghosts and must consider their actions when planning his moves.

## Key Files
- `multiAgents.py`: Contains all multi-agent search agents
- `pacman.py`: The main game file
- `game.py`: The game logic
- `util.py`: Utility functions
- `ghostAgents.py`: Ghost agent implementations

## Implemented Algorithms

### 1. Minimax
- Classical adversarial search algorithm
- Assumes ghosts are optimal adversaries
- Implemented with a specified depth limit
- Alternating layers of max (Pacman) and min (ghosts) nodes

### 2. Alpha-Beta Pruning
- Optimized version of minimax
- Maintains alpha (max's best option) and beta (min's best option)
- Prunes branches that cannot affect the final decision
- Significantly faster than standard minimax

### 3. Expectimax
- Handles probabilistic behavior
- Used when ghosts are not optimal adversaries
- Combines chance and max nodes
- More realistic for modeling suboptimal opponents

### 4. Evaluation Function
- Custom state evaluation for leaf nodes
- Considers factors like:
  - Food distance
  - Ghost proximity
  - Power pellet status
  - Remaining food

## Example Commands
```bash
# Run minimax agent
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4

# Run alpha-beta agent
python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3

# Run expectimax agent
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3
```
