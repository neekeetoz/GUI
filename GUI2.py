from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QPushButton
from PyQt5.QtCore import QSize, pyqtSignal, QObject
from PyQt5 import QtGui, QtCore, QtWidgets

class Ruble(QObject):
    setRuble = pyqtSignal(int)

    def __init__(self, r):
        super().__init__()
        self.rub = r

    def change(self, n):
        if n > 0:
            self.rub = self.rub * 2*n
        else:
            self.rub = self.rub / (2*(-n))

    def getRuble(self):
        return str('{:.6f}'.format(self.rub))


class Dollar(QObject):
    setDollar = pyqtSignal(int)

    def __init__(self, d):
        super().__init__()
        self.dollar = d

    def change(self,n):
        if n > 0:
            self.dollar = self.dollar * 2*n
        else:
            self.dollar = self.dollar / (2*(-n))

    def getDollar(self):
        return str('{:.6f}'.format(self.dollar))


class Oil():
    def __init__(self, o):
        self.oil = o

    def getOil(self):
        return str(self.oil)

    def setOil(self, o):
        self.oil = o


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        pixmap = QtGui.QPixmap("img.jpg").scaled(
            700, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)

        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        self.setPalette(pal)
        self.setMask(pixmap.mask())

        self.oil = Oil(1)
        self.rub = Ruble(97.68 * 61.24)
        self.rub.setRuble.connect(self.rub.change)
        self.dollar = Dollar(97.68)
        self.dollar.setDollar.connect(self.dollar.change)

        self.setWindowTitle("Second lab")
        self.setFixedSize(QSize(300, 400))


        self.label1 = QLabel(self)
        self.label1.setText("<font color=red>Нефть</font>")
        self.label1.move(20, 50)


        self.label2 = QLabel(self)
        self.label2.setText("<font color=yellow>Рубли</font>")
        self.label2.move(20, 100)

        self.label3 = QLabel(self)
        self.label3.setText("<font color=green>Доллары</font>")
        self.label3.resize(200, 30)
        self.label3.move(20, 150)

        self.fg1 = QLineEdit(self)
        self.fg1.move(160, 50)
        self.fg1.setText(self.oil.getOil())

        self.fg2 = QLineEdit(self)
        self.fg2.move(160, 100)
        self.fg2.setText(self.rub.getRuble())
        self.fg2.setReadOnly(True)

        self.fg3 = QLineEdit(self)
        self.fg3.move(160, 150)
        self.fg3.setText(self.dollar.getDollar())
        self.fg3.setReadOnly(True)

        self.button = QPushButton("Посчитать ", self)
        self.button.resize(100, 50)
        self.button.move(100, 250)
        self.button.clicked.connect(self.clicked)


    def clicked(self):
        if(float(self.fg1.text())<=0):
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('Значение должно быть больше 0')
            self.fg1.setText(self.oil.getOil())
        elif(float(self.fg1.text())>float(self.oil.getOil())):
            f=float(self.fg1.text())-float(self.oil.getOil())
            self.rub.setRuble.emit(-1*(f))
            self.fg2.setText(self.rub.getRuble())

            self.dollar.setDollar.emit(f)
            self.fg3.setText(self.dollar.getDollar())
        elif(float(self.fg1.text())<float(self.oil.getOil())):
            f = -float(self.fg1.text()) + float(self.oil.getOil())
            self.dollar.setDollar.emit(-1*f)
            self.fg3.setText(self.dollar.getDollar())

            self.rub.setRuble.emit(f)
            self.fg2.setText(self.rub.getRuble())


        self.oil.setOil(self.fg1.text())

app = QApplication([])
app.setStyleSheet("QLabel{font-size: 16pt;}")

window = MainWindow()
window.show()

app.exec()
