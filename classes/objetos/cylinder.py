# *-* coding: utf-8 -*-

from object import *

class Cylinder(Object):

	'''
	Atributos
	-----------------------------------------------------------------
	'''
	base = 0
	top = 0
	height = 0
	slices = 20
	stacks = 10

	'''
	Métodos
	-----------------------------------------------------------------
	'''
	def __init__(self, base, top, height, x = 0 , y = 0, z = 0, color = (1, 1, 1)):
		super(Cylinder, self).__init__(x, y, z, color)
		self.base = base
		self.top = top
		self.height = height

	def draw(self):
		
		print([self.base, self.top, self.height, self.slices, self.stacks])
		glPushMatrix()
		glMaterialfv(GL_FRONT,GL_DIFFUSE,self.color)
		glTranslate(self.x, self.y, self.z)
		self.transformations()
		glutSolidCylinder(self.base, self.height, self.slices, self.stacks)
		glPopMatrix()