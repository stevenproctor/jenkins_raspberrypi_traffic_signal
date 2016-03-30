import RPi.GPIO as GPIO  
import time

class TrafficSignal:
	def __init__(self, green_pin, yellow_pin, red_pin):
		self.green = green_pin
		self.yellow = yellow_pin
		self.red = red_pin
		self.__init_gpio()

	def __init_gpio(self):
		GPIO.setmode(GPIO.BOARD)  
		GPIO.setup(self.green, GPIO.OUT)  
		GPIO.setup(self.yellow, GPIO.OUT)  
		GPIO.setup(self.red, GPIO.OUT)  

	def on(self, pin):
		self.__setPin(pin, GPIO.HIGH)

	def off(self, pin):
		self.__setPin(pin, GPIO.LOW)

	def reset(self):
		self.off(self.green)
		self.off(self.yellow)
		self.off(self.red)

	def __setPin(self, pin, status):
		GPIO.output(pin, status)  

	def close(self):
		GPIO.cleanup()
