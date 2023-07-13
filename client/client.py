from login import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os

class reg():
    def __init__(self,s):
        self.s = s

        self.s.sendall("-".encode())          #отпражит - если новии клиент
        
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.login,self.signup)
        self.ui.setupUi(self.MainWindow)
        # ui.new_wrongname()
        self.MainWindow.show()
        
        sys.exit(app.exec_())

    def login(self,name, password):
        self.s.sendall(("lg"+name+" "+password).encode())    #отправка данниь
        print("lg"+name+" "+password)
        #палучит существует акаунт или нет
        data = self.s.recv(1024).decode('UTF-8')
        if data == "ok":
            print("login",name,password) 

            # обнавит состаяние клиента
            path = os.path.dirname(os.path.abspath(__file__))
            with open(path+"\\state.txt", "w") as f:
                f.write(name)

            # перезарузет прараму
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        else:
            self.ui.wrong()
                    



    def signup(self,name,password):
        self.s.sendall(("rg"+name+" "+password).encode())    #отправка данниь
        print("rg"+name+" "+password)
        #палучит существует акаунт или нет
        data = self.s.recv(1024).decode('UTF-8')

        if data == "ok":
            print("new akaunt",name,password)
            # обнавит состаяние клиента
            path = os.path.dirname(os.path.abspath(__file__))
            with open(path+"\\state.txt", "w") as f:
                f.write(name)
     
            #перезарузет прараму
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        else:
            self.ui.new_wrongname()
       


