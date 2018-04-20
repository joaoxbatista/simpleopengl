# -*- coding: utf-8 -*-
import sys
from OpenGL.GLUT import *
from OpenGL.GL import *

class Window(object):

	'''
	Lista de Tarefas
	-----------------------------------------------------------------
	1 - Possiblidade de adicionar objetos a janela (X)
	2 - Possibilidade de adicionar luzes           ()
	3 - Possibilidade de configurar material       ()  
	'''

	'''
	Atributos
	-----------------------------------------------------------------
	'''
	title = ""
	height = 420
	width = 640
	background = [1, 1, 1, 1]
	objects = []

	'''
	Métodos
	-----------------------------------------------------------------
	'''

	'''
	Construtor
	'''
	def __init__ (self, title, height, width):
		
		self.title = title
		self.height = height
		self.width = width

	'''
	Exibe a janela
	'''
	def show(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
		glutInitWindowSize(self.height, self.width)
		glutCreateWindow(self.title)
		glutDisplayFunc(self.display)
		
		'''
		Chamada das configurações
		''' 
		self.material()
		self.light()

		glutMainLoop()

	'''
	Método que exibe os objetos da janela
	''' 
	def display(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		for object in reversed(self.objects):
			object.draw()
		glutSwapBuffers()


	'''
	Configurações de iluminação
	''' 
	def light(self):
		glClearColor(self.background[0], self.background[1], self.background[2], self.background[3])
		lightZeroPosition = [10,4,10,1]
		lightZeroColor = [0.9,0.9,0.9,1.0]
		glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
		glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
		glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.2)
		glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
		glEnable(GL_LIGHT0)

	'''
	Configurações dos materiais
	''' 
	def material(self):
		glShadeModel(GL_SMOOTH)
		glEnable(GL_CULL_FACE)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_LIGHTING)
 
 	'''
	Adiciona objetos ao conjunto de objetos
	''' 
	def addObject(self, object):
		self.objects.append(object)