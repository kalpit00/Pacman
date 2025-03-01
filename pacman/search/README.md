# Search Project

## Overview
In this project, Pacman agent finds paths through his maze world using state-space search algorithms. The implemented algorithms are both uninformed (DFS, BFS) and informed (A* search).

## Key Files
- `search.py`: Implements the core search algorithms
- `searchAgents.py`: Contains search agents and heuristics
- `pacman.py`: The main game file
- `game.py`: The logic behind how the Pacman world works
- `util.py`: Useful data structures for implementing search algorithms

## Implemented Algorithms

### 1. Depth First Search (DFS)
- Stack-based implementation
- Explores deepest nodes first
- Not guaranteed to find shortest path

### 2. Breadth First Search (BFS)
- Queue-based implementation
- Explores all nodes at current depth before moving deeper
- Guarantees shortest path in unweighted graphs

### 3. Uniform Cost Search
- Priority queue implementation
- Considers path cost
- Guarantees optimal path with positive costs

### 4. A* Search
- Combines path cost with heuristic estimate
- Implements various heuristics:
  - Manhattan distance
  - Euclidean distance
  - Custom heuristics for specific problems

## Example Commands
```bash
# Run DFS
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs

# Run BFS
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Run A* with Manhattan heuristic
python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
