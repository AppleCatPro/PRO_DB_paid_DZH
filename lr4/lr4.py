# -*- coding: utf-8 -*-
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import QMessageBox
from server_4 import app


class FlaskServerThread(QThread):
    def __init__(self):
        super().__init__()

        self.app = app

    def run(self):
        app.run(debug=False)


class Ui_lr_4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 420)
        MainWindow.setMinimumSize(QtCore.QSize(1070, 420))
        MainWindow.setMaximumSize(QtCore.QSize(1070, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 9, 1051, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 1051, 61))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 120, 1051, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(720, 280, 151, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 180, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 230, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 140, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(720, 180, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(630, 280, 91, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(890, 330, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(720, 230, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 330, 91, 21))
        self.label_9.setObjectName("label_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(890, 230, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(890, 180, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(720, 330, 151, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 220, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 210, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color :rgb(255, 0, 0)")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(110, 210, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 280, 131, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(520, 140, 31, 251))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 21))
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

        conn = sqlite3.connect('db/home.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS lr4
                                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                name TEXT,
                                                coordinates BLOB)''')
        conn.commit()

        self.label_12.setText('Выключен')
        self.pushButton_2.setEnabled(True)

        self.pushButton_2.clicked.connect(self.start_server)
        self.pushButton_9.clicked.connect(self.open_in_browser)

        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_8.clicked.connect(self.update_data)
        self.pushButton_6.clicked.connect(self.del_data)

    def start_server(self):

        self.pushButton_2.setEnabled(False)
        self.label_12.setText('Включен')
        self.label_12.setStyleSheet("color : rgb(0, 170, 0)")

        self.flask_thread = FlaskServerThread()
        self.flask_thread.start()

    def stop_server(self):
        self.pushButton_2.setEnabled(True)
        self.label_12.setText('Выключен')

    def create_connection(self):
        conn = sqlite3.connect('db/home.db')
        return conn

    # def view_data(self):
    #     conn = self.create_connection()
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM lr4")
    #     rows = cur.fetchall()
    #     cur.close()
    #     conn.close()
    #     return rows

    def add_data(self):

        name = self.lineEdit_3.text()
        x = self.lineEdit_2.text()
        y = self.lineEdit_4.text()
        if name and x and y:
            conn = self.create_connection()
            cur = conn.cursor()
            cur.execute(f'SELECT name FROM lr4 WHERE name ="{name}"')

            if cur.fetchone() is None:

                cur.execute("INSERT INTO lr4 (name, coordinates) VALUES (?, ?)", (name, f'({x},{y})'))
                conn.commit()

                self.message_output("Информация", f'Запись {name} успешно добавлена!', QMessageBox.Information)
            else:
                self.message_output("Информация", 'Такая запись существует!', QMessageBox.Critical)

            cur.close()
            conn.close()

        else:
            self.message_output("Информация", f"Вы не указали данные.", QMessageBox.Critical)

    def del_data(self):

        id = self.lineEdit_5.text()

        if id:
            conn = self.create_connection()
            cur = conn.cursor()
            cur.execute(f'SELECT id FROM lr4 WHERE id ="{id}"')

            if cur.fetchone() is None:
                self.message_output("Информация", 'Такой записи нет!', QMessageBox.Critical)

            else:
                cur.execute(f'DELETE FROM lr4 WHERE id ="{id}"')
                conn.commit()

                self.message_output("Информация", f'Запись {id} успешно удалена!', QMessageBox.Information)

        else:
            self.message_output("Информация", f"Вы не указали ID", QMessageBox.Critical)

    def update_data(self):

        name = self.lineEdit_3.text()
        x = self.lineEdit_2.text()
        y = self.lineEdit_4.text()

        if name and x and y:

            conn = self.create_connection()
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM lr4 WHERE name = "{name}" ')

            if cur.fetchone() is None:

                self.message_output("Информация", 'Такой записи нет!', QMessageBox.Critical)
            else:
                cur.execute("UPDATE lr4 SET coordinates = ? WHERE name = ?", (f'({x},{y})', name))
                conn.commit()

                self.message_output("Информация", f'Запись {name} успешно обновлена!', QMessageBox.Information)

            cur.close()
            conn.close()
        else:
            self.message_output("Информация", f"Вы не указали данные.", QMessageBox.Critical)

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('Домашняя страница')
        msg.exec_()

    def open_in_browser(self):
        url = QUrl("http://localhost:5000")
        QDesktopServices.openUrl(url)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа № 4"))
        self.label.setText(_translate("MainWindow", "Задание:"))
        self.label_4.setText(_translate("MainWindow",
                                        "Знакомство с представлением и обработкой пространственной информации в базе данных. \n"
                                        "Используя Python Flask."))
        self.label_2.setText(_translate("MainWindow", " Название City:"))
        self.label_3.setText(_translate("MainWindow", " X Coordinate:"))
        self.label_8.setText(_translate("MainWindow", "Работа с данными"))
        self.label_6.setText(_translate("MainWindow", " Y Coordinate:"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить"))
        self.label_9.setText(_translate("MainWindow", "Введите ID:"))
        self.pushButton_8.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить"))
        self.label_7.setText(_translate("MainWindow", "Работа с сервером"))
        self.pushButton_2.setText(_translate("MainWindow", "Запустить"))
        self.label_12.setText(_translate("MainWindow", "Включен"))
        self.label_11.setText(_translate("MainWindow", "Состояние:"))
        self.pushButton_9.setText(_translate("MainWindow", "Открыть сайт"))


if __name__ == "__main__":
    import sys

    app1 = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_lr_4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app1.exec_())
