'''
    Created on: April 4th, 2014
    Author:     Kent Stark Olsen
    E-Mail:     kent.stark.olsen@gmail.com
'''

import time
import random

import LudoBoard as lb

NUMBER_OF_SIMPLE_TRAITS = 3
NUMBER_OF_ADVANCED_TRAITS = 4

'''
Genome for the PhylogenicPlayer:
=====================================================

Simple Strategy Gene:
    Index      Strategy
      0.    Rear Guard      (100 = Always move most rear piece on board, does not include pieces at home)
      1.    Sprinter        (010 = Always move foremost piece)
      2.    Random piece    (001 = Select random piece onboard)
                            (Other combinations make the phylogenic player choose strategy randomly from a uniform distribution)

Advanced Strategy Gene:
    Index      Strategy
      0.    Stay put        (0 = Does not try to assemble pieces on one spot,   1 = Try to assemble pieces at one spot)
      1.    Stay behind     (0 = Overtake enemy players,                        1 = Never overtake enemy players)
      2.    Stay home       (0 = Put many pieces onboard,                       1 = Only play with one piece onboard)
      3.    Revenge         (0 = Do not try to kick enemy pieces home           1 = Try to kick enemy pieces home)
'''

class PhylogenicPlayer():
    def __init__(self, playerIndex, genome = None):
        self.playerIndex = playerIndex

        if not genome:
            random.seed(time.clock())
            self.genome = [[random.randint(0,1) for i in range(NUMBER_OF_SIMPLE_TRAITS)], [random.randint(0,1) for i in range(NUMBER_OF_ADVANCED_TRAITS)]]
        else:
            self.genome = genome

    def __str__(self):
        return (' Player (' + str(self.playerIndex) + ') genome:' +
                '\n Simple strategy gene: ' + str(self.genome[0]) +
                '\n Advanced strategy gene: ' + str(self.genome[1]))

    def chooseSimpleStrategy(self):
        strategyList = []

        for i in self.genome[0]:
            if self.genome[0][1] == 1:
                strategyList.append(i)

        if len(strategyList):
            return strategyList[random.randint(0, len(strategyList) - 1)];
        else:
            return random.randint(0, NUMBER_OF_SIMPLE_TRAITS - 1)

    def move(self, dieRoll, board):
        #   Check player pieces position and arrange them
        home = []
        onBoard = []
        goal = []
        for piece in board.pieces[self.playerIndex]:
            if piece.position == 0:
                home.append(piece)
            elif piece.position == lb.GOAL_POSITION:
                goal.append(piece)
            else:
                onBoard.append(piece)

        simpleStrategy = self.chooseSimpleStrategy()

        return 1
