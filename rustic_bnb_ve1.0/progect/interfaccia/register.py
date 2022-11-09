from PyQt6.QtWidgets import QDialog, QLabel, QDateEdit, QButtonGroup 
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDate, QDateTime
from PyQt6.uic import loadUi
import Gestione_Database.Connesione_Database as db

class Register(QDialog):

    def __init__(self, parent):
        super(Register,self).__init__(parent)
        loadUi('interfaccia/ui/register.ui', self)
        self.setFixedSize(546, 352)
        self.setWindowTitle("B&B")
        d1 = QDateTime(1920, 1, 1, 10, 30)
        d2 = QDateTime.currentDateTime()
        self.dateEdit.setDateTimeRange(d1, d2)
        self.dateEdit.setDate(QDate.currentDate())
        self.bg = QButtonGroup()
        self.bg.addButton(self.female)
        self.bg.addButton(self.male)
        self.male.setChecked( True )
        self.cancel.clicked.connect(self.fun_cancel)
        self.confirm.clicked.connect(self.fun_confirm)
        
    def fun_confirm(self):
        #set dialog for information
        dlg = QDialog()
        dlg.setGeometry(100,100,100,50)
        dlg.setFixedSize(200, 100)
        l = QLabel (dlg)
        l.setFont(QFont('Arial font', 10))
        l.move(0, 40)
        dlg.setWindowTitle("credits")
        
        #I take the element
        if self.lineEdit.text().strip() != "" and self.lineEdit_2.text().strip() != "" and self.lineEdit_3.text().strip() != "":
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            c_n = self.lineEdit_3.text()
        else:
            l.setText("empty field")
            dlg.exec()
            
        birthday = self.dateEdit.date()
        birthday_D = birthday.toPyDate()
            
        if self.female.isChecked():
            gender = 'f'
        else:
            gender = 'm'
            
        utent = []
        utent.append(username)
        utent.append(password)
        utent.append(c_n)
        utent.append(birthday_D)
        utent.append(gender)
            
        try:
            ins = db.__insert_utente__(utent)
        except Exception as e:
            print(e)
            self.close()
            self.parent().show()

        if ins != 1:
            l.setText("the user is used")
            dlg.exec()
            self.close()
            self.parent().show()
        else:
            l.setText("successful")
            dlg.exec()
            self.close()
            self.parent().show()
          
    def fun_cancel(self):
        self.close()
        self.parent().show()
        