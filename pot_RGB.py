#RGB - Red(14), Green(13), Blue(12)

from machine import Pin, PWM, ADC

pwm1 = PWM(Pin(14))
adc1 = ADC(Pin(26))
pwm2 = PWM(Pin(13))
adc2 = ADC(Pin(27))
pwm3 = PWM(Pin(12))
adc3 = ADC(Pin(28))

pwm1.freq(1000)
pwm2.freq(1000)
pwm3.freq(1000)


while True:
    duty1 = adc1.read_u16()
    pwm1.duty_u16(duty1)
    duty2 = adc2.read_u16()
    pwm2.duty_u16(duty2)
    duty3 = adc3.read_u16()
    pwm3.duty_u16(duty3)
