#!/usr/bin/python
'''
    Created on: April 4th, 2014
    Author:     Kent Stark Olsen
    E-Mail:     kent.stark.olsen@gmail.com
'''

import os
from sys import platform as _platform

import EvolutionSimulator as evoSim

if __name__ == '__main__':
    #   Clear screen
    if _platform == "linux" or _platform == "linux2":   #   Linux
        os.system('clear')
    elif _platform == "darwin":                         #   OSX
        os.system('clear')
    elif _platform == "win32":                          #   Windows
        os.system('cls')

    #   Start phylogenic algorithm
    print '\n Kents Ludo AI in phylogenic time:'
    print ' =================================================================='

    evolutionSimulator = evoSim.EvolutionSimulator()
    evolutionSimulator.generateGenerations()

    print '\n\n'
