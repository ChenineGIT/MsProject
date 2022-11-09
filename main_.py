from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets
import sys
import sqlite3
from PyQt5.QtWidgets import QCheckBox, QPushButton
from coordwidget import CoordWidget
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
from product_func import Product
from coordwidget import CoordWidget
import icon


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("menu.ui", self)
        self.even_buttons()

    def even_buttons(self):
        self.btnMenu.clicked.connect(self.expandir)
        self.btnHome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.btnExit.clicked.connect(lambda: self.close())

    def expandir(self):
        width = self.menulzquerdo.width()
        if width == 50:
            new_width = 180
            self.btnMenu.setIcon(QtGui.QIcon(":/icons/icons/left.png"))
        elif width == 180:
            new_width = 50
            self.btnMenu.setIcon(QtGui.QIcon(":/icons/icons/menu_bl.png"))

        try:
            self.animation = QPropertyAnimation(self.menulzquerdo, b"minimumWidth")
            self.animation.setStartValue(width)
            self.animation.setEndValue(new_width)
            self.animation.setDuration(350)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()
        except:
            self.btnMenu.setIcon(QtGui.QIcon(":/icons/icons/menu_bl.png"))
            self.animation.setStartValue(50)
            self.animation.setEndValue(50)
            self.animation.setDuration(350)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()




if __name__ == '__main__':
    window = QApplication(sys.argv)
    gui = Main()
    gui.show()
    window.exec_()