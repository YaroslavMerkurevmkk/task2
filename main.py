import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ellipse(QMainWindow):
    def __init__(self):
        super(Ellipse, self).__init__()
        uic.loadUi('Ui.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    el = Ellipse()
    el.show()
    sys.exit(app.exec())
