# -*- coding: utf-8 -*-
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_Delivery(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 310)
        MainWindow.setMinimumSize(QtCore.QSize(320, 310))
        MainWindow.setMaximumSize(QtCore.QSize(320, 310))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 281, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 281, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 230, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 120, 261, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 180, 261, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
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

        self.courier_comboBox()
        self.customer_comboBox()

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

    def courier_comboBox(self):

        self.comboBox.clear()

        db = sqlite3.connect('db/home.db')
        cursor = db.cursor()
        cursor = cursor

        cursor.execute("""SELECT name FROM courier""")
        sql = cursor.fetchall()
        name = []
        for i in sql:
            name.append(i[0])
        self.comboBox.addItems(name)

    def customer_comboBox(self):

        self.comboBox_2.clear()

        db = sqlite3.connect('db/home.db')
        cursor = db.cursor()
        cursor = cursor
        cursor.execute("""SELECT address FROM customer""")
        sql = cursor.fetchall()
        address = []
        for i in sql:
            address.append(i[0])
        self.comboBox_2.addItems(address)

    def add_db_courier(self):
        global en

        name = self.comboBox.currentText()
        address = self.comboBox_2.currentText()

        AddDelivery(name, address)

        if en == 'Add':
            self.message_output("Информация", f'Результат добавлен в Базу Данных!', QMessageBox.Information)
        else:
            self.message_output("Информация", f'Такая запись уже имеется!', QMessageBox.Critical)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить достаку"))
        self.label_2.setText(_translate("MainWindow", "ФИО курьера"))
        self.label.setText(_translate("MainWindow", "Добавить Доставку"))
        self.label_5.setText(_translate("MainWindow", "Адрес клиента"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class AddDelivery:
    def __init__(self, name, address):

        global en

        name = name
        address = address

        try:
            db = sqlite3.connect('db/home.db')
            cursor = db.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS delivery(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                address TEXT
                                                    )''')

            db.commit()

            cursor.execute(f'INSERT INTO delivery(name, address) VALUES('
                           f'"{name}",'
                           f'"{address}")'
                           )
            db.commit()
            en = 'Add'


        except sqlite3.Error as error:
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
        msg.setWindowTitle('Доставка')
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Delivery()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
