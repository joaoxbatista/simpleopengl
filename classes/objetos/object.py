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
		"scale"     : [[1, 1, 1]]
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
		self.transform = {
			"translate" : [],
			"rotate"    : [],
			"scale"     : []
		}

	'''
	Realiza a chamada do conjunto de transformações
	'''
	def draw(self):
		print("X: %i, Y: %i e Z: %i" % (self.x, self.y, self.z))
		print("Tramsformações: ")
		pprint(self.transform)

	'''
	Operações de transformação
	'''	

	'''
	Escalonamento
	'''
	def scaleX(self, x):
		self.transform['scale'].append([x, 1, 1])
	def scaleY(self, y):
		self.transform['scale'].append([1, y, 1])
	def scaleZ(self, z):
		self.transform['scale'].append([1, 1, z])
	def scale(self, x, y, z):
		self.transform['scale'].append([x, y, z])
	def scaleU(self, uv):
		self.transform['scale'].append([uv, uv, uv])

	'''
	Translação
	'''
	def translateX(self, x):
		self.transform['translate'].append([x, 0, 0])
	def translateY(self, y):
		self.transform['translate'].append([0, y, 0])
	def translateZ(self, z):
		self.transform['translate'].append([0, 0, z])
	def translate(self, x, y, z):
		self.transform['translate'].append([x, y, z])

	'''
	Rotação
	'''
	def rotateX(self, degree):
		self.transform['rotate'].append([degree,1, 0, 0])
	def rotateY(self, degree):
		self.transform['rotate'].append([degree,0, 1, 0])
	def rotateZ(self, degree):
		self.transform['rotate'].append([degree,0, 0, 1])
	def rotateU(self, degree):
		self.transform['rotate'].append([degree,1, 1, 1])
	def rotate(self, degreeX, degreeY, degreeZ):
		self.transform['rotate'].append([degreeX,1, 0, 0])
		self.transform['rotate'].append([degreeY,0, 1, 0])
		self.transform['rotate'].append([degreeZ,0, 0, 1])

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