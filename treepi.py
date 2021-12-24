from gpiozero import PWMLED,LEDBoard
from gpiozero.tools import random_values, sin_values, scaled_half
import time
from signal import pause
import random

star = PWMLED(2)
star.value = 1
# tree = LEDBoard(4,15,13,21,25,8,5,10,16,17,27,26,24,9,12,6,20,19,14,18,11,7,23,22,pwm=True)
tree = LEDBoard(back=LEDBoard(15,21,8,5,27,26,12,6,19,18,11,7,pwm=True),
                front=LEDBoard(4,14,17,10,22,9,23,24,25,20,13,16,pwm=True))

def advent_lights(d):
  star.value = d/24
  for led in random.sample(tree.leds,d):
    led.source_delay = 0.01
    led.source = scaled_half(sin_values(random.randrange(100,300)))

def christmas_day_lights():
  star.blink(fade_in_time=0.2,fade_out_time=0.2,on_time=0.2+random.random(),off_time=1+random.random()*3,background=True)
  for led in tree.leds:
    led.blink(fade_in_time=0.2,fade_out_time=0.2,on_time=0.2+random.random(),off_time=1+random.random()*3,background=True)

def days_of_christmas_lights(d):
  star.value = (13-d)/12
  for led in random.sample(tree.back.leds,13-d):
    led.source_delay = 0.01
    led.source = scaled_half(sin_values(random.randrange(100,300)))
  for led in random.sample(tree.front.leds,13-d):
    led.on()

def update_lights(this_month = time.localtime(time.time()).tm_mon,
                  this_day = time.localtime(time.time()).tm_mday):

  print(this_month,this_day)
  if this_month == 12 and this_day < 25:
    day_of_advent = this_day
    print("day of advent:", day_of_advent)
    advent_lights(day_of_advent)
  elif this_month == 12 and this_day == 25:
    day_of_christmas = 1
    print("it's Chriiiiistmaaaaas!")
    christmas_day_lights()
  elif this_month == 12 and this_day > 25:
    day_of_christmas = this_day - 24
    print("day of Christmas:", day_of_christmas)
    days_of_christmas_lights(day_of_christmas)
  elif this_month == 1 and this_day < 6:
    day_of_christmas = this_day + 7
    print("day of Christmas:", day_of_christmas)
    days_of_christmas_lights(day_of_christmas)
  else:
    print("it's not Christmas :-(")

update_lights()
pause()
