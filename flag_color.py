#!/opt/local/bin/python3.4
# Jarik Oosting, 13-02-2015

from PyQt4 import QtGui
from random import randrange

class FlagColor(QtGui.QColor):

    """ Make Superclass """

    def __init__(self):
        QtGui.QColor.__init__(self)

        self.initUI()

    def initUI(self):

        self.color = QtGui.QColor(0, 0, 0)

    def setColor(self):

        # Set Blue color
        self.randomBlue = randrange(256)

        # Set Red color
        self.randomRed = randrange(256)

        # Set Green color
        self.randomGreen = randrange(256)

        self.color.setBlue(self.randomBlue)
        self.color.setRed(self.randomRed)
        self.color.setGreen(self.randomGreen)

        return self.color.name()

if __name__ == "__main__":
    app = FlagColor()