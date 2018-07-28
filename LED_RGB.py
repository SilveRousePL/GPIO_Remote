import sys
import signal
import time
import colorsys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(13, 0)
GPIO.output(19, 0)
GPIO.output(26, 0)

r_pwm = GPIO.PWM(13,60)
g_pwm = GPIO.PWM(19,60)
b_pwm = GPIO.PWM(26,60)

r_pwm.start(0)
g_pwm.start(0)
b_pwm.start(0)

def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C! Clean up GPIO')
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

hue = float(0)

while True:
    r, g, b = colorsys.hsv_to_rgb(hue,1,1)
    print("  {:3.0f}% {:3.0f}% {:3.0f}%\r".format(r*100,g*100,b*100),end='')
    r_pwm.ChangeDutyCycle(r*100)
    g_pwm.ChangeDutyCycle(g*100)
    b_pwm.ChangeDutyCycle(b*100)
    hue += 0.01
    if hue > 1.00:
        hue = float(0)
    time.sleep(.05)

GPIO.cleanup()
