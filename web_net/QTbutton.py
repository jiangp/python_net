#!/usr/bin/python
#coding = utf-8
#QTtest02.py
import sys

from PyQt4 import QtCore, QtGui

class My_window(QtGui.QWidget):
    def __init__(self):
        super(My_window, self).__init__()
        self.setWindowTitle("PyQt")
        self.resize(500, 500)
        gridlayout = QtGui.QGridLayout()

        button = QtGui.QPushButton("1234")
        button.setFlat(True)
        gridlayout.addWidget(button, 0, 0, 1, 2)
        self.setLayout(gridlayout)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    demo = My_window()
    demo.show()
    app.exec_()