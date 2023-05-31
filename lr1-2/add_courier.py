# -*- coding: utf-8 -*-
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_Courier(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 360)
        MainWindow.setMinimumSize(QtCore.QSize(340, 360))
        MainWindow.setMaximumSize(QtCore.QSize(340, 360))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 70, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 120, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(178, 190, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(50, 190, 111, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 281, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 121, 51))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 140, 121, 51))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 270, 101, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Загружаем иконку из файла
        icon = QIcon('image/1.png')
        # Устанавливаем иконку для главного окна
        MainWindow.setWindowIcon(QtGui.QIcon(icon))

        validator = QRegExpValidator(QRegExp(r'[a-zA-Zа-яА-Я]*'))
        self.lineEdit.setValidator(validator)  # валидация только на буквы

        self.pushButton.clicked.connect(self.add_db_courier)

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('Курьер')
        msg.exec_()

    def add_db_courier(self):
        global en

        fio = self.lineEdit.text()

        name = f'{fio}'
        data_b = self.dateEdit.text()
        gender = self.comboBox.currentText()

        if len(fio) == 0:
            self.message_output("Информация", 'Ошибка в поле "ФИО"', QMessageBox.Critical)

        else:
            AddCourier(name, data_b, gender)

            if en == 'Add':
                self.message_output("Информация", 'Результат добавлен в Базу Данных!', QMessageBox.Information)

                self.lineEdit.clear()

            else:
                self.message_output("Информация", 'Такая запись уже имеется!', QMessageBox.Critical)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить Курьера"))
        self.label.setText(_translate("MainWindow", "Добавить Курьера"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Мужской"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Женский"))
        self.label_2.setText(_translate("MainWindow", "ФИО"))
        self.label_3.setText(_translate("MainWindow", "Дата рождения"))
        self.label_4.setText(_translate("MainWindow", "Пол:"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class AddCourier:
    def __init__(self, name, data_b, gender):

        global en

        name = name
        age = data_b
        gender = gender

        try:
            db = sqlite3.connect('db/home.db')
            cursor = db.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS courier(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                age TEXT,
                                gender TEXT
                                                    )''')

            db.commit()
            cursor.execute(f'SELECT name FROM courier WHERE name ="{name}"')
            if cursor.fetchone() is None:

                cursor.execute(f'INSERT INTO courier(name, age, gender) VALUES('
                               f'"{name}",'
                               f'"{age}",'
                               f'"{gender}")'
                               )
                db.commit()
                en = 'Add'

            else:
                en = 'Error'
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            self.message_output("Информация", f'Ошибка при работе с SQLite: {error}', QMessageBox.Critical)

        finally:
            if db:
                db.close()

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('Курьер')
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Courier()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
