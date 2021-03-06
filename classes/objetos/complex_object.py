# -*- coding: utf-8 -*-

from object import *

class ComplexObject(Object):

	objects = []

	def __init__(self, objects, position):
		self.objects = objects
		super(ComplexObject, self).__init__(position[0], position[1], position[2])
		

	def draw(self):
		glPushMatrix()
		
		glTranslate(self.x, self.y, self.z)
		
		self.transformations()
		
		if(self.animation):
			print("ANIMATE - CLASS COMPLEXOBJECT")
			self.animation.animate()
			for child in self.objects:
				child.draw()
			glutPostRedisplay()
			
		else:
			for child in self.objects:
				child.draw()
		
			
		glPopMatrix()

	