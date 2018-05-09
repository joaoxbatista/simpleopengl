# -*- coding: utf-8

class Color(object):

	def __init__(self, red = 1, green = 1, blue = 1, alpha = 1):
		self.red = red
		self.green = green
		self.blue = blue
		self.alpha = alpha

	def color(self):
		return [self.red, self.green, self.blue, self.alpha]
