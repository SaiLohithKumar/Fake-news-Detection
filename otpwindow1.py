# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otpwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
import tkinter.messagebox as tsmg
import requests
import random
import json
import webbrowser

rand=random.randint(1,999999)
msg=f"this is  your OTP :{rand}"
class Ui_otpform(object):
      def send(self):
              a=(self.lineEdit1.text())
              print(type(a))
              print(type(msg))
              if(a==""):
                   tsmg.showerror("Error","Enter Your Mobile Number")
              elif (len(a)<10):
                   tsmg.showerror("Error","Invalid Mobile Number")
                   self.LineEdit1.set("")
              else:
                   b=tsmg.askyesno("Info",f"Your Number is {a}")
                   if(b==True):
                       for i in range(0,1):
                                  url="https://www.fast2sms.com/dev/bulk"
                                  params={
                                           #Paste Your Unique API Here in-place of ************
                                           "authorization":"xD8vU3tnEbpBTR2h4mqXc9SzJYHgiGlauM6e0dQZsO1AWkjwLfKODzuAY5dl9sWCJcrgp03Ex6MH7Smn",
                                           "sender_id":"SMSINI",
                                           "message":msg,
                                           "language":"english",
                                           "route":"p",
                                           "numbers":a
                                          }
                                  rs=requests.get(url,params=params)
                                
                   else:
                        self.lineEdit1.set("") 
                 
      def check(self):
               c=(self.lineEdit2.text()) 
               if(c==""):
                  tsmg.showerror("Error","Enter OTP")
               else:
                   if(str(rand)==c):
                      tsmg.showinfo("Info","Successful")
                      self.label4.setText("SucessFull")
                      filename = 'file:///Users/polinasaimanoj/Documents/HTML/19113101_saimanoj/team9_mini_project2/menu2.html'
                      webbrowser.open_new_tab(filename)
                   else:
                      tsmg.showerror("Error","Invalid OTP")
                      self.label4.setText("Invalid OTP")
                      self.lineEdit1.set("")
                      self.lineEdit2.set("")
      def setupUi(self, otpform):
          otpform.setObjectName("otpform")
          otpform.resize(499, 435)
          self.label1 = QtWidgets.QLabel(otpform)
          self.label1.setGeometry(QtCore.QRect(0, 0, 541, 431))
          self.label1.setText("")
          self.label1.setPixmap(QtGui.QPixmap("otpimg.png"))
          self.label1.setScaledContents(True)
          self.label1.setObjectName("label1")
          self.label2 = QtWidgets.QLabel(otpform)
          self.label2.setGeometry(QtCore.QRect(130, 10, 191, 31))
          self.label2.setObjectName("label2")
          self.label3 = QtWidgets.QLabel(otpform)
          self.label3.setGeometry(QtCore.QRect(10, 70, 191, 31))
          self.label3.setObjectName("label3")
          self.label = QtWidgets.QLabel(otpform)
          self.label.setGeometry(QtCore.QRect(10, 200, 131, 31))
          self.label.setObjectName("label")
          self.pushButton1 = QtWidgets.QPushButton(otpform)
          self.pushButton1.setGeometry(QtCore.QRect(30, 290, 161, 51))
          self.pushButton1.setObjectName("pushButton1")
          self.pushButton2 = QtWidgets.QPushButton(otpform)
          self.pushButton2.setGeometry(QtCore.QRect(250, 290, 161, 51))
          self.pushButton2.setObjectName("pushButton2")
          self.label_2 = QtWidgets.QLabel(otpform)
          self.label_2.setGeometry(QtCore.QRect(20, 370, 101, 31))
          self.label_2.setObjectName("label_2")
          self.label4 = QtWidgets.QLabel(otpform)
          self.label4.setGeometry(QtCore.QRect(140, 370, 191, 31))
          self.label4.setObjectName("label4")
          self.lineEdit1 = QtWidgets.QLineEdit(otpform)
          self.lineEdit1.setGeometry(QtCore.QRect(200, 70, 201, 31))
          self.lineEdit1.setInputMask("")
          self.lineEdit1.setClearButtonEnabled(True)
          self.lineEdit1.setObjectName("lineEdit1")
          self.lineEdit2 = QtWidgets.QLineEdit(otpform)
          self.lineEdit2.setGeometry(QtCore.QRect(150, 200, 201, 31))
          self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Normal)
          self.lineEdit2.setClearButtonEnabled(True)
          self.lineEdit2.setObjectName("lineEdit2")

          self.retranslateUi(otpform)
          QtCore.QMetaObject.connectSlotsByName(otpform)
          self.pushButton1.clicked.connect(self.send)
          self.pushButton2.clicked.connect(self.check)

      def retranslateUi(self, otpform):
          _translate = QtCore.QCoreApplication.translate
          otpform.setWindowTitle(_translate("otpform", "OTP FORM"))
          self.label2.setText(_translate("otpform", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic; color:#800080;\">OTP CHECKER</span></p></body></html>"))
          self.label3.setText(_translate("otpform", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#f94e4a;\">Mobile Number:</span></p></body></html>"))
          self.label.setText(_translate("otpform", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#f66c62;\">Check OTP:</span></p></body></html>"))
          self.pushButton1.setText(_translate("otpform", "Send OTP"))
          self.pushButton2.setText(_translate("otpform", "Check OTP"))
          self.label_2.setText(_translate("otpform", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#f95041;\">STATUS:</span></p></body></html>"))
          self.label4.setText(_translate("otpform", "<html><head/><body><p><br/></p></body></html>"))
          self.lineEdit1.setText(_translate("otpform", "Enter Mobile Number"))
          self.lineEdit2.setText(_translate("otpform", "Enter OTP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otpform = QtWidgets.QWidget()
    ui = Ui_otpform()
    ui.setupUi(otpform)
    otpform.show()
    sys.exit(app.exec_())
