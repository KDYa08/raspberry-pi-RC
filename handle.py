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
        self.Headlamp_Button = QtWidgets.QPushButton(Form)                                    # Headlamp 버튼 생성(전조등 버튼)
        self.Headlamp_Button.setGeometry(QtCore.QRect(0, 0, 521, 61))
        self.Headlamp_Button.setObjectName("Headlamp_Button")

        self.Headlamp_Button.clicked.connect(self.Headlamp_switch(self.Headlamp_switch))      # Headlamp_Button을 눌렀을시 headlamp_LED 제어

        # taillamp 버튼
        self.Taillamp_Button = QtWidgets.QPushButton(Form)                                    # Taillamp 버튼 생성(후미등 버튼)
        self.Taillamp_Button.setGeometry(QtCore.QRect(-10, 270, 531, 61))
        self.Taillamp_Button.setObjectName("Taillamp_Button")

        self.Headlamp_Button.clicked.connect(self.Taillamp_switch(self.Taillamp_switch))      # Taillamp_Button을 눌렀을시 taillamp_LED 제어
        
        # 앞 뒤 조종 슬라이더
        self.Speed_Slider = QtWidgets.QSlider(Form)                                           # Speed_Slider 슬라이더 생성(앞 뒤 조종)
        self.Speed_Slider.setGeometry(QtCore.QRect(40, 70, 51, 181))
        self.Speed_Slider.setMinimum(-100)                                                    # 슬라이더 값 범위를 -100~100으로 지정
        self.Speed_Slider.setMaximum(100)
        self.Speed_Slider.setOrientation(QtCore.Qt.Vertical)                                  # 슬라이더 방향을 세로로 지정
        self.Speed_Slider.setObjectName("Speed_Slider")

        self.Speed_Slider.valueChanged.connect(self.showValue,self.front_move)                # 슬라이더 값이 바뀌면 함수 showValue,front_move를 호출
        self.Speed_Slider.sliderReleased.connect(self.front_move_stop)                        # 슬라이더를 놓으면 함수 front_move_stop를 호출 

        # 속도계 다이얼
        self.Speed_meter = QtWidgets.QDial(Form)                                              # Speed_meter 다이얼 생성(속도계)
        self.Speed_meter.setGeometry(QtCore.QRect(190, 150, 111, 101))
        self.Speed_meter.setObjectName("Speed_meter")
        self.Speed_meter.setMaximum(240)

        # 속도계 숫자
        self.Speed_Label = QtWidgets.QLabel(Form)                                             # Speed_Label 생성(속도계 숫자)
        self.Speed_Label.setGeometry(QtCore.QRect(180, 90, 131, 51))
        self.Speed_Label.setScaledContents(False)
        self.Speed_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Speed_Label.setObjectName("Speed_Label")

        # 핸들 다이얼
        self.handle = QtWidgets.QDial(Form)                                                   # handle 다이얼 생성(핸들)
        self.handle.setGeometry(QtCore.QRect(360, 100, 131, 111))
        self.handle.setProperty("value", 0)
        self.handle.setObjectName("handle")

        self.handle.setValue(50)                                                              # handle 값을 중앙으로 설정
        self.handle.valueChanged.connect(self.cornor_move)                                    # handle 값이 바뀌면 함수 cornor_move를 호출

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    # 키보드로 조종하는 함수
    def KeyPressEvent(self, e):
        # 속도 조절 커맨드(10씩 컨트롤)
        if e.key() == QtCore.key_Ctrl:
            self.Speed_Slider.setValue(self.Speed_Slider.value() + 10)
            self.showValue()
        elif e.key() == QtCore.key_Alt:
            self.Speed_Slider.setValue(self.Speed_Slider.value() - 10)
            self.showValue()
        
        # 앞 뒤 조종 커맨드
        if e.key() == QtCore.key_W:
            self.front_move()
        elif e.key() == QtCore.key_S:
            self.front_move()
        
        # 좌 우 조종 커맨드
        if e.key() == QtCore.key_A:
            self.handle.setValue(0)
            self.cornor_move()
        elif e.key() == QtCore.key_D:
            self.handle.setValue(100)
            self.cornor_move()

        # LED 조종 컨트롤
        if e.key() == QtCore.key_Q:
            self.Headlamp_switch

        elif e.key() == QtCore.key_E:
            self.Taillamp_switch()
        else:
            self.front_move_stop()

    # UI 생성 함수
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Headlamp_Button.setText(_translate("Form", "Headlamp"))                          # headlamp 버튼 텍스트를 "Headlamp"로 지정
        self.Taillamp_Button.setText(_translate("Form", "Taillamp"))                          # taillamp 버튼 텍스트를 "Taillamp"로 지정
        self.Speed_Label.setText(_translate("Form", "0"))                                     # Speed_Label 라벨 텍스트를 "0"으로 지정

    # 정지
    def front_move_stop(self):
        self.Speed_Slider.setValue(0)                                                         # Speed_Slider값을 0으로 정한다
        headway.motor(self.Speed_Slider.value())                                              # headway 모터 속도를 Speed_Slider값(0)으로 정한다

    # 전진or후진
    def front_move(self):
        headway.motor(self.Speed_Slider.value())                                              # headway 모터 속도를 Speed_Slider값(-100 ~ 100)으로 정한다

    # 좌or우회전
    def cornor_move(self):
        cornor.motor(self.handle.value())                                                     # cornor 모터를 handle값(0 ~ 100)으로 정한다

    # 앞 뒤 조종 슬라이더를 움직일때 호출 되는 함수
    def showValue(self):
        # 슬라이더 값이 +이면 D, -면 R을 띄우고
        self.dir = ''
        if self.Speed_Slider.value() >= 0:
            self.dir = 'D'
        else:
            self.dir = 'R'
        
        # 슬라이더값을 절댓값으로 바꿔 속도계 다이얼에 적용한다
        self.speed = abs(self.Speed_Slider.value())                                            # Speed_Slider값을 절댓값으로 바꿔 speed에 저장
        self.Speed_meter.setValue(self.speed)                                                  # Speed_metrer값을 speed값으로 지정
        self.speed = str(self.speed)                                                           # speed값을 str로 저장
        self.Speed_Label.setText(self.dir+self.speed)                                          # Speed_Label값을 dir+speed값으로 지정 ex) D50, R50
    
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

