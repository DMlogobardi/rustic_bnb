from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QWidget
from PyQt6.uic import loadUi
import interfaccia.enter as enter
import Gestione_Database.Connesione_Database as db
from PyQt6.QtCore import QDate

class Utent(QDialog):

    def __init__(self, parent, utente):
        super(Utent,self).__init__(parent)
        loadUi('interfaccia/ui/utent.ui', self)
        self.setFixedSize(609, 498)
        self.setWindowTitle("B&B")
        self.utent.setText(utente)
        self.vbox = QVBoxLayout()
        self.container = QWidget()
        self.vbox_2 = QVBoxLayout()
        self.container_2 = QWidget()
        self.day_cost = ""
        self.prenotation = []
        
        self.__list_prenotation__()
        self.__list_Discount__()
        
        self.dateEdit.setMinimumDate(QDate.currentDate())
        self.dateEdit_2.setMinimumDate(QDate.currentDate())
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())
        self.container.setLayout(self.vbox)
        self.container_2.setLayout(self.vbox_2)
        self.scrollArea.setWidget(self.container)
        self.scrollArea_2.setWidget(self.container_2)
        
        self.pushButton_2.clicked.connect(self.fun_exit)
        self.update.clicked.connect(self.__list_prenotation__)
        self.update_2.clicked.connect(self.__list_Discount__)
        self.pre.clicked.connect(self.__preventive__)
        self.pushButton.clicked.connect(self.__prenotation__)
        
    def __preventive__(self):
        list = db.__discount__()
        data1 = self.dateEdit.date()
        data2 = self.dateEdit_2.date()
        data = QDate(data1)
        datap = QDate(data2)
        
        if data1 < data2:
            for l in list:
                if l[0] == 1:
                    d_c = l[3]
                        
                if data1 >= l[1] and data2 <= l[2]:
                    self.day_cost = l[3]
                    forDay = data.daysTo(datap)
                    cost = float(self.day_cost) * forDay
                        
                    self.price.setText(cost.__str__())
                    return 0
                
                forDay = data.daysTo(datap)
                cost = d_c * forDay
                            
                self.price.setText(cost.__str__())
                return 0
        else: 
            self.price.setText("error date")
        
    def __prenotation__(self):
        try:
            list = db.__discount__()
            data1 = self.dateEdit.date()
            data2 = self.dateEdit_2.date()
            data = QDate(data1)
            datap = QDate(data2)
            data1 = data1.toPyDate()
            data2 = data2.toPyDate()
        
            if data1 < data2:
                for l in list:
                    if l[0] == 1:
                        d_c = l[3]
                        
                    if data1 >= l[1] and data2 <= l[2]:
                        self.day_cost = l[3]
                        forDay = data.daysTo(datap)
                        cost = float(self.day_cost) * forDay
                        discount = l[0]
                         
                        ut = []
                        ut.append(self.utent.text())
                        utent = db.__utent__(ut).__str__()
                        utent = utent.replace("[", " ").replace("(", " ").replace(","," ").replace(")"," ").replace("]"," ").strip()
                        
                        prenotation = []
                        prenotation.append(utent)
                        prenotation.append(discount)
                        prenotation.append(data1)
                        prenotation.append(data2)
                        prenotation.append(cost)
                        
                        lns = db.__add_prenotation__(prenotation)
                        
                        if lns == 1:
                            self.price.setText("successful")
                        else:
                            self.price.setText("PRENOTATON EXIST")
                            print(lns)
                        return 0
                    else:
                        forDay = data.daysTo(datap)
                        cost = d_c * forDay
                        discount = l[0]
                             
                        ut = []
                        ut.append(self.utent.text())
                        utent = db.__utent__(ut).__str__()
                        utent = utent.replace("[", " ").replace("(", " ").replace(","," ").replace(")"," ").replace("]"," ").strip()
                            
                        prenotation = []
                        prenotation.append(utent)
                        prenotation.append(discount)
                        prenotation.append(data1)
                        prenotation.append(data2)
                        prenotation.append(cost)
                            
                        lns = db.__add_prenotation__(prenotation)
                            
                        if lns == 1:
                            self.price.setText("successful")
                        else:
                            self.price.setText("PRENOTATON EXIST")
                            print(lns)
                        return 0    
                        
            else: 
                self.price.setText("error date")
        except Exception as e:
            print(e)
        
    def __list_Discount__(self):
        for i in reversed(range(self.vbox_2.count())): 
           self.vbox_2.itemAt(i).widget().setParent(None)
           
        list = db.__discount__()
        
    
        if list.__str__() != "[]":
            for l in list:
                id = l[0]
                data_in = l[1]
                data_out = l[2]
                prezzo = l[3]
                n_persone = l[4]
                    
                discount = f"""{id}: For: {data_in}, to: {data_out}, price: {prezzo}, min persone: {n_persone}"""
                    
                label = QLabel()
                label.setText(discount)
                self.vbox_2.addWidget(label)  

    def __list_prenotation__(self):
        for i in reversed(range(self.vbox.count())): 
            self.vbox.itemAt(i).widget().setParent(None)
            
        utent = []
        utent.append(self.utent.text())
            
        list = db.__utent_prenotation__(utent)
        
        if list.__str__() != "[]":
            for l in list:
                id = l[0]
                data_checkin = l[3]
                data_checkout = l[4]
                cost = l[5]
                    
                prenotation = f"""{id}: For: {data_checkin}, to: {data_checkout}, price: {cost}"""
                    
                label = QLabel()
                label.setText(prenotation)
                self.vbox.addWidget(label)

    def fun_exit(self):
        self.close()
        self.parent().show()
