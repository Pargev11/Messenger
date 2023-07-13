import typing
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from functools import partial
import time
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal, QObject

path = os.path.dirname(os.path.abspath(__file__))

class Communicate(QObject):
    event = pyqtSignal()


# class thread(QThread):
#     def __init__(self, mainwindow, parent = None):
#         super().__init__()
#         self.mainwindow = mainwindow
#     def run(self):
#         while 1:
#             if self.mainwindow.flag == 1:
                
#                 self.mainwindow.flag = 0

class Ui_Form(object):
    def __init__(self,main):
        self.main = main
        self.flag = 0
        self.poisk_client = []
        self.contact = ""
        # self.sob_flag = 0
        self.contacts = []
        self.msg = []
        self.lay = []
        self.cdata = []
        self.msg_data = []
        self.get_data = ""


        self.poiskevent = Communicate()
        self.poiskevent.event.connect(self.poisk_clients)
        self.getevent = Communicate()
        self.getevent.event.connect(self.get_msg)
        self.change_sql = Communicate()
        self.change_sql.event.connect(self.main.change_sql)

  
    def poisk_text_change(self,text):
        self.pushButton_2.show()
        self.main.poisk(text)

    def click_on_but(self,anun):
        self.lineEdit_4.setText("")
        self.label.show()
        self.label.setText("    "+anun)
        self.lineEdit.show()
        self.pushButton_3.show()
        self.scrollArea.show()
        self.pushButton_2.hide()
        self.msg_data = []
        self.Msg_del()

        self.poisk_clients(self.contacts)
        print(anun)
        self.contact = anun

        self.main.get_msg_data(anun)
        # self.message_widjet()
        for i in self.msg_data:
            if i[0] == 'get':
                self.get_message_widjet(i[1])
            else:
                self.message_widjet(i[1])


    
    def clean_poisk(self):
        for e in self.poisk_client:
           e.deleteLater()
           self.verticalLayout.removeItem(self.spacerItem3)
        self.poisk_client = []

    def poisk_clients(self,listt = None):
        if listt == None:
            listt = self.cdata
        self.clean_poisk()
        
        print(listt) 
        if  listt != []:
            i = 0
            for j in listt:
                
                self.poisk_client.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents_2))
                self.poisk_client[i].setMinimumSize(QtCore.QSize(0, 70))
                self.poisk_client[i].setMaximumSize(QtCore.QSize(16777215, 70))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.poisk_client[i].setFont(font)
                self.poisk_client[i].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.poisk_client[i].setStyleSheet("\n"
                                                        "QPushButton {\n"
                                                        "    border: none;\n"
                                                        "    border-radius: 15px;;\n"
                                                        "    color:rgb(255, 255, 255);\n"
                                                        "    text-align: left;\n"
                                                        "}\n"
                                                        "QPushButton:hover {\n"
                                                        "     background-color: rgb(44, 44, 44);\n"
                                                        "}\n"
                                                        "")
                self.poisk_client[i].setObjectName("pushButton_8")
                self.verticalLayout.addWidget(self.poisk_client[i])
                self.poisk_client[i].setText("    "+j)
                self.poisk_client[i].clicked.connect(partial(self.click_on_but,j))
                i+=1
            
            self.spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout.addItem(self.spacerItem3)
   
    def back(self):
        self.lineEdit_4.setText("")
        self.poisk_clients(self.contacts)
        self.pushButton_2.hide()
        
    def Msg_del(self):
        for i in range(len(self.msg)):
            

            self.verticalLayout_3.removeItem(self.lay[i])
            self.lay[i].removeWidget(self.msg[i])
            self.msg[i].deleteLater()
            
        self.msg = []
        self.lay = []

    def message_widjet(self,text):
        tox = 1
        # ms = ""
        # l = len(text)
        # if l/50 > 1:
        #     tox = int(l/50)+1
        # for i in range(tox-1):
        #     print(50*i,(i+1)*50)
        #     ms = ms + text[50*i:(i+1)*50]+" "
        #     e = i+1
        # ms = ms + text[e:]
        # print(ms)
        # <html><head/><body><p>barev afabms afjdvm</p><p>nnnnn</p></body></html>
        horizontalLayout_5 = QtWidgets.QHBoxLayout()
        horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout_5.addItem(spacerItem2)
        label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.msg.append(label_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_5.sizePolicy().hasHeightForWidth())
        label_5.setSizePolicy(sizePolicy)
        label_5.setMinimumSize(QtCore.QSize(0, 39))
        # label_5.setMaximumSize(QtCore.QSize(100000, 39*tox))
        font = QtGui.QFont()
        font.setPointSize(12)
        label_5.setFont(font)
        label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border: none;\n"
                                        "    border-radius: 10px;;\n"
                                        "background-color: rgb(118, 106, 200);")
        label_5.setIndent(-1)
        label_5.setObjectName("label_5")
        label_5.adjustSize()
        label_5.setText(" "+text+" ")
        horizontalLayout_5.addWidget(label_5)
        self.lay.append(horizontalLayout_5)
        self.verticalLayout_3.addLayout(horizontalLayout_5)

    def get_message_widjet(self,text):
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.msg.append(label_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_4.sizePolicy().hasHeightForWidth())
        label_4.setSizePolicy(sizePolicy)
        label_4.setMinimumSize(QtCore.QSize(0, 39))
        # label_4.setMaximumSize(QtCore.QSize(201, 39))
        font = QtGui.QFont()
        font.setPointSize(12)
        label_4.setFont(font)
        label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"    border-radius: 10px;;\n"
