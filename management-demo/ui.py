from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox


class Ui(object):
    def setupUi(self, mainView):
        _translate = QtCore.QCoreApplication.translate
        mainView.setWindowTitle(_translate("mainView", "PG TOOL"))
        mainView.setObjectName("mainView")
        mainView.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        mainView.resize(1000, 800)
        mainView.setMinimumSize(QtCore.QSize(1000, 800))
        mainView.setMaximumSize(QtCore.QSize(1000, 800))
        # mainView.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)  # 隐藏边框
        # mainView.setWindowOpacity(0.7)

        self.topLine = QtWidgets.QWidget(parent=mainView)
        self.topLine.setGeometry(QtCore.QRect(0, 0, 1000, 50))
        self.topLine.setObjectName("topLine")
        self.topLine.setProperty("class", "topLine")
        self.top_h = QtWidgets.QHBoxLayout(self.topLine)
        self.top_h.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.top_h.setContentsMargins(0, 0, 0, 0)
        self.top_h.setSpacing(0)
        self.top_h.setObjectName("top_h")
        # mp = QtWidgets.QPushButton(self.topLine)
        # mp.setText("Market Place")
        # self.top_h.addWidget(mp)
        self.mp = QComboBox(self.topLine)
        self.mp.addItem('EU')
        self.mp.addItem('JP')
        self.mp.setProperty("class", "mp")
        self.top_h.addWidget(self.mp)
        self.top_h.addStretch(1)

        self.catalog = QtWidgets.QWidget(parent=mainView)
        self.catalog.setGeometry(QtCore.QRect(0, 50, 250, 800))
        self.catalog.setObjectName("catalog")
        self.catalog.setProperty("class", "sideLine")

        self.content = QtWidgets.QWidget(parent=mainView)
        self.content.setGeometry(QtCore.QRect(250, 50, 750, 800))
        self.content.setObjectName("content")
        self.content.setProperty("class", "contentPage")
        self.init_catalog()

    def init_catalog(self):
        self.label = QtWidgets.QLabel(parent=self.catalog)
        # self.label.setText("123")
        self.label.setProperty("class", "catalogLable")
        self.b_01 = QtWidgets.QPushButton(parent=self.catalog)
        self.b_01.setText("b01")
        self.b_01.setProperty("class","catalogButton")
        self.b_02 = QtWidgets.QPushButton(parent=self.catalog)
        self.b_02.setText("b01")
        self.b_02.setProperty("class", "catalogButton")
        self.catalog_l = QtWidgets.QVBoxLayout(self.catalog)
        self.catalog_l.addWidget(self.label)
        self.catalog_l.addWidget(self.b_01)
        self.catalog_l.addWidget(self.b_02)
        self.catalog_l.addStretch(1)
        pass
    def init_Content(self):
        pass

    # def mousePressEvent(self, event):  ##
    #         print("test")
    #         if event.button() == QtCore.Qt.LeftButton:
    #             self.Move = True  ##鼠标按下时设置为移动状态
    #             self.Point = event.globalPos() - self.pos()  ##记录起始点坐标
    #             event.accept()
    #
    # def mouseMoveEvent(self, QMouseEvent):  ##移动时间
    #         if QtCore.Qt.LeftButton and self.Move:  ##切记这里的条件不能写死，只要判断move和鼠标执行即可！
    #             self.move(QMouseEvent.globalPos() - self.Point)  ##移动到鼠标到达的坐标点！
    #             QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):  ##结束事件
    #         self.Move = False
