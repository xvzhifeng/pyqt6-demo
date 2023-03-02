"""
    @Author:sumu
    @Date:2/25/23 2:33 PM
    @Email:xvzhifeng@126.com

"""
from qt_material import apply_stylesheet

from pgDemo01 import Ui_mainView
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class test(Ui_mainView, QtWidgets.QWidget):
    def __init__(self):
        super(Ui_mainView, self).__init__()
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    test = test()
    sys.exit(app.exec())

