#GPIO제어 모듈 불러오기
import RPi.GPIO as GPIO
#시간 모듈 불러오기
from time import sleep
class Motor:
    #핀번호 받아와서 초기설정
    def __init__(self,pin1,pin2,pin3,pwm=0):
        self.pmw=pwm
        self.pin1=pin1
        self.pin2=pin2
        self.pin3=pin3
        #GPIO를 BCM(실제 핀 번호)으로 구동
        GPIO.setmode(GPIO.BCM)
        
        #출력핀으로 지정
        GPIO.setup(self.pin1,GPIO.OUT)
        GPIO.setup(self.pin2,GPIO.OUT)
        GPIO.setup(self.pin3,GPIO.OUT)
        #PWM헨들 얻어와서 100kHz로 동작 시킴 
        self.pwm=GPIO.PWM(self.pin1, 100)
        #출력0
        self.pwm.start(0)
        
        #모터 속도 제어 PWM
    def motor(self,speed):
        #속도가 -100이상 100이하라면
        if isinstance(speed,int) and speed>=-100 and speed<=100:
            #속도의 절댓값을 출력
            self.pwm.ChangeDutyCycle(abs(speed))
            #속도가 0보다 작다면
            if speed<0:
                #후진
                GPIO.output(self.pin2,0)
                GPIO.output(self.pin3,1)
            #속도가 0보다 크다면
            elif speed>0:
                #전진
                GPIO.output(self.pin2,1)
                GPIO.output(self.pin3,0)
            #아니면(속도가 0이라면)
            else:
                #정지
                GPIO.output(self.pin2,0)
                GPIO.output(self.pin3,0)
        #속도가 범위를 초과하면
        else:
            #오류문 출력
            print("\033[31m"+"###############ERROR###############")
            print("\033[31m"+"the range of speed is -100 to 100")
            print("\033[31m"+"the input speed is",speed)
            print("\033[31m"+"###################################")

    #종료
    def end(self):
        self.motor(0)
        print("\033[32m"+"motor stop")
