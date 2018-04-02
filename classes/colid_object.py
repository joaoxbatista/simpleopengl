#-*- coding: utf-8 -*-
class ColidObject(object):
	
	x = 0.0
	y = 0.0
	z = 0.0

	height = 0.0
	width = 0.0
	depth = 0.0

	velocity = 0.2
	color = [1.0,0.0,0.0,1.0]

	def __init__(self, x, y, z, width, height, depth):
		self.x = x
		self.y = y
		self.z = z
		self.width = width
		self.height = height
		self.depth = depth

	def colid(self, object):
		#Informações do objeto 
		right_side_a = self.x + float(self.width/1.8) 
		left_side_a = self.x - float(self.width/1.8)
		top_side_a = self.y - float(self.height/1.8)
		bottom_side_a = self.y + float(self.height/1.8)
		front_side_a = self.z + float(self.depth/1.8)
		back_side_a = self.z - float(self.depth/1.8)


		#Informações do objeto a ser verificado
		right_side_b = object.x + float(object.width/1.8)
		left_side_b = object.x - float(object.width/1.8)
		top_side_b = object.y - float(object.height/1.8)
		bottom_side_b = object.y + float(object.height/1.8)
		front_side_b = object.z + float(object.depth/1.8)
		back_side_b = object.z - float(object.depth/1.8)

		cRight = False
		cLeft = False
		cBottom = False
		cTop = False
		cFront = False
		cBack = False

		# print("LADO DE CIMA DE A ="+ str(top_side_a) + " <= LADO DE BAIXO DE B = " + str(bottom_side_b))
		# print("LADO DE BAIXO DE A ="+ str(bottom_side_a) + " >= LADO DE CIMA DE B = " + str(top_side_b))

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

		# print("--------------------------------")
		
		if(cBack and cFront and cLeft and cRight and cTop and cBottom):
			return True
		else:
			return False
	
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