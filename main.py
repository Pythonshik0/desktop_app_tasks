import random
import string
import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
import gui



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 477)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Создаем главный горизонтальный layout
        main_layout = QHBoxLayout(self.centralwidget)

        # Создаем вертикальный layout для кнопок
        button_layout = QVBoxLayout()

        # Устанавливаем отступы для вертикального layout в 0
        button_layout.setSpacing(0)
        button_layout.setContentsMargins(0, 0, 0, 0)

        # Создаем кнопки, устанавливаем их размер и добавляем их в вертикальный layout
        button_size = QSize(150, 40)  # Установите желаемый размер кнопок

        self.b_create_task = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_create_task.setObjectName("b_create_task")
        self.b_create_task.setFixedSize(button_size)
        button_layout.addWidget(self.b_create_task)

        self.b_may_task = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_may_task.setObjectName("b_may_task")
        self.b_may_task.setFixedSize(button_size)
        button_layout.addWidget(self.b_may_task)

        self.b_message = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_message.setObjectName("b_message")
        self.b_message.setFixedSize(button_size)
        button_layout.addWidget(self.b_message)

        self.b_groups = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_groups.setObjectName("b_groups")
        self.b_groups.setFixedSize(button_size)
        button_layout.addWidget(self.b_groups)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setFixedSize(button_size)
        button_layout.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setFixedSize(button_size)
        button_layout.addWidget(self.pushButton_6)

        self.b_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_exit.setObjectName("b_exit")
        self.b_exit.setFixedSize(button_size)
        button_layout.addWidget(self.b_exit)

        button_layout.addStretch()  # Добавляем растяжение после кнопок для размещения их вверху

        # Добавляем вертикальный layout для кнопок в главный горизонтальный layout
        main_layout.addLayout(button_layout)

        # Создаем вертикальную линию справа от кнопок
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line.setFixedWidth(2)  # Ширина линии

        # Добавляем вертикальную линию в главный горизонтальный layout
        main_layout.addWidget(self.line)

        # Создаем вертикальный layout для объектов создания задачи
        task_layout = QVBoxLayout()

        # Добавляем растяжимое пространство перед объектами, чтобы разместить их внизу
        task_layout.addStretch()

        # Добавляем объекты для создания задач в этот layout
        self.task_label = QtWidgets.QLabel("Task Creation", parent=self.centralwidget)
        self.task_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.create_task_button = QtWidgets.QPushButton("Create Task", parent=self.centralwidget)

        task_layout.addWidget(self.task_label)
        task_layout.addWidget(self.task_input)
        task_layout.addWidget(self.create_task_button)

        # Устанавливаем отступы для layout в 0
        task_layout.setSpacing(10)
        task_layout.setContentsMargins(10, 10, 10, 10)

        # Добавляем vertical layout для задач в главный горизонтальный layout
        main_layout.addLayout(task_layout)

        # Устанавливаем центральный виджет для главного окна
        MainWindow.setCentralWidget(self.centralwidget)

        # Устанавливаем текстовые метки для виджетов
        self.retranslateUi(MainWindow)


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


    def show_task_widgets(self):
        """Показать виджеты для создания задачи."""


    def show_may_task(self):
        """Скрыть виджеты для создания задачи."""


        """Отчистить виджеты для создания задачи."""



    def update_text_edit(self):
        """Обновить textEdit текстом из text_task."""



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()