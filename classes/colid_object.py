#-*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class ColidObject(object):

	
	colid_type = "sphere"
	colid_tolerance = 1.2

	arround_objects = []
	'''
	Coordenadas do Objeto
	'''
	x = 0.0
	y = 0.0
	z = 0.0

	'''
	Medidas do Objeto
	'''
	height = 0.0
	width = 0.0
	depth = 0.0

	'''
	Física do Objeto
	'''
	velocity = 0.2
	
	'''
	Cor do objeto
	'''
	red = 0.0
	blue = 0.0
	green = 0.0


	def __init__(self, x, y, z, width, height, depth):
		self.x = x
		self.y = y
		self.z = z
		self.width = width
		self.height = height
		self.depth = depth

	def keys_filter(self, key):

		if key == b'w':
			self.addZ()
			if(self.colidArround(key)):
				self.decZ()

		elif key == b's':
			self.decZ()
			if(self.colidArround(key)):
				self.addZ()

	def especial_keys_filter(self, key):
		
		if key == GLUT_KEY_UP:
			self.addY()
			if(self.colidArround(key)):
				self.decY()
				

		if key == GLUT_KEY_DOWN:
			self.decY()
			if(self.colidArround(key)):
				self.addY()
				

		if key == GLUT_KEY_LEFT:
			self.decX()
			if(self.colidArround(key)):
				self.addX()
				

		if key == GLUT_KEY_RIGHT:
			self.addX()
			if(self.colidArround(key)):
				self.decX()
				



	def colid(self, object, key):
		

		#Informações do objeto 
		right_side_a = self.x + float(self.width/self.colid_tolerance) 
		left_side_a = self.x - float(self.width/self.colid_tolerance)
		top_side_a = self.y - float(self.height/self.colid_tolerance)
		bottom_side_a = self.y + float(self.height/self.colid_tolerance)
		front_side_a = self.z + float(self.depth/self.colid_tolerance)
		back_side_a = self.z - float(self.depth/self.colid_tolerance)


		#Informações do objeto a ser verificado
		right_side_b = object.x + float(object.width/object.colid_tolerance)
		left_side_b = object.x - float(object.width/object.colid_tolerance)
		top_side_b = object.y - float(object.height/object.colid_tolerance)
		bottom_side_b = object.y + float(object.height/object.colid_tolerance)
		front_side_b = object.z + float(object.depth/object.colid_tolerance)
		back_side_b = object.z - float(object.depth/object.colid_tolerance)

		cRight = False
		cLeft = False
		cBottom = False
		cTop = False
		cFront = False
		cBack = False

		#Se o lado de cima do objeto A colidir com o o lado de baixo do objeto B
		if(top_side_a <= bottom_side_b):
			cTop = True
			print('Colidiu em cima')
		#Se o lado de baixo do objeto A colidir com o o lado de cima do objeto B
		if(bottom_side_a >= top_side_b):
			cBottom = True
			print('Colidiu em baixo')
		#Se o lado esquerdo do objeto A colidir com o o lado direito do objeto B
		if(left_side_a <= right_side_b):
			cLeft = True
			print('Colidiu na esquerda')
		#Se o lado direito do objeto A colidir com o o lado esquerdo do objeto B
		if(right_side_a >= left_side_b):
			cRight = True
			print('Colidiu na direita')
		#Se o lado da frente do objeto A colidir com o o lado trazeiro do objeto B
		if(front_side_a >= back_side_b):
			cFront = True
			print('Colidiu na frente')
		#Se o lado trazeiro do objeto A colidir com o o lado da frente do objeto B
		if(back_side_a <= front_side_b):
			cBack = True
			print('Colidiu por traz')

		if(cBack and cFront and cLeft and cRight and cTop and cBottom):

			if key == b'w':
				object.addZ()

			if key == b's':
				object.decZ()

			if key == GLUT_KEY_UP:
				object.addY()
			
			if key == GLUT_KEY_DOWN:
				object.decY()
				
			if key == GLUT_KEY_LEFT:
				object.decX()
				
			if key == GLUT_KEY_RIGHT:
				object.addX()
				
			return True
		else:
			return False
	
	def colidArround(self, key):
		return self.arround_objects.very_collid_objects(self, key)

	def addX(self):
		self.x = self.x + self.velocity
	
	def addY(self):
		self.y = self.y + self.velocity

	def addZ(self):
		self.z = self.z + self.velocity

	def decX(self):
		self.x = self.x - self.velocity
	
	def decY(self):
		self.y = self.y - self.velocity

	def decZ(self):
		self.z = self.z - self.velocity

	def color(self):
		color = [self.red, self.green, self.blue]
		return color

	def draw_sphere(self):
		glPushMatrix()
		glMaterialfv(GL_FRONT,GL_DIFFUSE,self.color())
		glTranslate(self.x, self.y, self.z)
		glutSolidSphere(self.width,50,10)
		glutPostRedisplay()
		glPopMatrix()
		return

	def draw_cube(self):
		glPushMatrix()
		glMaterialfv(GL_FRONT,GL_DIFFUSE,self.color())
		glTranslate(self.x, self.y, self.z)
		glutSolidCube(self.width)
		glutPostRedisplay()
		glPopMatrix()
		return