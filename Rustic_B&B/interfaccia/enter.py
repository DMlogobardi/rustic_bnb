from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
import interfaccia.start as s 
import sys



class Enter(QDialog):

    def __init__(self, parent):
        super(Enter,self).__init__(parent)
        loadUi('interfaccia/ui/login.ui', self)
        self.setFixedSize(442, 292)
        self.setWindowTitle("B&B")
        self.confirm_2.clicked.connect(self.cancel)

    def cancel(self):
        self.close()
        self.parent().show()
