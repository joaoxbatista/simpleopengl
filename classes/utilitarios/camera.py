# -*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos
from math import pi
from math import sin

class Camera(object):

	position = []
	velocity = 0.1
	object_position = []
	vector_up = [0, 1, 0]
	perspective = [40.,1.,1.,40.]

	def __init__(self, position, object_position):
		self.position = position
		self.object_position = object_position
		self.angulo = 30

	def active(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(self.perspective[0], self.perspective[1], self.perspective[2], self.perspective[3])
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity() 
		gluLookAt(self.position[0], self.position[1], self.position[2],
			self.object_position[0], self.object_position[1], self.object_position[2],
			self.vector_up[0], self.vector_up[1], self.vector_up[2])
		glEnable(GL_DEPTH_TEST) 
		glFlush()                 

	def normal_keys_filter(self, key):
		print(key)
		if key == b'a':
			self.position[0] = float(self.position[0] - self.velocity)
			self.object_position[0] = float(self.object_position[0] - self.velocity)

		elif key == b'd':
			self.position[0] = float(self.position[0] + self.velocity)
			self.object_position[0] = float(self.object_position[0] + self.velocity)

		elif key == b'w':
			self.position[1] = float(self.position[1] + self.velocity)
			self.object_position[1] = float(self.object_position[1] + self.velocity)

		elif key == b's':
			self.position[1] = float(self.position[1] - self.velocity)
			self.object_position[1] = float(self.object_position[1] - self.velocity)

		elif key == b'+':
			self.position[2] = float(self.position[2] - self.velocity)

		elif key == b'-':
			self.position[2] = float(self.position[2] + self.velocity)

		elif key == b'.':
			self.position[2] = 10
			self.position[1] = 0
			self.position[0] = 0


	def especial_keys_filter(self, key):

		if key == GLUT_KEY_UP:
			self.object_position[1] = float(self.object_position[1] + self.velocity)

		elif key == GLUT_KEY_DOWN:
			self.object_position[1] = float(self.object_position[1] - self.velocity)

		elif key == GLUT_KEY_LEFT:
			self.object_position[0] = float(self.object_position[0] - self.velocity)
				
		elif key == GLUT_KEY_RIGHT:
			self.object_position[0] = float(self.object_position[0] + self.velocity)