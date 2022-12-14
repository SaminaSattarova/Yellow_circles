import random

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor
from PyQt5 import uic
import sys
from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('UI.ui', self)
        self.pushButton.setText('Нарисовать')
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.setText('Стоп')
        self.pushButton_2.clicked.connect(self.stop)
        self.paint_bool = False

    def run(self):
        self.paint_bool = True

    def paintEvent(self, event):
        if self.paint_bool:
            self.qp = QPainter(self)
            self.qp.begin(self)
            self.draw()
            self.qp.end()
            self.update()

    def draw(self):
        d = random.randint(10, 100)
        self.qp.setPen(QPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 8, Qt.SolidLine))
        self.qp.drawEllipse(random.randint(10, 450), random.randint(10, 450), d, d)

    def stop(self):
        self.paint_bool = False


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exit(app.exec())