from tkinter.filedialog import Open
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
import interfaccia.enter as enter
import sys



class Utent(QDialog):

    def __init__(self, parent, utente):
        super(Utent,self).__init__(parent)
        loadUi('interfaccia/ui/utent.ui', self)
        self.setFixedSize(609, 498)
        self.setWindowTitle("B&B")
        self.utent.setText(utente)
        self.pushButton_2.clicked.connect(self.fun_exit)

    def fun_exit(self):
        self.close()
        self.parent().show()
