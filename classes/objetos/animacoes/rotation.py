# -*- coding: utf-8 -*-
from animation import Animation 
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Rotation(Animation):

	frames = 0
	reverse = False
	flag = True
	degree = 0
	limit_degree = 0
	axis = 'x'

	def __init__(self, axis, degree, limit_degree = 0, reverse = False):
		self.axis = axis
		self.degree = degree
		self.limit_degree = limit_degree
		self.reverse = reverse

	def animate(self):
		#GRAUS RESULTANTE DA MULTIPLICAÇÃO DA VELOCIDADE DA ROTAÇÃO
		degree_result = self.frames * self.degree

		#CASO A ANIMAÇÃO POSSUA A PROPRIEDADE DE VOLTAR PARA O ESTADO INICIAL
		if(self.reverse):
			self.reversed(degree_result)
		#CASO ELA SIGA O FLUXO NORMAL
		else:
			self.normal(degree_result)

		if(self.axis == 'x'):
			glRotate(degree_result, 1, 0, 0)

		elif(self.axis == 'y'):
			glRotate(degree_result, 0, 1, 0)

		elif(self.axis == 'z'):
			glRotate(degree_result, 0, 0, 1)

	def reversed(self, degree_result):
		if(degree_result >= self.limit_degree and self.flag):
			self.flag = False

		if(not self.flag and degree_result <= 0):
			self.flag = True

		if(self.flag):
			self.frames += 1
		else: 
			self.frames -= 1

	def normal(self, degree_result):
		if(degree_result <= 360):
			self.frames += 1
		else:
			self.frames = 0
