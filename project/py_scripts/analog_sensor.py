from machine import Pin, ADC
from time import sleep

sleep(0.1)

led_pin = 25
led2_pin = 15
data_pin = 13
analog_data_pin = 26

led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.IN)

data = Pin(data_pin, Pin.IN)

analog_data = ADC(Pin(analog_data_pin))

while True:
    if data.value() == 1:
        led.value(True)
        led2.value(False)
    else:
        led.value(False)
        led2.value(True)
    print(analog_data.read_u16())
    sleep(0.1)