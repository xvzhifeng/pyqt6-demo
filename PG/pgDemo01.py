# Form implementation generated from reading ui file 'Pg-demo01.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainView(object) :
    def setupUi(self, mainView) :
        mainView.setObjectName("mainView")
        mainView.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        mainView.resize(901, 753)
        mainView.setMinimumSize(QtCore.QSize(901, 753))
        mainView.setMaximumSize(QtCore.QSize(901, 753))

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=mainView)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 251, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.task01 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.task01.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.task01.setContentsMargins(0, 0, 0, 0)
        self.task01.setSpacing(0)
        self.task01.setObjectName("task01")
        self.p1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.p1.setObjectName("p1")
        self.task01.addWidget(self.p1)
        self.p2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.p2.setObjectName("p2")
        self.task01.addWidget(self.p2)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.task01.addWidget(self.pushButton_7)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.task01.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.task01.addWidget(self.pushButton_9)
        # self.task01.addStretch(1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=mainView)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 509, 251, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.task02 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.task02.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.task02.setContentsMargins(0, 0, 0, 0)
        self.task02.setObjectName("task02")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.task02.addWidget(self.pushButton)

        self.line = QtWidgets.QFrame(parent=mainView)
        self.line.setGeometry(QtCore.QRect(270, 0, 16, 751))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=mainView)
        self.line_2.setGeometry(QtCore.QRect(0, 470, 271, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(parent=mainView)
        self.label_2.setGeometry(QtCore.QRect(20, 490, 200, 20))
        self.label_2.setMaximumSize(QtCore.QSize(200, 20))
        self.label_2.setIndent(20)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=mainView)
        self.label.setGeometry(QtCore.QRect(0, 10, 201, 21))
        self.label.setMaximumSize(QtCore.QSize(215, 21))
        self.label.setIndent(30)
        self.label.setObjectName("label")
        
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=mainView)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(280, 42, 603, 681))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content_2 = QtWidgets.QWidget(parent=self.verticalLayoutWidget_3)
        self.content_2.setMinimumSize(QtCore.QSize(601, 161))
        self.content_2.setMaximumSize(QtCore.QSize(601, 161))
        self.content_2.setAutoFillBackground(False)
        self.content_2.setObjectName("content_2")
        self.p2_01 = QtWidgets.QPushButton(parent=self.content_2)
        self.p2_01.setGeometry(QtCore.QRect(6, 66, 78, 32))
        self.p2_01.setObjectName("p2_01")
        self.p2_02 = QtWidgets.QPushButton(parent=self.content_2)
        self.p2_02.setGeometry(QtCore.QRect(203, 66, 80, 32))
        self.p2_02.setObjectName("p2_02")
        self.p2_03 = QtWidgets.QPushButton(parent=self.content_2)
        self.p2_03.setGeometry(QtCore.QRect(400, 66, 80, 32))
        self.p2_03.setObjectName("p2_03")
        self.verticalLayout.addWidget(self.content_2)
        self.content = QtWidgets.QWidget(parent=self.verticalLayoutWidget_3)
        self.content.setMinimumSize(QtCore.QSize(601, 161))
        self.content.setMaximumSize(QtCore.QSize(601, 161))
        self.content.setAutoFillBackground(False)
        self.content.setObjectName("content")
        self.p1_01 = QtWidgets.QPushButton(parent=self.content)
        self.p1_01.setGeometry(QtCore.QRect(400, 66, 78, 32))
        self.p1_01.setObjectName("p1_01")
        self.p1_02 = QtWidgets.QPushButton(parent=self.content)
        self.p1_02.setGeometry(QtCore.QRect(203, 66, 80, 32))
        self.p1_02.setObjectName("p1_02")
        self.p1_03 = QtWidgets.QPushButton(parent=self.content)
        self.p1_03.setGeometry(QtCore.QRect(6, 66, 80, 32))
        self.p1_03.setObjectName("p1_03")
        self.verticalLayout.addWidget(self.content)
        self.content_2.raise_()
        self.content.raise_()
        self.content_dict = {'p1' : self.content, 'p2' : self.content_2}
        self.change_content('p1')
        self.retranslateUi(mainView)
        self.p1.clicked.connect(self.change_content)  # type: ignore
        self.p2.clicked.connect(self.change_content)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainView)

    def change_content(self, is_sender=None):
        sender = self.sender()
        if not sender:
            sender = is_sender
        else:
            sender = sender.text()
        print(sender, is_sender)
        self.content_dict[sender].show()
        for i in self.content_dict.keys() :
            if i != sender :
                self.content_dict[i].close()

    def retranslateUi(self, mainView) :
        _translate = QtCore.QCoreApplication.translate
        mainView.setWindowTitle(_translate("mainView", "Form"))
        self.p1.setText(_translate("mainView", "p1"))
        self.p2.setText(_translate("mainView", "p2"))
        self.pushButton_7.setText(_translate("mainView", "PushButton"))
        self.pushButton_10.setText(_translate("mainView", "PushButton"))
        self.pushButton_9.setText(_translate("mainView", "PushButton"))
        self.pushButton.setText(_translate("mainView", "PushButton"))
        self.label_2.setText(_translate("mainView", "Task2"))
        self.label.setText(_translate("mainView", "Task1"))
        self.p2_01.setText(_translate("mainView", "p2_01"))
        self.p2_02.setText(_translate("mainView", "p2_02"))
        self.p2_03.setText(_translate("mainView", "p2_03"))
        self.p1_01.setText(_translate("mainView", "p1_01"))
        self.p1_02.setText(_translate("mainView", "p1_02"))
        self.p1_03.setText(_translate("mainView", "p1_03"))
