from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self,login_2,signup_2):
        
        self.login_2 = login_2
        self.signup_2 = signup_2

    def no_prabel(self,text):
        for i in text:
            if i == " ":
                return False
        if text == "": return False
        return True
    
    def login(self):
        name = self.lineEdit_3.text()
        parol = self.lineEdit_4.text()

        if self.no_prabel(name) and self.no_prabel(parol): self.login_2(name,parol)
        else: self.wrong()

    def signup(self):
        name = self.lineEdit_3.text()
        parol = self.lineEdit_4.text() 

        if self.no_prabel(name) and self.no_prabel(parol): self.signup_2(name,parol)
        else: self.wrong()
    def wrong(self):
        self.label_6.setText("Wrong name or password")
    def new_wrongname(self):
        self.label_6.setText("this name already exists")
    
    def close(self):
        self.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 512)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(290, 371))
        self.widget.setMaximumSize(QtCore.QSize(290, 371))
        self.widget.setStyleSheet("background-color: rgb(33, 33, 33);\n"
                                "border:  none;\n"
                                "border-radius: 8px;")
        self.widget.setObjectName("widget")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(45, 30, 200, 51))

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)

        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(200, 200, 200);")
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 140, 230, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border:  none;\n"
                                        "border-radius: 5px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 220, 230, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border:  none;\n"
                                        "border-radius: 5px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(200, 200, 200);")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(200, 200, 200);")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 290, 110, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                        "color: rgb(200, 200, 200);\n"
                                        "border:  none;\n"
                                        "border-radius: 5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.login)


        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 290, 110, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                        "color: rgb(200, 200, 200);\n"
                                        "border:  none;\n"
                                        "border-radius: 5px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.signup)
        self.horizontalLayout.addWidget(self.widget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Welcome"))
        self.label_4.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.pushButton_4.setText(_translate("MainWindow", "Signup"))

def login(name, password):
    print("login",name,password)
def signup(name,password):
    print("signup",name,password)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(login,signup)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
