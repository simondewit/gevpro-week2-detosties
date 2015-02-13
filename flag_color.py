#!/opt/local/bin/python3.4
# Jarik Oosting, 13-02-2015

import sys
from PyQt4 import QtGui, QtColor

class FlagColor(QtGui.QColor):

    """ Make Superclass """

    def __init__(self,country):
        QtGui.QColor.__init__(self)


    def randomColor(self):
