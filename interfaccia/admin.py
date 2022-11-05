from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import QDate
from PyQt6.uic import loadUi
import Gestione_Database.Connesione_Database as db
import sys
from cProfile import label





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
        
        self.__list_Discount__()
        self.__list_prenotation__()
        
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit.setMinimumDate(QDate.currentDate())
        self.dateEdit_2.setMinimumDate(QDate.currentDate())
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
                 
                label = QLabel(discount)
                self.vbox.addWidget(label)

                
        
    def __fun_add_discount__(self):
        date1 = self.dateEdit.date()
        date2 = self.dateEdit_2.date()
        date_in = date1.toPyDate()
        date_out = date2.toPyDate()
        
        if date_in < date_out:
            if self.lineEdit_2.text().strip() != "":
                try:
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