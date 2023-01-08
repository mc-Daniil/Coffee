import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Window(QMainWindow):
   def __init__(self):
       super(Window, self).__init__()
       uic.loadUi("main.ui", self)

       self.connection = sqlite3.connect("coffee.sqlite")
       res = self.connection.cursor().execute("SELECT * FROM coffee").fetchall()

       self.tableWidget.setColumnCount(7)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(res):
           self.tableWidget.setRowCount(
               self.tableWidget.rowCount() + 1)
           for j, elem in enumerate(row):
               self.tableWidget.setItem(
                   i, j, QTableWidgetItem(str(elem)))

       self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())