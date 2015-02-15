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

    def iniUI(self):

        flags = {}

        self.c_list, c_obj_list = makeCountries()

        for i in self.c_list:
            flags[i] = FlagColor()

        self.setWindowTitle("Country Flags")

        # Set grid layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        self.c1 = QtGui.QComboBox(self)
        self.c1.addItems(self.c_list)
        grid.addWidget(self.c1, 1, 0)
        self.c1.setCurrentIndex(13)
        self.c1.currentIndexChanged.connect(self.updateUI)

    def updateUI(self):
        """
        Updates the flag.
        """
        flags[self.c1.currentText()] =



def main():
    app = QtGui.QApplication(sys.argv)
    f = Flags()
    app.exec_()


if __name__ == '__main__':
    main()