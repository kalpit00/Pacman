# Probabilistic Inference Project

## Overview
This project implements probabilistic inference algorithms to track ghosts in the Pacman world. The agent must reason about ghost positions with limited and noisy sensor information.

## Key Files
- `inference.py`: Contains inference algorithms
- `bustersAgents.py`: Agents for ghost tracking
- `busters.py`: Main game logic for ghost hunting
- `distanceCalculator.py`: Computes maze distances
- `bayesNet.py`: Bayesian network implementation

## Implemented Algorithms

### 1. Exact Inference (Hidden Markov Models)
- Forward algorithm implementation
- Maintains exact belief distributions
- Uses:
  - Transition models
  - Sensor models
  - Bayes' rule
  - Normalization

### 2. Particle Filtering
- Approximate inference method
- Maintains particles representing beliefs
- Features:
  - Particle resampling
  - Importance sampling
  - Particle reinvigoration
  - Adaptive particle count

### 3. Joint Particle Filter
- Tracks multiple ghosts simultaneously
- Handles ghost interactions
- Maintains joint distribution over positions

### 4. Advanced Inference
- Dynamic Bayesian Networks
- Advanced sensor fusion
- Multiple observation integration
- State estimation techniques

## Example Commands
```bash
# Run with exact inference
python busters.py -l labyrinth -p BasicAgentAA

# Run with particle filtering
python busters.py -l labyrinth -p ParticleAgent -n 30

# Run with joint particle filter
python busters.py -l labyrinth -p JointParticleAgent -n 30

# Watch inference in action
python busters.py -l labyrinth -p BasicAgentAA --frameTime 0.1
```

## Key Concepts
- Probabilistic State Estimation
- Hidden Markov Models
- Particle Filtering
- Bayesian Networks
- Sensor Fusion
