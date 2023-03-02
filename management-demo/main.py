import traceback

from ui import Ui


from qt_material import apply_stylesheet
from PyQt6 import QtCore, QtGui, QtWidgets
import sys


def init_style(app: QtWidgets.QApplication):
    f = open("style.css", "r")
    app.setStyleSheet(f.read())
class main_Ui(Ui, QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
   try:
       app = QtWidgets.QApplication(sys.argv)
       init_style(app)
       # apply_stylesheet(app, theme='light_blue.xml')
       test = main_Ui()
       sys.exit(app.exec())
   except Exception:
        print(traceback.format_exc())
