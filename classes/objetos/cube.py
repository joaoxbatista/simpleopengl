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
	def __init__(self, size, x = 0, y = 0, z = 0, color = (1, 1, 1)):
		super(Cube, self).__init__(x, y, z, color)
		self.size = size

	def draw(self):
		
		super(Cube, self).draw()
		
		glPushMatrix()
		glMaterialfv(GL_FRONT,GL_DIFFUSE,self.color)
		glTranslate(self.x, self.y, self.z)
		self.transformations()

		if(self.animation):
			self.animation.animate()
			glutSolidCube(self.size)
			glutPostRedisplay()
			
		else:
			glutSolidCube(self.size)	

		glPopMatrix()