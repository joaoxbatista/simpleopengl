# -*- coding: utf-8 -*

class Rgb(object):

	@staticmethod
	def color(red, green, blue):
		value = 1.0/255.0
		red = value * red
		green = value * green
		blue = value * blue
		color = (round(red,2), round(green,2), round(blue,2))
		print(color)
		return color

		

COLOR_RED = Rgb.color(200, 0, 0)
COLOR_GREEN = Rgb.color(0, 255, 0)
COLOR_BLUE = Rgb.color(0, 0, 20)

COLOR_GREEN1 = Rgb.color(2, 188, 156)
COLOR_GREEN2 = Rgb.color(46, 204, 113)

COLOR_BLUE1 = Rgb.color(40, 120, 180)
COLOR_BLUE2 = Rgb.color(52, 152, 219)