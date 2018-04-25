# -*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from pprint import pprint

class Manipulable(object):

	position = [0.0, 1.0, 0.0]
	velocity = 0.1

	def __init__(self, position):
		self.position = position

	def normal_keys_filter(self, key):
		
		print("--------------------------------")
		print("Classe: Manipulable")
		print("POSIÇAO DA CAMERA:")
		print(self.position)
		print("--------------------------------")

		if key == b'w':
			self.position[2] = float(self.position[2] + self.velocity)

		elif key == b's':
			self.position[2] = float(self.position[2] - self.velocity)
			

	def especial_keys_filter(self, key):
		
		print("--------------------------------")
		print("Classe: Manipulable")
		print("POSIÇAO DA CAMERA:")
		print(self.position)
		print("--------------------------------")

		if key == GLUT_KEY_UP:
			print("POSIÇÃO Y: " + str(self.position[1]))
			print("POSIÇÃO Y ATUALIZADA"  + str(self.position[1] + self.velocity))
			self.position[1] = float(self.position[1] + self.velocity)

		elif key == GLUT_KEY_DOWN:
			print("POSIÇÃO Y: " + str(self.position[1]))
			print("POSIÇÃO Y ATUALIZADA"  + str(self.position[1] - self.velocity))
			self.position[1] -= self.velocity

		elif key == GLUT_KEY_LEFT:
			print("POSIÇÃO Z: " + str(self.position[1]))
			print("POSIÇÃO Z ATUALIZADA"  + str(self.position[0] - self.velocity))
			self.position[0] -= self.velocity
				
		elif key == GLUT_KEY_RIGHT:
			print("POSIÇÃO Z: " + str(self.position[1]))
			print("POSIÇÃO Z ATUALIZADA"  + str(self.position[0] + self.velocity))
			self.position[0] += self.velocity