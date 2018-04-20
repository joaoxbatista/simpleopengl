#-*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from pprint import pprint

class Object(object):
	
	'''
	Atributos
	-----------------------------------------------------------------
	'''
	x = 0
	y = 0
	z = 0
	
	color = (1, 1, 1)

	transform = {
		"translate" : [[0, 0, 0]],
		"rotate"    : [[0, 0, 0, 0]],
		"scale"     : []
	}

	'''
	Métodos
	-----------------------------------------------------------------
	'''
	def __init__(self, x, y, z, color = (1, 1, 1)):
		self.x = x
		self.y = y
		self.z = z
		self.color = color

	'''
	Realiza a chamada do conjunto de transformações
	'''
	def draw(self):
		print("X: %i, Y: %i e Z: %i" % (self.x, self.y, self.z))
		print("Tramsformações: ")
		pprint(self.transform)

	'''
	Realiza a chamada do conjunto de transformações
	'''
	def transformations(self):
		for translate in reversed(self.transform['translate']):
			glTranslate(translate[0], translate[1], translate[2])
			# pprint(translate)
		for rotate in reversed(self.transform['rotate']):
			glRotate(rotate[0], rotate[1], rotate[2], rotate[3])
			# pprint(rotate)
		for scale in reversed(self.transform['scale']):
			glScale(scale[0], scale[1], scale[2])
			# pprint(scale)