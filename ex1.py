import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)

    l1.setText("Hello World")
    l2.setPixmap(QtGui.QPixmap("Charlie-brown.png"))

    w.setWindowTitle("Marius_test")
    w.setGeometry(100, 100, 300, 300)
    l1.move(130, 20)
    l2.move(130, 80)
    w.show()
    sys.exit(app.exec_())

window()