# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/py/raspberry-pi-RC/handle.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 330)
        self.Headlamp_Button = QtWidgets.QPushButton(Form)
        self.Headlamp_Button.setGeometry(QtCore.QRect(0, 0, 521, 61))
        self.Headlamp_Button.setObjectName("Headlamp_Button")

        self.Taillamp_Button = QtWidgets.QPushButton(Form)
        self.Taillamp_Button.setGeometry(QtCore.QRect(-10, 270, 531, 61))
        self.Taillamp_Button.setObjectName("Taillamp_Button")
        
        self.SpeedSlider = QtWidgets.QSlider(Form)
        self.SpeedSlider.setGeometry(QtCore.QRect(40, 70, 51, 181))
        self.SpeedSlider.setMinimum(-100)
        self.SpeedSlider.setMaximum(100)
        self.SpeedSlider.setOrientation(QtCore.Qt.Vertical)
        self.SpeedSlider.setObjectName("SpeedSlider")
        self.SpeedSlider.valueChanged.connect(self.showValue)
        self.SpeedSlider.sliderReleased.connect(self.reset)

        self.Speed_meter = QtWidgets.QDial(Form)
        self.Speed_meter.setGeometry(QtCore.QRect(190, 150, 111, 101))
        self.Speed_meter.setObjectName("Speed_meter")
        self.Speed_meter.setMaximum(240)

        self.Speed_Label = QtWidgets.QLabel(Form)
        self.Speed_Label.setGeometry(QtCore.QRect(180, 90, 131, 51))
        self.Speed_Label.setScaledContents(False)
        self.Speed_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Speed_Label.setObjectName("Speed_Label")

        self.handle = QtWidgets.QDial(Form)
        self.handle.setGeometry(QtCore.QRect(360, 100, 131, 111))
        self.handle.setProperty("value", 0)
        self.handle.setObjectName("handle")
        self.handle.setValue(50)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Headlamp_Button.setText(_translate("Form", "Headlamp"))
        self.Taillamp_Button.setText(_translate("Form", "Taillamp"))
        self.Speed_Label.setText(_translate("Form", "0"))
    
    def reset(self):
        self.SpeedSlider.setValue(0)

    def showValue(self):
        self.dir = ''
        if self.SpeedSlider.value() >= 0:
            self.dir = 'D'
        else:
            self.dir = 'R'
        self.speed = abs(self.SpeedSlider.value())
        self.Speed_meter.setValue(self.speed)
        self.speed = str(self.speed)
        self.Speed_Label.setText(self.dir+self.speed)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

