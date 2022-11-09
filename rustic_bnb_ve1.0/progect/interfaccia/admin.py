from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QWidget, QFrame,\
    QPushButton
from PyQt6.QtCore import QDate, QEvent
from PyQt6.uic import loadUi
from PyQt6.QtGui import QMouseEvent, QSinglePointEvent
import Gestione_Database.Connesione_Database as db

class Admin(QDialog):

    def __init__(self, parent, utent):
        super(Admin,self).__init__(parent)
        loadUi('interfaccia/ui/admin.ui', self)
        self.setFixedSize(498, 583)
        self.setWindowTitle("B&B")
        self.utent.setText(utent)
        self.vbox = QVBoxLayout()
        self.container = QWidget()
        self.vbox_2 = QVBoxLayout()
        self.container_2 = QWidget()
        self.id = ""
        
        self.__list_Discount__()
        self.__list_prenotation__()
        
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())
        self.enter.setText(self.__guadagno_label__())
        self.container.setLayout(self.vbox)
        self.container_2.setLayout(self.vbox_2)
        self.scrollArea_3.setWidget(self.container)
        self.scrollArea_2.setWidget(self.container_2)
        
        self.exit.clicked.connect(self.fun_exit)
        self.add.clicked.connect(self.fun_add)
        self.addDiscount.clicked.connect(self.__fun_add_discount__)
        self.update.clicked.connect(self.__list_prenotation__)
        self.update_1.clicked.connect(self.__list_Discount__)
        self.select.clicked.connect(self.__select__)
        self.remove.clicked.connect(self.__delete__)
        self.modify.clicked.connect(self.__modify__)
        
    def __modify__(self):
        try:
            data1 = self.dateEdit.date()  
            data2 = self.dateEdit_2.date()
            data1 = data1.toPyDate()
            data2 = data2.toPyDate()
            
            if data1 < data2 and data2 >= QDate.currentDate():
                mod = []
                mod.append(data1)
                mod.append(data2)
                mod.append(self.lineEdit_2.text())
                mod.append(self.id.__str__())
                
                ins = db.__mod__(mod)
                
                if ins == 1:
                    self.dateEdit.setDate(QDate.currentDate())
                    self.dateEdit_2.setDate(QDate.currentDate())
                    self.lineEdit_3.setText("")
                    self.lineEdit_2.setText("successful")
                else:
                    print(ins)
                    self.lineEdit_2.setText("error")
            else:
                self.dateEdit.setDate(QDate.currentDate())
                self.dateEdit_2.setDate(QDate.currentDate())
                self.lineEdit_3.setText("")
                self.lineEdit_2.setText("you don't have Delorian")
        except Exception as e:
            print(e)
        
    def __delete__(self):
        if self.id != 1:
            list = []
            list.append(self.id)
            ins = db.__delete__(list)
            
            if ins == 1:
                self.dateEdit.setDate(QDate.currentDate())
                self.dateEdit_2.setDate(QDate.currentDate())
                self.lineEdit_3.setText("")
                self.lineEdit_2.setText("successful")
            else:
                self.lineEdit_2.setText("id not exist")
        else:
            self.lineEdit_2.setText("id not exist")
        
    def __select__(self):
        self.id = self.lineEdit_3.text().strip()
        
        try:
            int(self.id)
            if id != "":
                element = db.__discount__()
                if element.__str__() != "[]":
                    for e in element:
                        if e[0].__str__() == self.id.__str__():
                            data1 = e[1]
                            data2 = e[2]
                            cost = e[3].__str__()
                            
                            self.dateEdit.setDate(data1) 
                            self.dateEdit_2.setDate(data2) 
                            self.lineEdit_2.setText(cost)
                    
                else:
                   self.lineEdit_3.setText("id not exist")
        except Exception as e:
            self.lineEdit_3.setText("mmmm")
            print(e)
        
    def __list_prenotation__(self):
        for i in reversed(range(self.vbox_2.count())): 
            self.vbox_2.itemAt(i).widget().setParent(None)
            
        list = db.__prenotation__()
        
        if list.__str__() != "[]":
            for l in list:
                label = QLabel(l.__str__())
                self.vbox_2.addWidget(label)
        
    def __list_Discount__(self):
        for i in reversed(range(self.vbox.count())): 
           self.vbox.itemAt(i).widget().setParent(None)
           
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
                self.vbox.addWidget(label)  
        
    def __fun_add_discount__(self):
        date1 = self.dateEdit.date()
        date2 = self.dateEdit_2.date()
        date_in = date1.toPyDate()
        date_out = date2.toPyDate()
        
        if date_in < date_out:
            if self.lineEdit_2.text().strip() != "":
                try:
                    if float(self.lineEdit_2.text().strip()) > 0 and float(self.lineEdit_2.text().strip()) < 500: 
                        discount = []
                        discount.append(date_in)
                        discount.append(date_out)
                        float(self.lineEdit_2.text().strip())
                        discount.append(self.lineEdit_2.text().strip())
                        
                        ins = db.__add_Discount__(discount)
                        
                        if ins == 1:
                            self.lineEdit_2.setText("successful")
                        else:
                            self.lineEdit_2.setText("Discount already exists")
                    else:
                        self.lineEdit_2.setText("price is out of range")
                except:
                    self.lineEdit_2.setText("invalid value")
            else:
                self.lineEdit_2.setText("cost is empty")
        else:
            self.lineEdit_2.setText("the start data is smaller than end data")
        
    def __guadagno_label__(self):
        result = db.__guadagno__()
    
        cost = 0.0    
    
        if result.__str__() != "[]":    
            for r in result:
                num = r.__str__()
                num = num.replace("[", " ").replace("(", " ").replace(","," ").replace(")"," ").replace("]"," ").strip()
                cost = cost + int(num)

                return cost.__str__()
        else:
            return "poor"
        
    def fun_add(self):
        if self.lineEdit.text().strip() != "":
            try:
                int(self.lineEdit.text().strip())
                lst = []
                lst.append(self.lineEdit.text().strip())
                ins = db. __add_prezzo__(lst)
                if ins == 1:
                    self.lineEdit.setText("successful")
                else:
                    print(ins)
                    self.lineEdit.setText("Error db")     
            except Exception as e:
                print(e)
                self.lineEdit.setText("invalid value")
        else:
            self.lineEdit.setText("invalid value")
        
    def fun_exit(self):
        self.close()
        self.parent().show()