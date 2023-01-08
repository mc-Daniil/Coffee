import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Window(QMainWindow):
   def __init__(self):
       super(Window, self).__init__()
       uic.loadUi("main.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())