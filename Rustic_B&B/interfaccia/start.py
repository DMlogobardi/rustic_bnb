from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Start(QMainWindow):
    def __init__(self):
        super(Start,self).__init__()
        self.setGeometry(200,200,400,360)
        self.setWindowTitle("B&B")
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("siii")
        self.label.move(200,10)
        self.label.setAlignment(Qt.AlignCenter)

        self.log = QPushButton(self)
        self.log.setText("Login")
        self.log.move(10,200)
        #self.log.clicked.connect(self.clicked)

        self.reg = QPushButton(self)
        self.reg.setText("Register")
        self.reg.move(10,240)
        #self.reg.clicked.connect(self.clicked)

        self.cred = QPushButton(self)
        self.cred.setText("Crediti")
        self.cred.move(10,280)
        #self.cred.clicked.connect(self.clicked)

        self.esc = QPushButton(self)
        self.esc.setText("Close")
        self.esc.move(10,320)
        self.esc.clicked.connect(self.close)

    def close(self):
            self.close()

def start():
    app = QApplication([])
    app.setStyle("fusion")
    window = Start()

    window.show()
    app.exec_()

