# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 477)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_create_task = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_create_task.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.b_create_task.setObjectName("b_create_task")
        self.b_may_task = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_may_task.setGeometry(QtCore.QRect(0, 40, 101, 41))
        self.b_may_task.setObjectName("b_may_task")
        self.b_message = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_message.setGeometry(QtCore.QRect(0, 80, 101, 41))
        self.b_message.setObjectName("b_message")
        self.b_groups = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_groups.setGeometry(QtCore.QRect(0, 120, 101, 41))
        self.b_groups.setObjectName("b_groups")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 160, 101, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 200, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.b_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_exit.setGeometry(QtCore.QRect(0, 410, 101, 41))
        self.b_exit.setObjectName("b_exit")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(95, 0, 21, 461))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.columnView = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(110, 0, 551, 451))
        self.columnView.setObjectName("columnView")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(120, 330, 191, 22))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.text_task = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_task.setEnabled(True)
        self.text_task.setGeometry(QtCore.QRect(120, 350, 191, 71))
        self.text_task.setObjectName("text_task")
        self.send_task = QtWidgets.QPushButton(parent=self.centralwidget)
        self.send_task.setGeometry(QtCore.QRect(120, 420, 191, 24))
        self.send_task.setObjectName("send_task")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(320, 350, 331, 71))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_create_task.setText(_translate("MainWindow", "Создать задачу"))
        self.b_may_task.setText(_translate("MainWindow", "Мои задачи"))
        self.b_message.setText(_translate("MainWindow", "Сообщения"))
        self.b_groups.setText(_translate("MainWindow", "Группы"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.b_exit.setText(_translate("MainWindow", "Выйти"))
        self.lineEdit.setText(_translate("MainWindow", "Напишите текст задачи"))
        self.send_task.setText(_translate("MainWindow", "Создать задачу"))