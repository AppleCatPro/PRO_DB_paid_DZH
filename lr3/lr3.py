# -*- coding: utf-8 -*-

import re
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QMessageBox
from matplotlib import pyplot as plt
from matplotlib.patches import RegularPolygon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 435)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 435))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 435))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 190, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 360, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 140, 1081, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 320, 111, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 240, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 360, 111, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 340, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 1081, 91))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1051, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 320, 111, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 360, 141, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(640, 340, 101, 31))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 240, 391, 31))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 190, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(890, 280, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(71, 240, 221, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 280, 391, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(640, 280, 221, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(750, 340, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(535, 160, 31, 241))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
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

        self.pushButton.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.start)
        self.pushButton_3.clicked.connect(self.data_view_fig_db)
        self.pushButton_4.clicked.connect(self.save_figure)

        conn = sqlite3.connect('db/home.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS figures
                                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                type TEXT,
                                                x REAL,
                                                y REAL,
                                                width REAL,
                                                sides REAL,
                                                height REAL,
                                                radius REAL,
                                                area REAL)''')
        conn.commit()

        self.figure_comboBox()

        validator = QIntValidator()

        # Установка валидатора на QLineEdit
        self.lineEdit.setValidator(validator)
        self.lineEdit_2.setValidator(validator)
        self.lineEdit_3.setValidator(validator)

    def start(self):
        lin1 = self.lineEdit_2.text()
        lin2 = self.lineEdit_3.text()
        type_f = self.comboBox.currentText()
        type_fig = (''.join(map(str, type_f)))

        if type_fig == 'Круг':
            self.label_3.setText('Радиус')
            self.label_6.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            if lin1 == '':
                self.message_output("Информация", f"Ошибка, проверьте заполненность полей!", QMessageBox.Critical)
            else:
                self.figure_type, self.x, self.y, self.width, self.height, self.sides, self.radius, self.area = Figures(
                    type_fig,
                    lin1,
                    lin2).create_circle()

        elif type_fig == 'Прямоугольник':
            self.label_3.setText('Ширина')
            self.label_6.setText('Высота')
            self.label_6.setEnabled(True)
            self.lineEdit_3.setEnabled(True)

            if lin1 == '' or lin2 == '' or lin2 == '0' or lin1 == '0':
                self.message_output("Информация", f"Ошибка, проверьте заполненность полей!", QMessageBox.Critical)
            else:
                self.figure_type, self.x, self.y, self.width, self.height, self.sides, self.radius, self.area = Figures(
                    type_fig,
                    lin1,
                    lin2).create_rectangle()

        elif type_fig == 'Многогранник':
            self.label_3.setText('Грани')
            self.label_6.setText('Длинна')
            self.label_6.setEnabled(True)
            self.lineEdit_3.setEnabled(True)

            if lin1 == '' or lin2 == '' or lin2 == '0' or lin1 == '0':
                self.message_output("Информация", f"Ошибка, проверьте заполненность полей!", QMessageBox.Critical)
            else:
                self.figure_type, self.x, self.y, self.width, self.height, self.sides, self.radius, self.area = Figures(
                    type_fig,
                    lin1,
                    lin2).create_polygon()

        else:
            self.message_output("Информация", f"Фигура не найдена!", QMessageBox.Critical)

    def save_figure(self):

        if self.figure_type == '' and self.x == '' and self.y == '' and self.width == '' and self.height == '' and self.sides == '' and self.radius == '' and self.area == '':
            self.message_output("Информация", f'Ошибка сохранения, фигура не была создана!', QMessageBox.Critical)
        else:
            conn = sqlite3.connect('db/home.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS figures
                                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        type TEXT,
                                        x REAL,
                                        y REAL,
                                        width REAL,
                                        sides REAL,
                                        height REAL,
                                        radius REAL,
                                        area REAL)''')
            conn.commit()

            # Сохранение фигуры в базе данных
            c.execute(
                "INSERT INTO figures (type, x, y, width, height, sides, radius, area) VALUES (?, ?, ?, ?,?, ?, ?, ?)",
                (self.figure_type, self.x, self.y, self.width, self.sides, self.height, self.radius, self.area))
            conn.commit()
            self.message_output("Информация", f'Фигура: "{self.figure_type}" сохранена в Базе данных.',
                                QMessageBox.Information)
            self.figure_comboBox()
            self.label_10.setText(f'Введите ID:')
            conn.close()

    def delete_data(self):
        text = self.lineEdit.text()
        if not text:
            self.message_output("Ошибка", "Пустое поле!", QMessageBox.Critical)
        else:
            try:
                db = sqlite3.connect('db/home.db')

                c = db.cursor()

                # разделить строку на список по запятой, пробелу и любым другим символам-разделителям
                id_list = re.split('[,\s]+', text)
                id_list = [x.strip() for x in id_list]  # удалить лишние пробелы

                for id in id_list:
                    c.execute(f"SELECT id FROM figures WHERE id ={id}")

                    if c.fetchone() is None:
                        self.message_output("Ошибка", f"Такой записи {id} нет!", QMessageBox.Critical)
                    else:
                        c.execute(f"DELETE FROM figures WHERE id = {id};")
                        self.message_output("Успешно", f"Запись {id} успешно удалена!", QMessageBox.Information)
                db.commit()

                self.lineEdit.setText('')
                self.label_10.setText(f'Введите ID:')

                self.figure_comboBox()

            except Exception as _ex:
                self.message_output("Ошибка", f"Ошибка при работе с SQLite3 {_ex}", QMessageBox.Critical)
            finally:
                if db:
                    db.close()

    def data_view_fig_db(self):
        type_f = self.comboBox_2.currentText()

        elements = type_f.split(' \\ ')
        first_element = elements[0]
        split_elements = first_element.split('=')
        id_value = split_elements[1].strip()

        db = sqlite3.connect('db/home.db')
        cursor = db.cursor()
        cursor = cursor
        cursor.execute(f"""SELECT * FROM figures WHERE id ={id_value}""")
        sql = cursor.fetchall()
        address = []
        for i in sql:
            address.append(i)

        id, figure_type, x, y, width, sides, height, radius, area = address[0]
        self.label_10.setText(f'id = {id}')
        self.view_fig_db(figure_type, x, y, width, sides, height, radius)

    def view_fig_db(self, figure_type, x, y, width, height, sides, radius):

        if figure_type == 'Прямоугольник':
            plt.figure()
            plt.gca().add_patch(plt.Rectangle((x, y), width, height, edgecolor='black', linewidth=2))
            plt.gca().set_aspect('equal', 'box')
            plt.gca().set_xlim(x, x + width)
            plt.gca().set_ylim(y, y + height)
            plt.show()
        elif figure_type == 'Круг':
            plt.figure()
            plt.gca().add_patch(plt.Circle((x + radius, y + radius), radius, edgecolor='black', linewidth=2))
            plt.gca().set_aspect('equal', 'box')
            plt.gca().set_xlim(x, x + 2 * radius)
            plt.gca().set_ylim(y, y + 2 * radius)
            plt.show()
        elif figure_type == 'Многогранник':
            sides1 = sides
            radius1 = radius
            width1 = radius1 * 2
            height1 = radius1 * 2

            plt.figure()
            polygon = RegularPolygon((x + radius1, y + radius1), numVertices=sides1, radius=radius1, edgecolor='black',
                                     linewidth=2)
            plt.gca().add_patch(polygon)
            plt.gca().set_aspect('equal', 'box')
            plt.gca().set_xlim(x, x + width1)
            plt.gca().set_ylim(y, y + height1)
            plt.show()
        else:
            self.message_output("Информация", f"Фигура не найдена!", QMessageBox.Critical)

    def figure_comboBox(self):

        self.comboBox_2.clear()
        self.label_10.setText(f'Введите ID:')

        db = sqlite3.connect('image/1.png')
        cursor = db.cursor()
        cursor = cursor
        cursor.execute("""SELECT id, type, area FROM figures""")
        sql = cursor.fetchall()
        address = []
        for i in sql:
            address.append(f'id = {i[0]} \ {i[1]} \ {i[2]}')
        self.comboBox_2.addItems(address)

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('ЛР №3')
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа № 3"))
        self.label_7.setText(_translate("MainWindow", "Работа с фигурами"))
        self.label_3.setText(_translate("MainWindow", "Ширина"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать фигуру"))
        self.label_6.setText(_translate("MainWindow", "Высота"))
        self.pushButton.setText(_translate("MainWindow", "Удалить из бд"))
        self.label_4.setText(_translate("MainWindow",
                                        "Напишите программу, которая выводит на экран различные геометрические фигуры, сохраняет их в базе данных и \n"
                                        "предоставляет графический интерфейс для взаимодействия с пользователем."))
        self.label.setText(_translate("MainWindow", "Задание:"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить фигуру"))
        self.label_10.setText(_translate("MainWindow", "Введите ID:"))
        self.label_9.setText(_translate("MainWindow", "Сохраненные фигуры:"))
        self.label_8.setText(_translate("MainWindow", "Работа с Базой данных"))
        self.pushButton_3.setText(_translate("MainWindow", "Выбрать фигуру"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Круг"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ромб"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Квадрат"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Прямоугольник"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Многогранник"))
        self.label_2.setText(_translate("MainWindow", "Введите данные для создания фигур:"))


class Figures:

    def __init__(self, type_figures, lineedit1, lineedit2):
        super().__init__()

        self.type_fig = type_figures
        self.lineedit1 = int(lineedit1)
        if lineedit2:
            self.lineedit2 = int(lineedit2)

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('ЛР №3')
        msg.exec_()

    def create_rectangle(self):
        # Создание прямоугольника и сохранение его в базе данных
        figure_type = "Прямоугольник"
        sides = '-'
        radius = '-'
        x = 0
        y = 0
        width = float(self.lineedit1)
        height = float(self.lineedit2)
        area = width * height
        area_new = round(area, 2)
        self.message_output("Информация", f"Прямоугольник создан. Площадь: {area_new}", QMessageBox.Information)

        # Отображение прямоугольника с помощью matplotlib
        plt.figure()
        plt.gca().add_patch(plt.Rectangle((x, y), width, height, edgecolor='black', linewidth=2))
        plt.gca().set_aspect('equal', 'box')
        plt.gca().set_xlim(x, x + width)
        plt.gca().set_ylim(y, y + height)
        plt.show()

        return figure_type, x, y, width, height, sides, radius, area_new

    def create_circle(self):
        # Создание окружности и сохранение ее в базе данных
        figure_type = "Круг"
        x = 0
        y = 0
        sides = '-'
        width = '-'
        height = '-'
        radius = float(self.lineedit1)
        area = 3.14159 * radius * radius
        area_new = round(area, 2)
        self.message_output("Информация", f"Окружность создана. Площадь: {area_new}", QMessageBox.Information)

        # Отображение окружности с помощью matplotlib
        plt.figure()
        plt.gca().add_patch(plt.Circle((x + radius, y + radius), radius, edgecolor='black', linewidth=2))
        plt.gca().set_aspect('equal', 'box')
        plt.gca().set_xlim(x, x + 2 * radius)
        plt.gca().set_ylim(y, y + 2 * radius)
        plt.show()

        return figure_type, x, y, width, height, sides, radius, area_new

    def create_polygon(self):
        figure_type = "Многогранник"
        x = 0
        y = 0
        sides = int(self.lineedit1)
        radius = float(self.lineedit2)
        width = radius * 2
        height = radius * 2
        area = (sides * radius ** 2 * (3 ** 0.5)) / 4
        area_new = round(area, 2)
        self.message_output("Информация", f"Многогранник создан. Площадь: {area_new}", QMessageBox.Information)

        # Отображение многогранника с помощью matplotlib
        plt.figure()
        polygon = RegularPolygon((x + radius, y + radius), numVertices=sides, radius=radius, edgecolor='black',
                                 linewidth=2)
        plt.gca().add_patch(polygon)
        plt.gca().set_aspect('equal', 'box')
        plt.gca().set_xlim(x, x + width)
        plt.gca().set_ylim(y, y + height)
        plt.show()

        return figure_type, x, y, width, height, sides, radius, area_new


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
