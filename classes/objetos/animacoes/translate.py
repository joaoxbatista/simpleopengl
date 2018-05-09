# -*- coding: utf-8 -*-
from animation import Animation 
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Translate(Animation):

	def __init__(self,axis, initial, finaly, inverse = False, velocity = 0.01):
		self.axis = axis
		self.initial = initial
		self.finaly = finaly
		self.position = initial
		self.velocity = velocity
		self.inverse = inverse

		if (self.inverse):
			self.velocity = velocity * -1.0

	def animate(self):
		print("POSISION :> " + str(self.position))
		if(self.axis == 'x'):
			glTranslate(self.position, 0, 0)

		elif(self.axis == 'y'):
			glTranslate(0, 0, self.position)

		elif(self.axis == 'z'):
			glTranslate(0, self.position, 0)

		
		if(self.inverse and self.position <= self.initial):
			self.velocity = self.velocity * -1.0
			self.inverse = False

		elif(not self.inverse and self.position >= self.finaly): 
			self.velocity = self.velocity * -1.0
			self.inverse = True
		else:
			self.position += self.velocity

obj = Translate('y', 0, 10, True)
