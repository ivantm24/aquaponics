import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, 1)
print("Test")
if 1==1:
	print("k")
GPIO.cleanup()
