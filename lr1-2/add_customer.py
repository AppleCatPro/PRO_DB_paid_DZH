# -*- coding: utf-8 -*-
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_Customer(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 400)
        MainWindow.setMinimumSize(QtCore.QSize(330, 400))
        MainWindow.setMaximumSize(QtCore.QSize(330, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 121, 51))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 310, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 200, 121, 51))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(168, 250, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(40, 250, 111, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 120, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 281, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 180, 241, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 281, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
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
        self.lineEdit_2.setValidator(validator)  # валидация только на буквы

        self.pushButton.clicked.connect(self.add_db_customer)

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('Клиент')
        msg.exec_()

    def add_db_customer(self):
        global en

        fio = self.lineEdit.text()

        name = f'{fio}'
        data_b = self.dateEdit.text()
        gender = self.comboBox.currentText()
        address = self.lineEdit_2.text()

        if len(fio) == 0:
            self.message_output("Информация", 'Ошибка в поле "Фамилия"', QMessageBox.Critical)

        elif len(address) == 0:
            self.message_output("Информация", 'Ошибка в поле "Адрес"', QMessageBox.Critical)

        else:
            AddCourier(name, data_b, gender, address)

            if en == 'Add':
                self.message_output("Информация", 'Результат добавлен в Базу Данных!', QMessageBox.Information)

                self.lineEdit.clear()
                self.lineEdit_2.clear()

            else:
                self.message_output("Информация", 'Такая запись уже имеется!', QMessageBox.Critical)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить пользователя "))
        self.label_3.setText(_translate("MainWindow", "Дата рождения"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label_4.setText(_translate("MainWindow", "Пол:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Мужской"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Женский"))
        self.label.setText(_translate("MainWindow", "Добавить Клиент"))
        self.label_2.setText(_translate("MainWindow", "ФИО"))
        self.label_5.setText(_translate("MainWindow", "Адрес"))


class AddCourier:
    def __init__(self, name, data_b, gender, address):

        global en

        name = name
        age = data_b
        gender = gender
        address = address

        try:
            db = sqlite3.connect('db/home.db')
            cursor = db.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS customer(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                age TEXT,
                                address TEXT,
                                gender TEXT
                                                    )''')

            db.commit()
            cursor.execute(f'SELECT name FROM customer WHERE name ="{name}"')
            if cursor.fetchone() is None:

                cursor.execute(f'INSERT INTO customer(name, age, address, gender) VALUES('
                               f'"{name}",'
                               f'"{age}",'
                               f'"{address}",'
                               f'"{gender}")'
                               )
                db.commit()
                en = 'Add'

            else:
                en = 'Error'
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if db:
                db.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Customer()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
