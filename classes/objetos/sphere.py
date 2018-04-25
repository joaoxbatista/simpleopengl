# *-* coding: utf-8 -*-

from object import *

class Sphere(Object):

	'''
	Atributos
	-----------------------------------------------------------------
	'''
	radius = 1
	slices = 20
	stacks = 20
	quadric = None
	'''
	Métodos
	-----------------------------------------------------------------
	'''
	def __init__(self, radius, x, y, z, color = (1, 1, 1)):
		super(Sphere, self).__init__(x, y, z, color)
		self.radius = radius

	def draw(self):
		# print("Sphere draw method")
		# pprint(self.quadric)
		super(Sphere, self).draw()
		glPushMatrix()
		glMaterialfv(GL_FRONT,GL_DIFFUSE,self.color)
		glTranslate(self.x, self.y, self.z)
		self.transformations()
		glutSolidSphere(self.radius,self.slices,self.stacks)
		glPopMatrix()