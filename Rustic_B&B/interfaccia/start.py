from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QWidget
from PyQt6.QtGui import QFont
from PyQt6.uic import loadUi
import interfaccia.enter as enter  
import interfaccia.register as register
import sys 

class Start(QMainWindow):

    def __init__(self):
        super(Start,self).__init__()
        loadUi('interfaccia/ui/start.ui', self)
        self.setFixedSize(571, 461)
        self.setWindowTitle("B&B")
        self.pushButton_3.clicked.connect(self.credit)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.fun_register)

    def fun_register(self):
        self.hide()
        reg = register.Register(self)
        reg.exec()

    def login(self):
        self.hide()
        log = enter.Enter(self)
        log.exec()

    def credit(self):
        dlg = QDialog()
        dlg.setGeometry(200,200,600,100)
        dlg.setFixedSize(600, 100)
        l = QLabel (dlg)
        l.setText("Develop by: Davide Nino Longobardi, Nunzio Boiano, Sebastiano Lamonica, Manuel Raffone Bartolomeo")
        l.setFont(QFont('Arial font', 10))
        l.move(0, 40)
        dlg.setWindowTitle("credits")
        dlg.exec()

def start():
    app = QApplication([])
    app.setStyle("fusion")
    window = Start()
    window.show()
    app.exec()
