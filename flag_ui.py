#!/opt/local/bin/python3.4
# Simon de Wit, februari 2015

import sys
from makeCountries import *
from flag_color import *
from country import Country
from PyQt4 import QtCore, QtGui


class Flags(QtGui.QWidget):
    def __init__(self):
        super(Flags, self).__init__()
        self.initUI()

    def initUI(self):

        self.c_list, self.c_obj_list = makeCountries()

        self.setWindowTitle("Country Flags")

        # Set grid layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Make QComboBox with countries
        self.c1 = QtGui.QComboBox(self)
        self.c1.addItems(self.c_list)
        grid.addWidget(self.c1, 1, 0)
        self.c1.setCurrentIndex(13)
        self.c1.currentIndexChanged.connect(self.updateUI)

        # Make QFrame for displaying the flag
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.show()

    def updateUI(self):
        """
        Updates the flag.
        """
        land = self.c_obj_list[self.c1.currentIndex()]
        color = land.getColor()
        self.square.setStyleSheet("QWidget { background-color: %s }" % color)




def main():
    app = QtGui.QApplication(sys.argv)
    f = Flags()
    app.exec_()


if __name__ == '__main__':
    main()