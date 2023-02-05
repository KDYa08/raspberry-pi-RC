#클래스 불러오기
import motor,led
#GPIO제어/시간 모듈 불러오기
import RPi.GPIO as GPIO
from time import sleep
#인스턴스 생성(괄호안은 핀번호)
front=motor.Motor(11,22,27)
rear=motor.Motor(17,9,10)
white=led.Led(4)
red=led.Led(6)
##########실행##########
#출력100으로 전진
rear.motor(100)
#백색 led 켬
white.on()
#적색 led 끔
red.off()
#1초 대기
sleep(1)

#출력100으로 후진
rear.motor(-100)
#백색 led 끔
white.off()
#적색 led 켬
red.on()
#1초 대기
sleep(1)
##########종료##########
front.end()
rear.end()
white.end()
red.end()

GPIO.cleanup()
