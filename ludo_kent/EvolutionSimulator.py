'''
    Created on: April 6th, 2014
    Author:     Kent Stark Olsen
    E-Mail:     kent.stark.olsen@gmail.com
'''

import copy

import LudoGame as lg
import PhylogenicPlayer as pp

MAX_NUMBER_OF_GENERATIONS = 100
MAX_NUMBER_OF_GAMES = 1000

class EvolutionSimulator():
    def __init__(self, dataLogger = None, maxIterations = 100):
        self.dataLogger = dataLogger
        self.ludoGame = lg.LudoGame(players = [ pp.PhylogenicPlayer(0, [[1, 0], [0, 0, 0]]),
                                                pp.PhylogenicPlayer(1, [[0, 1], [0, 0, 0]]),
                                                pp.PhylogenicPlayer(2),
                                                pp.PhylogenicPlayer(3)])

    def generateGenerations (self):
        numberOfGenerations = 1

        gameStatus = self.ludoGame.playGame()

#        if not gameStatus:
#            #   Game was finished

#        else:
#            #   Something went wrong - Game was not finished
#            if gameState < 0:
#            elif gameState > 0:


        return numberOfGenerations
