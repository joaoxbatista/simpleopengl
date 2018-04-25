# -*- coding: utf-8 -*-
import sys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from camera import *

class Window(object):

	'''
	Lista de Tarefas
	-----------------------------------------------------------------
	1 - Possiblidade de adicionar objetos a janela (X)
	2 - Possibilidade de adicionar luzes           ()
	3 - Possibilidade de configurar material       ()
	4 - Possibilitar adicionar camera              (X)  
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
	camera = Camera([0.0, 0.0, 4.0], [0.0, 0.0, 0.0])

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
		glutKeyboardFunc(self.normal_keys_filter)
		glutSpecialFunc(self.especial_keys_filter)
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
		
		self.camera.active()
		self.light()
		
		glPushMatrix()
		for object in self.objects:
			object.draw()
		glPopMatrix()

		glutSwapBuffers()
		glFlush()                 

	'''
	Funções para filtar as teclas
	'''
	def normal_keys_filter(self, key, x, y):
		self.camera.normal_keys_filter(key)
		self.display()
		
	def especial_keys_filter(self, key, x, y):
		self.camera.especial_keys_filter(key)
		self.display()
	'''
	Configurações de iluminação
	''' 
	def light(self):
		glClearColor(self.background[0], self.background[1], self.background[2], self.background[3])

		lightZeroPosition = [10,4,10,1]
		lightZeroColor = [0.9,0.9,0.9,1.0]

		#Capacidade de brilho do material
		especularidade=[.1,.4,.5,1]
		especMaterial = 120

		#  Define a refletância do material
		glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, especularidade)
		#  Define a concentração do brilho
		glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

		# Ativa o uso da luz ambiente
		# glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2,0.2,0.2,0.2])

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