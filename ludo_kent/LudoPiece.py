'''
    Created on: April 6th, 2014
    Author:     Kent Stark Olsen
    E-Mail:     kent.stark.olsen@gmail.com
'''

class Piece():
    def __init__(self, startPosition = 0):
        self.position = int(startPosition)

    def __str__(self):
        return  ' Position: ' + str(self.position)

    def __lt__(self, other):
        return self.position < other.position
