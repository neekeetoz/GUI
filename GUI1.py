import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor

class Dialog(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(255, 255, 255) # белый цвет по умолчанию
        self.btn = QPushButton('Замена цвета', self) # надпись на кнопке
        self.btn.move(20, 60) # положение кнопки
        self.btn.clicked.connect(self.Dialog_window) # при нажатии будет диалоговое окошко

        # параметры цветного прямоугольника
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 30, 100, 100)

        # параметры рамки основного окна
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Выбор цвета')
        self.show()

    def Dialog_window(self):
        col = QColorDialog.getColor() # диалоговое окно с выбором цвета
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dialog()
    sys.exit(app.exec_())