# -*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from pprint import pprint

class Light(object):
	
	def __init__(self, ambient, diffuse, specular, position):
		self.ambient = ambient
		self.diffuse = diffuse
		self.specular = specular
		self.position = position

	def active(self):
		glLightfv(GL_LIGHT1, GL_AMBIENT, self.ambient)
		glLightfv(GL_LIGHT1, GL_DIFFUSE, self.diffuse)
		glLightfv(GL_LIGHT1, GL_SPECULAR, self.specular)
		glLightfv(GL_LIGHT1, GL_POSITION, self.position)
		glEnable(GL_LIGHT1)

	def desactive(self):
		glDisable(GL_LIGHT1)