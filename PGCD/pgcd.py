from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *



def pgcd():
    a=int(fen.nb1.text())
    b=int(fen.nb2.text())
    while (a != b):
        if (a>b):
            a=a-b
        else:
            b=b-a
    fen.res.setText("  "+str(a))
def effacer():
    fen.nb1.setText("")
    fen.nb2.setText("")
    fen.res.setText("")

def ouvrir_pgcd():
    fen.show()

def fermer_1():
    fen.close()
    
app=QApplication([])
fen=loadUi("pgcd.ui")
pp=loadUi("menu.ui")

fen.effacer.clicked.connect(effacer)
fen.calculer.clicked.connect(pgcd)
fen.fermer.clicked.connect(fermer_1)
pp.pgcd.clicked.connect(ouvrir_pgcd)
#pp.ppcm.clicked.connect(ouvrir_ppcm)


pp.show()
