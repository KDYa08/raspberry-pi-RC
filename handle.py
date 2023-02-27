# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/py/raspberry-pi-RC/handle.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# 2/26 프론트 엔드 완성
# 2/27 버튼 백엔드 완성

from PyQt5 import QtCore, QtGui, QtWidgets
import motor,led
import RPi.GPIO as GPIO
from time import sleep

#인스턴스 생성(괄호안은 핀번호)
cornor=motor.Motor(11,22,27)
headway=motor.Motor(17,9,10)
headlamp=led.Led(4)
taillamp=led.Led(6)

# LED 리셋
Headlamp_state = False
Taillamp_state = False
headlamp.off()
taillamp.off()

class Ui_Form(object):
    def setupUi(self, Form, Headlamp_state, Taillamp_state):
        # 변수 불러오기
        self.Headlamp_state = Headlamp_state
        self.Taillamp_state = Taillamp_state

        # 창 생성
        Form.setObjectName("Form")
        Form.resize(522, 330)
        
        # headlamp 버튼
        self.Headlamp_Button = QtWidgets.QPushButton(Form)                             # Headlamp 버튼 생성
        self.Headlamp_Button.setGeometry(QtCore.QRect(0, 0, 521, 61))
        self.Headlamp_Button.setObjectName("Headlamp_Button")

        self.Headlamp_Button.clicked.connect(self.Headlamp_switch(self.Headlamp_switch))      # Headlamp_Button을 눌렀을시 headlamp_LED 제어

        # taillamp 버튼
        self.Taillamp_Button = QtWidgets.QPushButton(Form)
        self.Taillamp_Button.setGeometry(QtCore.QRect(-10, 270, 531, 61))
        self.Taillamp_Button.setObjectName("Taillamp_Button")
        self.Headlamp_Button.clicked.connect(self.Taillamp_switch(self.Taillamp_switch))      # Taillamp_Button을 눌렀을시 taillamp_LED 제어
        
        # 앞 뒤 조종 슬라이더
        self.SpeedSlider = QtWidgets.QSlider(Form)
        self.SpeedSlider.setGeometry(QtCore.QRect(40, 70, 51, 181))
        self.SpeedSlider.setMinimum(-100)
        self.SpeedSlider.setMaximum(100)
        self.SpeedSlider.setOrientation(QtCore.Qt.Vertical)
        self.SpeedSlider.setObjectName("SpeedSlider")
        self.SpeedSlider.valueChanged.connect(self.showValue,self.front_move)
        self.SpeedSlider.sliderReleased.connect(self.front_move_stop)

        # 속도계 다이얼
        self.Speed_meter = QtWidgets.QDial(Form)
        self.Speed_meter.setGeometry(QtCore.QRect(190, 150, 111, 101))
        self.Speed_meter.setObjectName("Speed_meter")
        self.Speed_meter.setMaximum(240)

        # 속도계 숫자
        self.Speed_Label = QtWidgets.QLabel(Form)
        self.Speed_Label.setGeometry(QtCore.QRect(180, 90, 131, 51))
        self.Speed_Label.setScaledContents(False)
        self.Speed_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Speed_Label.setObjectName("Speed_Label")

        # 핸들 다이얼
        self.handle = QtWidgets.QDial(Form)
        self.handle.setGeometry(QtCore.QRect(360, 100, 131, 111))
        self.handle.setProperty("value", 0)
        self.handle.setObjectName("handle")
        self.handle.setValue(50)
        self.handle.valueChanged.connect(self.cornor_move)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # UI 생성 함수
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Headlamp_Button.setText(_translate("Form", "Headlamp"))
        self.Taillamp_Button.setText(_translate("Form", "Taillamp"))
        self.Speed_Label.setText(_translate("Form", "0"))
    
    # 앞 뒤 조종 슬라이더를 놓았을 때 값과 속도값을 0으로 정한다
    def front_move_stop(self):
        self.SpeedSlider.setValue(0)
        headway.motor(self.SpeedSlider.value())

    # 자동차 앞 뒤 조종
    def front_move(self):
        headway.motor(self.SpeedSlider.value())

    # 자동차 조향 조종
    def cornor_move(self):
        cornor.motor(self.handle.value())

    # 앞 뒤 조종 슬라이더를 움직일때 호출 되는 함수
    def showValue(self):
        # 슬라이더 값이 +이면 D, -면 R을 띄우고
        self.dir = ''
        if self.SpeedSlider.value() >= 0:
            self.dir = 'D'
        else:
            self.dir = 'R'
        
        # 슬라이더값을 절댓값으로 바꿔 속도계 다이얼에 적용한다 ex) D50, R50
        self.speed = abs(self.SpeedSlider.value())
        self.Speed_meter.setValue(self.speed)
        self.speed = str(self.speed)
        self.Speed_Label.setText(self.dir+self.speed)
    
    # headlamp 스위치 함수
    def Headlamp_switch(self, Headlamp_state):
        # healamp가 켜져있으면 끄고,
        if Headlamp_state == True:
            headlamp.off()
            self.Headlamp_state = False
        # taillamp가 꺼져있으면 켜진다
        else:
            headlamp.on()
            self.Headlamp_state = True
    
    # taillamp 스위치 함수
    def Taillamp_switch(self, Taillamp_state):
        # taillamp가 켜져있으면 끄고,
        if Taillamp_state == True:
            taillamp.off()
            self.Taillamp_state = False
        # taillamp가 꺼져있으면 켜진다
        else:
            taillamp.on()
            self.Taillamp_state = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    front.end()
    rear.end()
    white.end()
    red.end()
    GPIO.cleanup()

