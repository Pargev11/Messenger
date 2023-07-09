from login import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os

class reg():
    def __init__(self,s):
        self.s = s

    def login(self,name, password):
        self.s.sendall(("l "+name+" "+password).encode())    #отправка данниь

        #палучит существует акаунт или нет
        data = self.s.recv(1024).decode('UTF-8')             
        if data[0:2] == "no":
            self.ui.wrong()
        elif data[0:2] == "ok":
            id = data[2:]
            print("cista")
            print("login",name,password)

            text = id

            # обнавит состаяние клиента
            path = os.path.dirname(os.path.abspath(__file__))
            with open(path+"\\state.txt", "w") as f:
                f.write(text)
     
            #перезарузет прараму
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                          



    def signup(self,name,password):
        self.s.sendall(("s "+name+" "+password).encode())    #отправка данниь
        print(1)
        #палучит существует акаунт или нет
        data = self.s.recv(1024).decode('UTF-8')
        print(data)
        if data[:2] == "no":
            print("new akaunt",name,password)
            id = data[2:]

            text = id

            # обнавит состаяние клиента
            path = os.path.dirname(os.path.abspath(__file__))
            with open(path+"\\state.txt", "w") as f:
                f.write(text)
     
            #перезарузет прараму
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

        elif data == "ok":
            self.ui.new_wrongname()
            

    def run(self):
        self.s.sendall("-".encode())          #отпражит 0 если новии клиент
        
        
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.login,self.signup)
        self.ui.setupUi(self.MainWindow)
        # ui.new_wrongname()
        self.MainWindow.show()
        
        sys.exit(app.exec_())
