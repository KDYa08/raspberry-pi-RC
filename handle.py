# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handle.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(60, 70, 26, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setMinimum(-100)
        self.verticalSlider.setMaximum(100)
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(280, 90, 111, 131))
        self.dial.setObjectName("dial")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 20, 99, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 240, 99, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 20, 99, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(150, 70, 101, 41))
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 20, 99, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.dial_2 = QtWidgets.QDial(Form)
        self.dial_2.setGeometry(QtCore.QRect(150, 120, 91, 101))
        self.dial_2.setObjectName("dial_2")

        self.retranslateUi(Form)
        self.verticalSlider.valueChanged.connect(self.showValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Head Light"))
        self.pushButton_2.setText(_translate("Form", "Tail Light"))
        self.pushButton_3.setText(_translate("Form", "Left"))
        self.pushButton_4.setText(_translate("Form", "Right"))
    
    def showValue(self):
        self.a = abs(self.verticalSlider.value())
        self.lcdNumber.display(self.a)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

