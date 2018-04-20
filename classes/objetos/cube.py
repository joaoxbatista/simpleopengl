# *-* coding: utf-8 -*-

from object import *

class Cube(Object):

	'''
	Atributos
	-----------------------------------------------------------------
	'''
	size = 1

	'''
	Métodos
	-----------------------------------------------------------------
	'''
	def __init__(self, size, x, y, z, color = (1, 1, 1)):
		super(Cube, self).__init__(x, y, z, color)
		self.size = size

	def draw(self):
		print("Cube draw method")
		super(Cube, self).draw()
		glPushMatrix()
		glMaterialfv(GL_FRONT,GL_DIFFUSE,self.color)
		glTranslate(self.x, self.y, self.z)
		self.transformations()
		glutSolidCube(self.size)
		glPopMatrix()