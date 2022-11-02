from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
import Gestione_Database.Connesione_Database as db
import sys





class Admin(QDialog):

    def __init__(self, parent, utent):
        super(Admin,self).__init__(parent)
        loadUi('interfaccia/ui/admin.ui', self)
        self.setFixedSize(498, 583)
        self.setWindowTitle("B&B")
        self.utent.setText(utent)
        self.exit.clicked.connect(self.fun_exit)
        
    def fun_exit(self):
        self.close()
        self.parent().show()