#!/opt/local/bin/python3.4
# Simon de Wit, februari 2015

import sys
from country import Country
from PyQt4 import QtCore, QtGui


class Flags(QtGui.QWidget):
    def __init__(self):
        super(Flags, self).__init__()
        self.initUI()

    def iniUI(self):
        self.setWindowTitle("Country Flags")

        # Set grid layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

def main():
    app = QtGui.QApplication(sys.argv)
    f = Flags()
    app.exec_()


if __name__ == '__main__':
    main()