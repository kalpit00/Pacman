# Reinforcement Learning Project

## Overview
This project implements various reinforcement learning algorithms where Pacman learns optimal behaviors through trial and error. The agent learns from experience to make better decisions over time.

## Key Files
- `valueIterationAgents.py`: Value iteration agent implementation
- `qlearningAgents.py`: Q-learning agents
- `learningAgents.py`: Base classes for learning agents
- `environment.py`: Abstract environment class
- `gridworld.py`: Gridworld implementation

## Implemented Algorithms

### 1. Value Iteration
- Model-based learning algorithm
- Computes optimal values for each state
- Uses Bellman equations
- Requires complete knowledge of:
  - State transitions
  - Rewards
  - Discount factor

### 2. Q-Learning
- Model-free learning algorithm
- Learns action values (Q-values)
- Features:
  - Exploration vs exploitation
  - Learning rate
  - Discount factor
  - Experience replay

### 3. Approximate Q-Learning
- Handles large state spaces
- Uses feature-based representation
- Linear function approximation
- Feature extraction strategies

### 4. SARSA (State-Action-Reward-State-Action)
- On-policy learning algorithm
- Similar to Q-learning but uses current policy
- More conservative learning approach

## Example Commands
```bash
# Run value iteration
python gridworld.py -a value -i 100 -k 10

# Run Q-learning
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid 

# Run approximate Q-learning
python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid

# Watch trained agent
python pacman.py -p ApproximateQAgent -l smallGrid -n 10 -q
```

## Key Concepts
- Markov Decision Processes (MDPs)
- Temporal Difference Learning
- Function Approximation
- Exploration Strategies
- Policy Learning
