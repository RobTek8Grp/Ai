#!/usr/bin/python
'''
    Created on: April 7th, 2014
    Author:     Kent Stark Olsen
    E-Mail:     kent.stark.olsen@gmail.com
'''

import os
from sys import platform as _platform

import LudoGame as lg
import PhylogenicPlayer as pp

if __name__ == '__main__':
    #   Clear screen
    if _platform == "linux" or _platform == "linux2":   #   Linux
        os.system('clear')
    elif _platform == "darwin":                         #   OSX
        os.system('clear')
    elif _platform == "win32":                          #   Windows
        os.system('cls')

    #   Testing ludo
    print '\n Ludo mechanics test:'
    print ' =================================================================='

    ludoGame = lg.LudoGame(players = [  pp.PhylogenicPlayer(0, [[1, 0, 0], [0, 0, 0, 0]]),
                                        pp.PhylogenicPlayer(1, [[0, 1, 0], [0, 0, 0, 0]]),
                                        pp.PhylogenicPlayer(2, [[0, 0, 1], [0, 0, 0, 0]]),
                                        pp.PhylogenicPlayer(3)])

    for player in ludoGame.players: print player
    print ' '
    print ludoGame.board
    print ' '

    print ' Phylogenic players and board instantiated ...'
    print ' '
    print ' Playing ludo game ...'
    print ' '

    gameStatus = ludoGame.playGame()
    
    print ' '
    if not gameStatus:
        print ' Game was played succesfully ... OK!'
    else:
        print ' Game was played succesfully ... FAILED!'
        
    print ' ==================================================================\n'
