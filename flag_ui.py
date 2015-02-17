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

        # Make QComboBox with countries
        self.c1 = QtGui.QComboBox(self)
        self.c1.addItems(self.c_list)
        self.c1.setGeometry(20, 20, 200, 25)
        self.c1.setCurrentIndex(0)
        self.c1.currentIndexChanged.connect(self.updateUI)

        # Make QFrame for displaying the flag
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(20, 65, 200, 200)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.c_obj_list[self.c1.currentIndex()].getColor())

        self.show()

    def updateUI(self):
        """
        Updates the flag.
        """
        # Get the color from the corresponding country object in the list
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.c_obj_list[self.c1.currentIndex()].getColor())




def main():
    app = QtGui.QApplication(sys.argv)
    f = Flags()
    app.exec_()


if __name__ == '__main__':
    main()