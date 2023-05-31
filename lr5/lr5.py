# -*- coding: utf-8 -*-
import os
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QMessageBox
import geopandas as gpd
from geopy import Nominatim
from matplotlib import pyplot as plt
from shapely import Point, LineString


class Ui_lr_5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 380)
        MainWindow.setMinimumSize(QtCore.QSize(870, 380))
        MainWindow.setMaximumSize(QtCore.QSize(870, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 851, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 851, 61))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 110, 851, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 170, 591, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 851, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 21))
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

        self.pushButton_5.clicked.connect(self.add_to_list)
        self.pushButton_8.clicked.connect(self.save_geojson)
        self.pushButton_9.clicked.connect(self.open_in_browser)

        # Чтение данных из Excel-файла
        df = pd.read_excel('lr5/111.xlsx')

        # Добавление всех уникальных значений из столбца "Регион" в комбобокс и QLineEdit
        regions = df['Город'].unique()
        self.comboBox.addItems(regions)

        self.data = {'city': [], 'population': [], 'geometry': [], 'center': []}

        self.delete_file()

    def delete_file(self):
        if os.path.exists('lr5/cities.geojson'):
            os.remove('lr5/cities.geojson')
        else:
            pass

    def add_to_list(self):

        # Загрузить границы регионов
        regions = gpd.read_file('lr5/gg/gadm36_RUS_1.shp')

        # Ввести название города
        city_name = self.comboBox.currentText()

        # Получить координаты города
        geolocator = Nominatim(user_agent='myapp')
        location = geolocator.geocode(city_name)
        if location is None:
            self.message_output("Ошибка", f"Некорректное название города", QMessageBox.Critical)
            exit()
        lat, lon = location.latitude, location.longitude

        # Выделить границы области, содержащей город
        region = regions[regions.contains(Point(lon, lat))]
        if region.empty:
            self.message_output("Ошибка", f"Город не найден", QMessageBox.Critical)
            exit()

        # Получить координаты границы области
        region_geom = Point(lon, lat).buffer(0.05)  # Создание круга с радиусом 10

        self.add_data(self.data, city_name, self.lineEdit_3.text(), region_geom, (lon, lat))

        self.message_output("Информация", f"Город {city_name} успешно добавлен с список.", QMessageBox.Information)

    def save_geojson(self):

        gdf = gpd.GeoDataFrame(self.data, crs='EPSG:4326', geometry='geometry')

        if len(gdf) == 1:
            self.message_output("Ошибка", "Добавьте еще минимум 1 локацию!", QMessageBox.Critical)
        else:
            centroids = [Point(c) for c in gdf['center']]

            line = LineString([c.coords[0] for c in centroids])
            line_gdf = gpd.GeoDataFrame(geometry=[line], crs='EPSG:4326')

            geom_union = gdf['geometry'].unary_union
            cities = gdf['geometry']
            centroids = [p.centroid for p in cities]
            combined_gdf = gpd.GeoDataFrame(geometry=list(cities) + [line], crs='EPSG:4326')

            combined_gdf['city'] = gdf['city']
            combined_gdf['population'] = gdf['population']
            combined_gdf = combined_gdf[['city', 'population', 'geometry']]

            combined_gdf.to_file('lr5/cities.geojson', driver='GeoJSON', driveroptions={'keep_infinity': True})

            self.message_output("Информация", f"GeoJSON успешно создан", QMessageBox.Information)

            fig, ax = plt.subplots()
            combined_gdf.plot(ax=ax)
            line_gdf.plot(ax=ax, color='red')
            plt.show()

    def add_data(self, data, city, population, geometry, center):
        data['city'].append(city)
        data['population'].append(population)
        data['geometry'].append(geometry)
        data['center'].append(center)

    def updateCityComboBox(self, index):
        city = self.comboBox.currentText()
        if city == '':
            pass
        else:
            self.find_population_city(city)

    def find_population_city(self, city):
        df2 = pd.read_excel('lr5/dataRUS.xlsx')

        # Поиск данных по городу
        city_data = df2.loc[(df2["Название, город"] == city)]
        if len(city_data) == 0:
            self.message_output("Ошибка", f"Данные по городу {city} не найдены.", QMessageBox.Critical)
            self.comboBox.clear()
            self.comboBox.setText('0')
            return
        else:
            city_population = city_data.iloc[0, 3]
            self.comboBox.setText(f'{str(city_population)}')

    def message_output(self, settext, setInformativeText, setIconType):
        icon = QIcon('image/1.png')
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(icon))
        msg.setIcon(setIconType)
        msg.setText(f'<b>{settext}</b>')
        msg.setInformativeText(setInformativeText)
        msg.setWindowTitle('ЛР №5')
        msg.exec_()

    def open_in_browser(self):
        url = QUrl("https://geojson.io/")
        QDesktopServices.openUrl(url)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа № 5"))
        self.label.setText(_translate("MainWindow", "Задание:"))
        self.label_4.setText(_translate("MainWindow", "Создание пространственной базы данных на языке Python с\n"
"использованием библиотеки GEOPandas."))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить в список"))
        self.label_3.setText(_translate("MainWindow", "Город"))
        self.label_2.setText(_translate("MainWindow", "Население"))
        self.pushButton_8.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_9.setText(_translate("MainWindow", "Открыть сайт"))
        self.label_8.setText(_translate("MainWindow", "Работа с данными"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_lr_5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