"background-color: rgb(33, 33, 33);")
        label_4.setIndent(-1)
        label_4.adjustSize()
        label_4.setObjectName("label_4")
        label_4.setText(" "+text+" ")
        horizontalLayout.addWidget(label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem1)
        self.lay.append(horizontalLayout)
        self.verticalLayout_3.addLayout(horizontalLayout)

    def send_button(self):
        text = self.lineEdit.text()
        for i in range(len(text)):
            if text[i] != " ":
                text = text[i:]
                break
        if text != "":
            self.lineEdit.setText("")
            self.main.send(self.contact,text)
            self.message_widjet(text)
            
    def get_msg(self):

        self.get_message_widjet(self.get_data.split()[1])
        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 550)
        Form.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setMinimumSize(QtCore.QSize(515, 201))
        self.scrollArea.setMaximumSize(QtCore.QSize(620, 16777215))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 530, 413))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
#         self.label_4.setSizePolicy(sizePolicy)
#         self.label_4.setMinimumSize(QtCore.QSize(201, 39))
#         self.label_4.setMaximumSize(QtCore.QSize(201, 39))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.label_4.setFont(font)
#         self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
# "border: none;\n"
# "    border-radius: 10px;;\n"
# "background-color: rgb(33, 33, 33);")
#         self.label_4.setIndent(-1)
#         self.label_4.setObjectName("label_4")
#         self.horizontalLayout.addWidget(self.label_4)
#         spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout.addItem(spacerItem1)
#         self.verticalLayout_3.addLayout(self.horizontalLayout)
#         self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_5.setObjectName("horizontalLayout_5")
#         spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout_5.addItem(spacerItem2)
#         self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
#         self.label_5.setSizePolicy(sizePolicy)
#         self.label_5.setMinimumSize(QtCore.QSize(201, 39))
#         self.label_5.setMaximumSize(QtCore.QSize(201, 39))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.label_5.setFont(font)
#         self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
# "border: none;\n"
# "    border-radius: 10px;;\n"
# "background-color: rgb(118, 106, 200);")
#         self.label_5.setIndent(-1)
#         self.label_5.setObjectName("label_5")
#         self.horizontalLayout_5.addWidget(self.label_5)
#         self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_8.addWidget(self.scrollArea)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_8.addWidget(self.line_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()                                       #панел отправки собщение
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(450, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(550, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("border: none;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(33, 33, 33);\n"
"padding: 0 8px;\n"
"")
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorPosition(5)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius: 25%;\n"
"background-color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(118, 106, 200);\n"
"}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+r"\ui\4645382n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)  
        self.pushButton_3.clicked.connect(self.send_button)                  
        self.horizontalLayout_2.addLayout(self.horizontalLayout_9)
        # spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)                                     #  название клиента
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"border-right: 1px solid rgb(60,60, 60);")
        self.widget.setObjectName("widget")
        self.widget.setMinimumSize(QtCore.QSize(250, 60))
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(70, 10, 171, 40))
        self.widget_2.setStyleSheet("border: none;\n"
"border-radius: 20px;\n"
"background-color: rgb(44, 44, 44);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 8, 25, 25))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(path+r"\ui\systemsearch_104123 (1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(42, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.textChanged.connect(self.poisk_text_change)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(15, 10, 40, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius: 20%;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(44, 44, 44);\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path+r"\ui\126472m.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 10, 40, 40))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius: 20%;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(44, 44, 44);\n"
"}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(path+r"\ui\img_83225.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(250, 0))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scrollArea_2.setStyleSheet("border: none;\n"
"background-color: rgb(33, 33, 33);")
        self.scrollArea_2.setLineWidth(1)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 250, 490))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setContentsMargins(-1, 9, 0, 9)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
#         self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
#         self.pushButton_8.setMinimumSize(QtCore.QSize(0, 70))
#         self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 70))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.pushButton_8.setFont(font)
#         self.pushButton_8.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.pushButton_8.setStyleSheet("\n"
# "QPushButton {\n"
# "    border: none;\n"
# "    border-radius: 15px;;\n"
# "    color:rgb(255, 255, 255);\n"
# "    text-align: left;\n"
# "}\n"
# "QPushButton:hover {\n"
# "     background-color: rgb(44, 44, 44);\n"
# "}\n"
# "")
#         self.pushButton_8.setObjectName("pushButton_8")
#         self.verticalLayout.addWidget(self.pushButton_8)
        
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 1, 0, 1, 1)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # self.tthread = thread(mainwindow=self)
        # self.tthread.start()

    def retranslateUi(self, Form):
        self.label.hide()
        self.lineEdit.hide()
        self.pushButton_3.hide()
        self.scrollArea.hide()
        self.pushButton_2.hide()
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.label_4.setText(_translate("Form", "<html><head/><body><p>barev afabms afjdvm <span style=\" color:#646464; vertical-align:sub;\">12:34</span></p></body></html>"))
        # self.label_5.setText(_translate("Form", "<html><head/><body><p>barev afabms afjdvm <span style=\" color:#969696; vertical-align:sub;\">12:34</span></p></body></html>"))
        # self.lineEdit.setText(_translate("Form", "Barev"))
        self.label.setText(_translate("Form", "    Anun"))
        # self.pushButton_8.setText(_translate("Form", "    Anun"))
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(None,None,None,None)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
