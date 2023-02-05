#GPIO제어 모듈 불러오기
import RPi.GPIO as GPIO
class Led:
    #핀번호 받아와서 초기 설정
    def __init__(self,pin):
        self.pin=pin
        #GPIO를 BCM(실제 핀 번호)으로 구동
        GPIO.setmode(GPIO.BCM)
        #출력핀으로 지정
        GPIO.setup(self.pin,GPIO.OUT)
        #led 끔
        GPIO.output(self.pin,0)
    #led 끔
    def off(self):
        GPIO.output(self.pin,0)
    #led 켬
    def on(self):
        GPIO.output(self.pin,1)
    #종료
    def end(self):
        GPIO.output(self.pin,0)
        print("\033[32m"+"led stop")
