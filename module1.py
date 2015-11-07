#-------------------------------------------------------------------------------
# Name:        FTP
# Purpose:
#
# Author:      Tailong Zhou Tai
#
# Created:     04/15/2014

#-------------------------------------------------------------------------
Squares= 9
EMPTY = " "

class Board(object):
    def Draw(self):
        board = []
        for square in range (Squares):
            board.append(EMPTY)
        return board

class Mark(Board):
    def Draw(self,b,c):
        list[b]=c

#list=["1","2","3","4","5","6","7","8","9"]
list = [1,2,3,4,5,6,7,8,9]
print (list[1])

b= Board()
m=Mark()
m.Draw("X",9)
m.Draw("O",1)
