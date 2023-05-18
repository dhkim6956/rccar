from Raspi_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x6F)
pwm.setPWMFreq(60)

while True:
    value = int(input('PWM VALUE : '))
    if value <= 200 or value >= 500 : 
        print("WARNING")
        continue
    pwm.setPWM(0, 0, value)