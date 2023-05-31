# -*- coding: utf-8 -*-
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from add_courier import Ui_Add_Courier
from add_customer import Ui_Add_Customer
from add_delivery import Ui_Add_Delivery


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 600)
        MainWindow.setMinimumSize(QtCore.QSize(790, 600))
        MainWindow.setMaximumSize(QtCore.QSize(790, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 9, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 781, 91))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 150, 781, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 250, 771, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 220, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Загружаем иконку из файла
        icon = QIcon('image/1.png')
        # Устанавливаем иконку для главного окна
        MainWindow.setWindowIcon(QtGui.QIcon(icon))

        self.pushButton.clicked.connect(self.view_data_new)

        self.action.triggered.connect(self.Add_Courier)
        self.action_2.triggered.connect(self.Add_Customer)
        self.action_3.triggered.connect(self.Add_Delivery)

    def Add_Courier(self):
        self.add_courier_v = QtWidgets.QMainWindow()
        self.ui = Ui_Add_Courier()
        self.ui.setupUi(self.add_courier_v)
        self.add_courier_v.show()

    def Add_Customer(self):
        self.add_customer_v = QtWidgets.QMainWindow()
        self.ui = Ui_Add_Customer()
        self.ui.setupUi(self.add_customer_v)
        self.add_customer_v.show()

    def Add_Delivery(self):
        self.add_delivery_v = QtWidgets.QMainWindow()
        self.ui = Ui_Add_Delivery()
        self.ui.setupUi(self.add_delivery_v)
        self.add_delivery_v.show()

    def close_project(self):
        QCoreApplication.quit()

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('ЛР №1-2')
        msg.exec_()

    def view_data_new(self):
        xxx = self.comboBox.currentText()

        if xxx == 'Курьеры':
            xxx1 = 'courier'
        elif xxx == 'Клиенты':
            xxx1 = 'customer'
        elif xxx == 'Доставка':
            xxx1 = 'delivery'
        else:
            self.message_output("Информация", f'Таблица не найдена!', QMessageBox.Critical)

        ggg = (''.join(map(str, xxx1)))

        try:
            db = sqlite3.connect('db/home.db')
            cursor = db.cursor()

            cursor.execute(f"""SELECT * FROM {ggg}""")
            result = cursor.fetchall()

            if not result:
                self.message_output("Информация", f'Таблица {ggg} не содержит записей!', QMessageBox.Critical)
            else:
                self.tableWidget.setRowCount(len(result))
                self.tableWidget.setColumnCount(len(result[0]))

                column_names = [d[0] for d in cursor.description]
                global row_dict
                for row in result:
                    row_dict = {column_names[index]: value for (index, value) in enumerate(row)}
                self.tableWidget.setHorizontalHeaderLabels(row_dict)

                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

                db.close()
        except sqlite3.Error as error:
            self.message_output("Информация", f'Ошибка при работе с SQLite: {error}', QMessageBox.Critical)

        finally:
            if db:
                db.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа № 1 - 2"))
        self.label.setText(_translate("MainWindow", "Задание:"))
        self.label_4.setText(_translate("MainWindow", "Реализовать базу данных для службы курьерской доставки. \n"
"3 таблицы: курьеры, клиенты, доставка."))
        self.label_8.setText(_translate("MainWindow", "Работа с Базой Данных"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Курьеры"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Клиенты"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Доставка"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать"))
        self.menu.setTitle(_translate("MainWindow", "Добавить"))
        self.action.setText(_translate("MainWindow", "Курьер"))
        self.action_2.setText(_translate("MainWindow", "Клиент"))
        self.action_3.setText(_translate("MainWindow", "Доставка"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
