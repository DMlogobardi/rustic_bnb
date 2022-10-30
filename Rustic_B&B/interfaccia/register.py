from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
import sys



class Register(QDialog):

    def __init__(self, parent):
        super(Register,self).__init__(parent)
        loadUi('interfaccia/ui/register.ui', self)
        self.setFixedSize(546, 352)
        self.setWindowTitle("B&B")
        self.cancel.clicked.connect(self.fun_cancel)

    def fun_cancel(self):
        self.close()
        self.parent().show()
