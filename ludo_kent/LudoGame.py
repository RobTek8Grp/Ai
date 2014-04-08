'''
    Created on: April 4th, 2014
    Author:     Kent Stark Olsen
    E-Mail:     kent.stark.olsen@gmail.com
'''

import time
import random

import LudoBoard as lb

MAX_NUMBER_OF_TURNS = 10 #  Before 1000

class LudoGame():
    def __init__(self, players):
        self.board = lb.LudoBoard()
        self.players = players
        
        self.playerData = [[self.board.getPlayerSum(i)] for i in range(len(players))]

    def rollDie(self):
        return random.randint(1,6)

    def playGame(self):
        #   Find initial player
        random.seed(time.time())
        
        #   Unbias random generator
        i = 0
        rolls = random.randint(0,100)
        while (i < rolls):
            i += 1
            self.rollDie()

        rolls = [self.rollDie() for i in range(len(self.players))]
        print ' Initial rolls: ' + str(rolls)

        returnState = 1
        if len(rolls):
            startPlayer = 0
            maxRoll = 0
            for i in range(len(rolls)):
                if rolls[i] > maxRoll:
                    maxRoll = rolls[i]
                    startPlayer = i

            print ' Player (' + str(startPlayer) + ') won the right of starting the game ...'
            returnState = self.startGame(startPlayer)

        else:
            return -1

        return returnState

    def startGame(self, startPlayerIndex):
        #   Order players according to initial die roll
        players = self.players[startPlayerIndex:] + self.players[:startPlayerIndex]
        turns = 0
        playersFinished = []

        while(True):    #   Continue until game is finished
            turns += 1

            #   Current players turn
            for player in players:
                if not player.playerIndex in playersFinished:
                    roll = 0
                    rolls = 0
                    moveStatus = 0

                    while((not moveStatus and rolls < 3) or roll == 6):
                        roll = self.rollDie()
                        rolls += 1

                        moveStatus = player.move(roll, self.board)

                        if self.board.getPlayerSum(player.playerIndex) == 4 * lb.GOAL_POSITION:
                            playersFinished.append(player.playerIndex)

            print ' '
            print ' Turn#: ' + str(turns)
            print self.board

            #   Record data from each player this turns
            for player in self.players:
                i = player.playerIndex
                self.playerData[i].append(self.board.getPlayerSum(i))

            #   Check if game has ended
            if turns >= MAX_NUMBER_OF_TURNS or len(playersFinished) == len(self.players):
                if len(playersFinished) > 0:
                    print ' Game finished - Player (' + playersFinished[0] + ') won the game...'
                else:
                    print ' Game finished - Too many turns was taken ...'
                break;
                
        return 0
