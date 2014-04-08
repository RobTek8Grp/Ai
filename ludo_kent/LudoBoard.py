'''
    Created on: April 6th, 2014
    Author:     Kent Stark Olsen
    E-Mail:     kent.stark.olsen@gmail.com
'''

import LudoPiece as lp

LENGTH = 52
PLAYER_OFFSET = 13
LAST_POSITION = 50
GOAL_POSITION = 56

class LudoBoard():
    def __init__(self):
        self.pieces = [ [lp.Piece(), lp.Piece(), lp.Piece(), lp.Piece()],
                        [lp.Piece(), lp.Piece(), lp.Piece(), lp.Piece()],
                        [lp.Piece(), lp.Piece(), lp.Piece(), lp.Piece()],
                        [lp.Piece(), lp.Piece(), lp.Piece(), lp.Piece()]]

    def __str__(self):
        return (' Ludo board:' +
                '\n Player (0): ' + str(self.pieces[0][0].position) + '  ' + str(self.pieces[0][1].position) + '  ' + str(self.pieces[0][2].position) + '  ' + str(self.pieces[0][3].position) +
                '\n Player (1): ' + str(self.pieces[1][0].position) + '  ' + str(self.pieces[1][1].position) + '  ' + str(self.pieces[1][2].position) + '  ' + str(self.pieces[1][3].position) +
                '\n Player (2): ' + str(self.pieces[2][0].position) + '  ' + str(self.pieces[2][1].position) + '  ' + str(self.pieces[2][2].position) + '  ' + str(self.pieces[2][3].position) +
                '\n Player (3): ' + str(self.pieces[3][0].position) + '  ' + str(self.pieces[3][1].position) + '  ' + str(self.pieces[3][2].position) + '  ' + str(self.pieces[3][3].position))

    def pieceCollisionCheck(self, dieRoll, playerIndex, curPiece):
        if curPiece.position == 0 or curPiece.position > LAST_POSITION:
            return []

        newAbsPosition = ((dieRoll + curPiece.position + PLAYER_OFFSET * playerIndex) % LENGTH)

        collidingWith = []

        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[i])):
                if curPiece != self.pieces[i][j] and self.pieces[i][j].position > 0 and self.pieces[i][j].position < LAST_POSITION + 1:
                    absPosition = ((self.pieces[i][j].position + PLAYER_OFFSET * i) % LENGTH)

                    if newAbsPosition == absPosition:
                        collidingWith.append(self.pieces[i][j])

        return [curPiece, collidingWith]

    def getPlayerSum(self, playerIndex):
        return sum(piece.position for piece in self.pieces[playerIndex])
