from gpiozero import PWMLED,LEDBoard
from gpiozero.tools import random_values, sin_values, scaled_half
from signal import pause
import random

star = PWMLED(2)
star.value = 1
tree = LEDBoard(4,15,13,21,25,8,5,10,16,17,27,26,24,9,12,6,20,19,14,18,11,7,23,22,pwm=True)
for led in tree:
 led.source_delay = 0.01
 led.source = scaled_half(sin_values(random.randrange(100,300)))
pause()

