from PyQt6.QtWidgets import QDialog, QLineEdit
from PyQt6.uic import loadUi
import interfaccia.utente as utent
import interfaccia.admin as admin
import Gestione_Database.Connesione_Database as db
import sys





class Enter(QDialog):

    def __init__(self, parent):
        super(Enter,self).__init__(parent)
        loadUi('interfaccia/ui/login.ui', self)
        self.setFixedSize(442, 292)
        self.setWindowTitle("B&B")
        try:
            self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        except Exception as e:
            print(e) 
        self.confirm_2.clicked.connect(self.fun_cancel)
        self.confirm.clicked.connect(self.fun_confirm)
       
    def fun_confirm(self):
        campi = []
        campi.append(self.lineEdit.text())
        campi.append(self.lineEdit_2.text())
        col = db.__controllo_utent__(campi).__str__()
        try:
            if col == "[]":
                self.lineEdit.setText("User don't exist or you have miss password or username")
                self.lineEdit_2.clear()
            elif col[3] == "n":
                self.close()
                user = utent.Utent(self.parent(), campi[0])
                user.exec()
            else:
                self.close()
                adm = admin.Admin(self.parent(), campi[0])
                adm.exec()
        except Exception as e:
            print(e)

    def fun_cancel(self):
        self.close()
        self.parent().show()
