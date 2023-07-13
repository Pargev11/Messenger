from mainui import Ui_Form 
from client import reg 
from PyQt5 import QtWidgets
import sys
import os
import socket
import sqlite3 as sq
import time
import threading
from PyQt5.QtCore import QThread
from sqlite3 import Error


class main:
    def __init__(self,s,my_name):
        path = os.path.dirname(os.path.abspath(__file__))
        self.cone = sq.connect(path+"\\BD.sqlite")

        self.s = s
        data = s.recv(1024).decode('UTF-8')
        if data != " ": 
            with self.cone:
                data = data.split()
                for i in range(0,len(data),3):
                    contact, text, Time = data[i+0], data[i+1], float(data[i+2])
                    print(data)
                    cur = self.cone.cursor()
                    cur.execute(F"INSERT INTO mesages VALUES('{contact}', '{text}', 'g', '{Time}', 'no')")
                    self.cone.commit()


        self.cdata = []
        
        self.my_name = my_name
        tr1 = threading.Thread(target=self.get_msg)
        tr1.start()

        self.ui = Ui_Form(self)
        self.app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        self.ui.setupUi(Form)
        self.get_contacts_data()
        Form.show()
        
        sys.exit(self.app.exec_())
        

    def addclient(self):
        poisk_name = []
        
        for i in self.cdata:
            poisk_name.append(i)
        return poisk_name

    def poisk(self,name):
        
        if name != "":
            s.sendall(("po"+name).encode())
            
        else:
            self.cdata = []
            self.ui.clean_poisk()
    
    
    def poisk_get(self,data):

        data = data.split()
        try:
            data.remove(self.my_name)
        except:
            pass
        self.cdata = data
        self.ui.cdata = data
        self.ui.poiskevent.event.emit()
        # # self.ui.c.eventt.emit()
        print(data)
        
    def client_list_change(self,contact,):
        with self.cone:
            seconds = time.time()
            cur = self.cone.cursor()
            zapros = F"SELECT * FROM contacts WHERE names == '{contact}'"
            cur.execute(zapros)
            id = cur.fetchall()
            
            if id == []:
                cur.execute(F"INSERT INTO contacts VALUES('{contact}', '{seconds}')")
                self.cone.commit()

                cur.execute(F"SELECT * FROM contacts ORDER BY timee")
                a = cur.fetchall()
                listt = [i[0] for i in a]
                self.ui.contacts = listt
            else:
                cur.execute(F"UPDATE contacts SET timee = {seconds}  WHERE names = '{contact}'")

            index = self.ui.contacts.index(contact)
            self.ui.contacts = [contact]+self.ui.contacts[:index]+self.ui.contacts[index+1:]
            print(self.ui.contacts)

            self.ui.poisk_clients(self.ui.contacts)

    def send(self,contact,text):
        with self.cone:
            try:
                send_msg = "se"+contact+" "+text
                s.sendall(send_msg.encode())
                self.client_list_change(contact)

                cur = self.cone.cursor()

                print(contact,text)
                

                cur.execute(F"INSERT INTO mesages VALUES('{contact}', '{text}', 's', '{time.time()}', 'no')")
                self.cone.commit()
            except:pass
            

    def get_mg(self,data):     
        self.ui.get_data = data
        self.ui.getevent.event.emit()

        data = data.split()
        
        self.sqldata = [data[0],data[1]]
        self.ui.change_sql.event.emit()
        # self.ui.get_message_widjet(data[1])
    
    def change_sql(self):
        contact,text = self.sqldata[0],self.sqldata[1]
        with self.cone:
            cur = self.cone.cursor()
            try:
                cur.execute(F"INSERT INTO mesages VALUES('{contact}', '{text}', 'g', '{time.time()}', 'no')")
                self.cone.commit()
            except Error as e:
                print(e)
            print(contact,text)

            self.client_list_change(contact)

    def get_msg_data(self,contact):
        with self.cone:
            cur = self.cone.cursor()
            cur.execute(F"SELECT * FROM mesages WHERE name == '{contact}'")
            a = cur.fetchall()
            print(a)
            for i in a:
                if i[2] == 'g':
                    self.ui.msg_data.append(['get',i[1]])
                else:
                    self.ui.msg_data.append(['send',i[1]])


    def get_contacts_data(self):
        with self.cone:
            cur = self.cone.cursor()
            cur.execute(F"SELECT * FROM contacts ORDER BY timee DESC")
            a = cur.fetchall()
            listt = [i[0] for i in a]
            print(listt)
            self.ui.contacts = listt
            self.ui.poisk_clients(listt)

    def get_msg(self):
        
        while 1:
            try:
                data = s.recv(1024).decode('UTF-8')
                if data[:2] == 'po':
                    self.poisk_get(data[2:])
                elif data[:2] == 'se':
                    # print(data)
                    self.get_mg(data[2:])
            except:
                break
    


# палучит состаяние клиента (новии или старии)
path = os.path.dirname(os.path.abspath(__file__))
with open(path+"\\state.txt") as f:
    data = f.read()
    state = data
    


# падключение сержера
HOST = "127.0.0.1"  
PORT = 65432  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))





if state == '-':
    reg(s)


s.sendall(state.encode())
my_name = state
a = main(s,my_name)




