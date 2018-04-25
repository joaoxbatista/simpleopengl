# -*- coding: utf-8 -*-

class Light(object):

	ambient
	diffuse
	specular
	position
	
	def __init__(self, ambient, diffuse, specular, position):
		 # Define os parametros da luz de número 1
	    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1)
	    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1 )
	    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1 )
	    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1 )