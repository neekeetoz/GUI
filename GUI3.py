import sys, psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtWidgets

class ld_data(object):

    def ld_labels(cursor, tableWidget):
        tableWidget.setColumnCount(5)
        row_list = ld_data.load_name_tables(cursor)
        tableWidget.setHorizontalHeaderLabels([row_list[0], row_list[1], row_list[2], row_list[3], row_list[4]])

    def ld_data_main_window(cursor, tableWidget):
        sql = "SELECT * FROM gui_table"
        cursor.execute(sql)  # type: ignore
        result = cursor.fetchall()  # type: ignore
        row_count = 0
        list = []
        for row in result:
            list = []
            for elem in row:
                list.append(elem)
            tableWidget.insertRow(row_count)
            for i in range(0, 5):
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, list[i])  # type: ignore
                tableWidget.setItem(row_count, i, item)
                tableWidget.resizeColumnToContents(i)
            tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(list[2])))  # type: ignore
            tableWidget.resizeColumnToContents(2)
        tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)  # type: ignore

    def load_name_tables(cursor):
        sql1 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'gui_table'"
        cursor.execute(sql1)  # type: ignore
        result_header = cursor.fetchall()  # type: ignore
        row_list = []
        for row in result_header:
            for elem in row:
                row_list.append(elem)
        return row_list

    def ld_data_add_window(cursor, tableWidget, column_name):
        sql = "SELECT " + column_name + " FROM gui_table"
        cursor.execute(sql)  # type: ignore
        result = cursor.fetchall()  # type: ignore
        row_count = 0
        list = []
        for row in result:
            list = []
            for elem in row:
                list.append(elem)
            tableWidget.insertRow(row_count)
            if (column_name == 'Возраст'):
                tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(list[0])))  # type: ignore
            else:
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, list[0])  # type: ignore
                tableWidget.setItem(row_count, 0, item)
            tableWidget.resizeColumnToContents(0)
        if (column_name == 'id'):
            tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)  # type: ignore

class Ui_MainWindow(object):
    global conn, cursor
    conn = psycopg2.connect(dbname='postgres1', user='postgres', password='5432', host='localhost')
    cursor = conn.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.execut_query)
        self.gridLayout_3.addWidget(self.pushButton, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget_2, 2, 0, 1, 6)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_connection = QtWidgets.QAction(MainWindow)
        self.actionOpen_connection.setObjectName("actionOpen_connection")
        self.actionOpen_connection.triggered.connect(self.open_connect)
        self.actionClose_connection = QtWidgets.QAction(MainWindow)
        self.actionClose_connection.setObjectName("actionClose_connection")
        self.actionClose_connection.triggered.connect(self.close_connect)
        self.menuMenu.addAction(self.actionOpen_connection)
        self.menuMenu.addAction(self.actionClose_connection)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit_click(self):
        self.close_connect()
        quit()

    def open_connect(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        conn = psycopg2.connect(dbname='postgres1', user='postgres', password='5432', host='localhost')
        cursor = conn.cursor()
        ld_data.ld_labels(cursor, self.tableWidget)
        ld_data.ld_data_main_window(cursor, self.tableWidget)
        self.comboBox.addItems(ld_data.load_name_tables(cursor))

    def close_connect(self):
        conn = psycopg2.connect(dbname='postgres1', user='postgres', password='5432', host='localhost')
        conn.close()
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.clear()
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.comboBox.clear()

    def execut_query(self):
        if (self.comboBox.currentText() != ""):
            self.tableWidget_2.clear()
            self.tableWidget_2.setColumnCount(1)
            self.tableWidget_2.setRowCount(0)
            conn = psycopg2.connect(dbname='postgres1', user='postgres', password='5432', host='localhost')
            cursor = conn.cursor()
            ld_data.ld_data_add_window(cursor, self.tableWidget_2, self.comboBox.currentText())
        else:
            msg_text = 'Соединение с БД не установлено'
            ld_data.show_message(msg_text, QMessageBox.Warning)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр базы данных"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Страница 1"))
        self.pushButton.setText(_translate("MainWindow", "Выполнить запрос"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Страница 2"))
        self.menuMenu.setTitle(_translate("MainWindow", "Меню"))
        self.actionOpen_connection.setText(_translate("MainWindow", "Установить соединение с БД"))
        self.actionClose_connection.setText(_translate("MainWindow", "Закрыть соединение с БД"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
