#!/usr/bin/python
#coding = utf-8
#QTtest02.py
import sys

from PyQt4 import QtCore, QtGui

class My_window(QtGui.QWidget):
    def __init__(self):
        super(My_window, self).__init__()
        self.setWindowTitle("PyQt")
        self.resize(500, 300)
        gridlayout = QtGui.QGridLayout()

        self.radio1 = QtGui.QRadioButton("radio1")
        self.radio2 = QtGui.QRadioButton("radio2")
        self.radio3 = QtGui.QRadioButton("radio3")
        self.radio1.setChecked(True)

        gridlayout.addWidget(self.radio1)
        gridlayout.addWidget(self.radio2)
        gridlayout.addWidget(self.radio3)

        checkbox1 = QtGui.QCheckBox("checkbox1")
        checkbox2 = QtGui.QCheckBox("checkBox2")
        checkbox3 = QtGui.QCheckBox("checkBox3")
        checkbox1.setChecked(True)

        gridlayout.addWidget(checkbox1)
        gridlayout.addWidget(checkbox2)
        gridlayout.addWidget(checkbox3)

        self.button = QtGui.QPushButton("Ok")
        gridlayout.addWidget(self.button)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.OnButton)

        self.setLayout(gridlayout)
    def OnButton(self):
        if self.radio2.isChecked():
            self.radio2.setText('the ansery is Error')
        if self.radio1.isChecked():
            self.radio1.setText('the ansery is Error')
        if self.radio3.isChecked():
            self.radio3.setText('the ansery is right')
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = My_window()
    win.show()
    app.exec_()