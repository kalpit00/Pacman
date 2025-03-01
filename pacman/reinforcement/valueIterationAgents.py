# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util, math

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        # value iteration algorithm

        #copy of the current values dictionary to store the updated values for each state
        newValues = self.values.copy()
        # loop through each non-terminal state and update its value based on the maximum expected reward from the available actions
        for i in range(self.iterations):
            for state in self.mdp.getStates():
                # If a state is terminal, its value remains unchanged
                if self.mdp.isTerminal(state):
                    continue
                # use getQValue to compute The maximum expected reward
                # params: a state and an action and returns the expected reward
                #  for taking that action from the current state, plus the discounted future reward based on the value of the resulting next state.
                newValues[state] = max([self.getQValue(state, action)
                                          for action in self.mdp.getPossibleActions(state)])
            self.values = newValues.copy()

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        totalValue = 0
        # loop through each possible transition from the current state, and for each transition
        # compute the expected reward as the sum of the immediate reward obtained for taking the action in the current state
        # and the discounted future reward based on the value of the resulting next state.
        for transition, probability in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, transition)
            totalValue += probability * (reward + (self.discount * self.getValue(transition)))
        return totalValue
    
    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # initialize maxAction to None and maxValue to negative infinity
        maxAction = None
        maxValue = -math.inf
        actions = self.mdp.getPossibleActions(state)
        # iterate through all possible actions for the given state using the getPossibleActions method of the MDP
        for action in actions:
            # For each action, compute the Q-value using the computeQValueFromValues method and update maxAction and maxValue if the Q-value
            # is higher than the current maximum.
            QValue = self.computeQValueFromValues(state, action)
            if QValue > maxValue:
                maxValue = QValue
                maxAction = action
        return maxAction
    
    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        # get a list of all the states in the MDP
        states = self.mdp.getStates()
        # loop for the given number of iterations and select a state from the list using the modulo operator to cycle through the states.
        for i in range(self.iterations): 
            state = states[i % len(states)]
            # If the selected state is terminal, the method moves on to the next iteration.
            if self.mdp.isTerminal(state):
                continue
            # Otherwise, get a list of possible actions for the current state using the getPossibleActions method of the MDP.
            actions = self.mdp.getPossibleActions(state)
            values = []
            # For each action, it computes the Q-value using the getQValue method and appends the value to a list of values.
            for action in actions:
                values.append(self.getQValue(state,action))
            # The value of the current state is then updated to the maximum value in the list using the max function.
            self.values[state] = max(values)

class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        # get a list of all the states in the MDP
        states = self.mdp.getStates()
        # initialize a predecessor dictionary, where each state in the MDP is a key and its value is a set of states that can transition to the key state.
        predecessors = {}
        for state in states:
            for action in self.mdp.getPossibleActions(state):
                for successor in [stateprob[0] for stateprob in self.mdp.getTransitionStatesAndProbs(state, action)]:
                    if successor not in predecessors:
                        predecessors[successor] = set()
                    predecessors[successor].add(state)
        # create a priority queue and adds all non-terminal states to it.
        pq = util.PriorityQueue()
        for state in states:
            if not self.mdp.isTerminal(state):
                # For each state, the method calculates the maximum Q-value over all possible actions
                maxQValue = max(self.getQValue(state, a) for a in self.mdp.getPossibleActions(state))
                # find the absolute difference between this value and the current value of the state.
                diff = abs(self.values[state] - maxQValue)
                # The state is then added to the priority queue with a priority based on the negative value of the difference.
                pq.update(state, -diff)

# In each iteration of the loop, pop a state from the pq and update its value based on the maximum Q-value over all possible actions.
        for i in range(self.iterations):
            if not pq.isEmpty():
                state = pq.pop()
                if not self.mdp.isTerminal(state):
                    maxQValue = max([self.computeQValueFromValues(state, a) for a in self.mdp.getPossibleActions(state)])
                    self.values[state] = maxQValue
                    #  loop through all the predecessors of the state and checks if their values need to be updated.
                    for pred in predecessors[state]:
                        maxQValue = max([self.computeQValueFromValues(pred, a) for a in self.mdp.getPossibleActions(pred)])
                        diff = abs(maxQValue - self.getValue(pred))
                        if diff > self.theta:
                            pq.update(pred, -diff)

