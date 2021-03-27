from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

def pgcd(x):
    a=fen.lab1.text()
    b=fen.lab2.text()
    fen2=loadUi("noti.ui")
    if (a and b)=='':
        print('Hello')
        QMessageBox.warning(fen, "Attention", "enter a number")
    else:
        a=int(a)
        b=int(b)
        while (a!=b):
            if a>b :
                a=a-b
            else:
                b=b-a
        fen.res.setText(str(a))

def unul():
    fen.res.setText('')
    fen.lab1.setText('')
    fen.lab2.setText('')

def execute():
    app=QApplication([])
    fen=loadUi("pgcd.ui")
    fen.show()
    fen.culc.clicked.connect(pgcd)
    fen.ann.clicked.connect(unul)
    app.exec_()
