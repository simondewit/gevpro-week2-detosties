#!/opt/local/bin/python3.4
# Jarik Oosting, 13-02-2015

from PyQt4 import QtGui, QtColor
from random import randrange

class FlagColor(QtGui.QColor):

    """ Make Superclass """

    def __init__(self, country):
        QtGui.QColor.__init__(self)


    def randomColor(self):

        # Set Blue color
        randomBlue = randrange(256)
        self.setBlue(randomBlue)

        # Set Red color
        randomRed = randrange(256)
        self.setRed(randomRed)

        # Set Green color
        randomGreen = randrange(256)
        self.setGreen(randomGreen)

