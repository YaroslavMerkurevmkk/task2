import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from Ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ellipse(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ellipse, self).__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(100, 100, randint(50, 500), randint(50, 500))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    el = Ellipse()
    el.show()
    sys.exit(app.exec())
