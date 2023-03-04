# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # Information from the current state
        currentGhostStates = currentGameState.getGhostStates()
        currentScaredTimes = [ghostState.scaredTimer for ghostState in currentGhostStates]

        "*** YOUR CODE HERE ***"

        # Calculate the distance to the closest food
        foodList = newFood.asList()
        foodDistances = [manhattanDistance(newPos, foodPos) for foodPos in foodList]
        closestFoodDistance = min(foodDistances) if len(foodDistances) > 0 else 0

        # Calculate the distance to the closest ghost. Use manhattan distance
        ghostDistances = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        closestGhostDistance = min(ghostDistances) if len(ghostDistances) > 0 else 0

        # Calculate the score for this state. This was returned initally but use this variable to update score
        score = successorGameState.getScore()

        # Add a bonus for getting closer to the closest food
        if closestFoodDistance > 0:
            score += 1.0 / closestFoodDistance

        # Add a penalty for getting too close to a ghost
        if closestGhostDistance > 0:
            if closestGhostDistance <= 1 and currentScaredTimes[0] == 0:
                score -= 1000  # Huge penalty for getting eaten by a ghost
            else:
                score -= 1.0 / closestGhostDistance
        return score

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        actions = gameState.getLegalActions(0)
        currentScore = -999
        returnAction = ''

        # USE AGENTINDEX as param to generalize between all agents. Need a way to get min and max between parent and child. add functions

        # ftn to get the minimum value. This represents the Ghost Layer        
        def minimum(gameState, depth, agentIndex):
            value = 999
            
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            
            actions = gameState.getLegalActions(agentIndex)
            
            for action in actions:
                successor = gameState.generateSuccessor(agentIndex, action)
                
                if agentIndex == (gameState.getNumAgents() - 1):
                    value = min (value, maximum(successor, depth))
                    
                else:
                    value = min(value,minimum(successor,depth,agentIndex+1))
                    
            return value
        
        # ftn to get the maximum value. This represents the Pacman Layer
        def maximum(gameState, depth):
            value = -999
            currentDepth = depth + 1
            
            if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
                return self.evaluationFunction(gameState)

            actions = gameState.getLegalActions(0)
            
            for action in actions:
                successor = gameState.generateSuccessor(0, action)
                value = max (value, minimum(successor, currentDepth, 1))
                
            return value
        
        for action in actions:
            nextState = gameState.generateSuccessor(0, action)
            
            # update score.
            score = minimum(nextState, 0, 1)
            
            # Traverse if score > current score and update nodes
            if score > currentScore:
                returnAction = action
                currentScore = score
                
        return returnAction

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        # Again need a max and min ftn like before between parent and child
        # ALPHA represents Pacman, and maximizing value, BETA represents Ghosts, and minimizing value
        # Use a second variable to update Alpha and Beta values if traversed to a child

        # max ftn, USE DEPTH, Alpha, Beta as params
        def maximum(gameState, depth, alpha, beta):
            currentDepth = depth + 1
            if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
                return self.evaluationFunction(gameState)
            
            value = -999
            actions = gameState.getLegalActions(0)
            # second var to store updated alpha
            alphaNew = alpha
            
            for action in actions:
                successor = gameState.generateSuccessor(0, action)
                # use min function to get value of child
                value = max (value, minimum(successor, currentDepth, 1, alphaNew, beta))
                # if value by min function is greater than beta, prune the sub tree
                if value > beta:
                    return value
                
                alphaNew = max(alphaNew, value)
                
            return value
        
        # min ftn
        def minimum(gameState, depth, agentIndex, alpha, beta):
            value = 999
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            
            actions = gameState.getLegalActions(agentIndex)
            betaNew = beta
            
            for action in actions:
                successor= gameState.generateSuccessor(agentIndex, action)
                
                if agentIndex == (gameState.getNumAgents() - 1):
                    # use max ftn to get value of child
                    value = min (value, maximum(successor, depth, alpha, betaNew))
                    # if value returned by max ftn < alpha, prune the sub tree
                    if value < alpha:
                        return value
                    betaNew = min(betaNew, value)
                else:
                    value = min(value, minimum(successor, depth, agentIndex + 1, alpha, betaNew))
                    
                    if value < alpha:
                        return value
                    
                    betaNew = min(betaNew, value)
            
            return value

        #Alpha-Beta Pruning algorithm. Check the slides
        alpha = -999
        beta = 999
        currentScore = -999
        returnAction = ''
        actions = gameState.getLegalActions(0)
        
        for action in actions:
            nextState = gameState.generateSuccessor(0, action)
            score = minimum(nextState, 0, 1, alpha, beta)

            if score > currentScore:
                returnAction = action
                currentScore = score
   
            if score > beta:
                return returnAction
            
            alpha = max(alpha, score)
        
        return returnAction

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        ## now have max nodes for Pacman and expected nodes for random agents

        # max function, similar to minimax/alpha-beta
        def maximum(gameState, depth):
            currentDepth = depth + 1
            
            # as usual check if depth is reached or end state reached.
            if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
                return self.evaluationFunction(gameState)
            
            value = -999
            actions = gameState.getLegalActions(0)
            
            for action in actions:
                successor = gameState.generateSuccessor(0, action)
                value = max (value, expectedLevel(successor, currentDepth, 1))
            
            return value
        
        #ftn to get expected value of a chance node
        # USE AGENTINDEX as param for generalization, make sure to return avg
        def expectedLevel(gameState, depth, agentIndex):
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            
            actions = gameState.getLegalActions(agentIndex)
            totalValue = 0
            totalActions = len(actions)
            
            for action in actions:
                successor = gameState.generateSuccessor(agentIndex, action)
                # max node
                if agentIndex == (gameState.getNumAgents() - 1):
                    expectedvalue = maximum(successor, depth)
                # chance node
                else:
                    expectedvalue = expectedLevel(successor, depth, agentIndex + 1)
                
                totalValue = totalValue + expectedvalue
            
            if totalActions == 0:
                return  0
            # expected value is ag of total values amongst all possible moves and total cost
            ## use float values here, int's give wrong answers
            return float(totalValue) / float(totalActions)
        
        ## choose action with highest expected value
        actions = gameState.getLegalActions(0)
        currentScore = -999
        returnAction = ''
        
        for action in actions:
            nextState = gameState.generateSuccessor(0, action)
            score = expectedLevel(nextState, 0, 1)
            
            if score > currentScore:
                returnAction = action
                currentScore = score
        
        return returnAction


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).
    DESCRIPTION: <write something here so we know what you did>
    1. extract the current position of Pacman, the remaining food pellets, the ghost locations, and the scared timer of each ghost.
    2. calculate the manhattan distance between the Pacman and food, and between Pacman and each ghost location.
    3. calculate the total number of uneaten food pellets, number of times a ghost is scared,
        the distances between Pacman and each ghost, and the number of food pellets left
    4. assign a score based on these factors, adding the current score, the reciprocal of the sum of the food distances, and the number of uneaten food pellets.
    5. If any ghost is scared, include time scared in score, and  -1 * power pellets, -1 * distance between Pacman and the ghosts.
    6. If no ghost is currently scared, then the score only includes the distance between Pacman and the ghosts and the total power pellets.
    """
    "*** YOUR CODE HERE ***"
    ## Get pacman pos, food, ghosts and scaredGhosts from state
    position = currentGameState.getPacmanPosition()
    food = currentGameState.getFood()
    ghosts = currentGameState.getGhostStates()
    scaredGhost = [ghostState.scaredTimer for ghostState in ghosts]
    
    foodList = food.asList()
    foodDistance = [0]
    # manhattan distance between pacman and food
    for f in foodList:
        foodDistance.append(manhattanDistance(position, f))

    ghostLocation = []
    for ghost in ghosts:
        ghostLocation.append(ghost.getPosition())
    
    ghostDistance = [0]
    # manhattan distance between ghosts and pacman
    for l in ghostLocation:
        ghostDistance.append(manhattanDistance(position, l))

    ## USE gamestate.GETCAPSULES() to get power pellets
    totalPowerPellets = len(currentGameState.getCapsules())

    ## sum the total uneaten food pellets, total scared times and distances for ghosts, assign score var
    score = 0
    eatenFood = len(food.asList(False))           
    totalTimesScared = sum(scaredGhost)
    totalGhostDistances = sum(ghostDistance)
    foodDistances = 0

    ## reciprocal of food distances
    if sum(foodDistance) > 0:
        foodDistances = 1.0 / sum(foodDistance)

    # update score
    score += currentGameState.getScore()  + foodDistances + eatenFood

    # if ghost scared, add the scared time to score and substract the power pellets and ghost distances
    if totalTimesScared > 0:    
        score +=   totalTimesScared + (-1 * totalPowerPellets) + (-1 * totalGhostDistances)
    # if ghost not scored, just add power pellets and ghost distances    
    else :
        score +=  totalGhostDistances + totalPowerPellets
    # return final score
    return score


# Abbreviation
better = betterEvaluationFunction
