import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window4(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing 4")
        self.rabbit = QPixmap("images/rabbit.png")

        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,120))
        p.drawPolygon([
            QPoint(120,120) , QPoint(0,50) ,QPoint(50,50), QPoint(-50,-40)
        ])
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()