#!/usr/bin/python
# -*- coding: utf-8 -*-
# QT_test.py
import sys
from PyQt4 import QtGui  # 载入基本的GUI 窗口部件

class Icon(QtGui.QWidget):           #初始化一个窗口
    def __init__(self, parenf = None):
        QtGui.QWidget.__init__(self, parenf)

        self.setGeometry(300, 200, 600, 350)            #窗口大小
        self.setWindowTitle('Icon')    #窗口名
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)  #传参
    icon = Icon()
    icon.show()
    sys.exit(app.exec_())