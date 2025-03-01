# Artificial Intelligence Course Projects

This repository contains implementations of various fundamental Artificial Intelligence concepts and algorithms, primarily demonstrated through the Pacman game environment developed at UC Berkeley.

## Overview

The projects in this repository showcase different AI techniques including:
- Search Algorithms (BFS, DFS, A*, etc.)
- Multi-Agent Systems
- Reinforcement Learning
- Probabilistic Inference

## Project Structure

The repository is organized into multiple projects, each focusing on different aspects of AI:

- `pacman/`: Main project directory containing the Pacman game environment and implementations
  - Search-based pathfinding
  - Multi-agent gameplay strategies
  - Reinforcement learning agents
  - Probabilistic inference

## Getting Started

### Prerequisites
- Python 3.x
- No additional dependencies required

### Running the Projects

The main entry point is the `pacman.py` file. You can run different configurations using various command-line arguments:

```bash
# Basic game
python pacman.py

# Search algorithms
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs  # BFS
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs  # DFS
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar  # A* Search

# Different maze layouts
python pacman.py -l tinyMaze  # Tiny maze
python pacman.py -l mediumMaze  # Medium maze
python pacman.py -l bigMaze  # Big maze
```

### Key Arguments
- `-l`: Specifies the layout (maze)
- `-p`: Specifies the agent type
- `-a`: Additional arguments for the agent

## Acknowledgments

This project is based on the Pacman projects developed at UC Berkeley for their AI course. The projects have been modified and completed as part of coursework in Artificial Intelligence.

## License

This project is intended for educational purposes only. The base Pacman framework is courtesy of UC Berkeley's AI course materials.
