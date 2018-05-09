# -*- coding: utf-8 -*-
from animation import Animation 
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Scale(Animation):

	def __init__(self,axis, initial, finaly, inverse = False, velocity = 0.01):
		self.axis = axis
		self.initial = initial
		self.finaly = finaly
		self.scale = initial
		self.velocity = velocity
		self.inverse = inverse

		if (self.inverse):
			self.velocity = velocity * -1.0

	def animate(self):

		if(self.axis == 'x'):
			glScale(self.scale, 1, 1)

		elif(self.axis == 'y'):
			glScale(1, 1, self.scale)

		elif(self.axis == 'u'):
			glScale(self.scale, self.scale, self.scale)

		elif(self.axis == 'z'):
			glScale(1, self.scale, 1)

		
		if(self.inverse and self.scale <= self.initial):
			self.velocity = self.velocity * -1.0
			self.inverse = False

		elif(not self.inverse and self.scale >= self.finaly): 
			self.velocity = self.velocity * -1.0
			self.inverse = True
		else:
			self.scale += self.velocity

obj = Scale('y', 0, 10, True)
