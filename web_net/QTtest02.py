#!/usr/bin/python
#coding = utf-8
#QTtest02.py
import sys

from PyQt4 import QtCore, QtGui

class My_window(QtGui.QWidget):
    def __init__(self):
        super(My_window, self).__init__()
        self.setWindowTitle("FTP client")
        self.resize(500, 600)

        gridlayout = QtGui.QGridLayout()

        label = QtGui.QLabel('user name:')
        label2 = QtGui.QLabel('user word:')
        textFile = QtGui.QLineEdit()
        gridlayout.addWidget(label, 0, 0)
        gridlayout.addWidget(label2, 1, 0)
        gridlayout.addWidget(textFile, 0, 1)

        passwordFile = QtGui.QLineEdit()
        passwordFile.setEchoMode(QtGui.QLineEdit.Password)
        gridlayout.addWidget(passwordFile, 1, 1)

        textArea = QtGui.QTextEdit()
        textArea.setText("Begin:")
        gridlayout.addWidget(textArea, 3, 1)
        self.setLayout(gridlayout)

        self.button = QtGui.QPushButton("close")
        gridlayout.addWidget(self.button, 3, 0, 1, 1)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.OnClose)
        self.setLayout(gridlayout)

    def OnClose(self):
        self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = My_window()
    window.show()
    app.exec_()