import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from draw_bey import *
from draw_toon import *
from draw_bob import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        self.w = Simple_drawing_window4()
        self.w.show()

        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(50,200),QPoint(150,200) , QPoint(100,400),
        ])
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()


def main():
    app = QApplication(sys.argv)
        
    w = Simple_drawing_window()
    w.show()


    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
