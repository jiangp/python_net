#!/usr/bin/python
#coding = utf-8
#QTtest02.py
import sys

from PyQt4 import QtCore, QtGui

class myWindow(QtGui.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setWindowTitle("PyQt")
        self.resize(500, 300)

        menubar = self.menuBar()
        self.file = menubar.addMenu('&File')
        open = self.file.addAction('open')
        self.connect(open, QtCore.SIGNAL('triggered()'), self.OnOpen)

        save = self.file.addAction('Save')
        self.connect(save, QtCore.SIGNAL('triggered()'), self.OnSave)
        self.file.addSeparator()
        close = self.file.addAction("Close")
        self.connect(close, QtCore.SIGNAL('triggered()'), self.OnClose)

        self.label = QtGui.QLabel('this is a google test')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def OnOpen(self):
        self.label.setText("open")
    def OnSave(self):
        self.label.setText("save")
    def OnClose(self):
        self.close()
    def contextMenuEvent(self, event):
        self.file.exec_(event.globalPos())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = myWindow()
    win.show()
    app.exec_()