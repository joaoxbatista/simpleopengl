# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.object import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
from classes.objetos.cylinder import *
from classes.objetos.complex_object import *
from classes.objetos.animacoes.rotation import *
from classes.objetos.animacoes.scale import *
from classes.objetos.animacoes.translate import *
from PIL import Image as Image
import timeit
import numpy
import ctypes
import random

def read_texture(filename):
      img = Image.open(filename)
      img_data = numpy.array(list(img.getdata()), numpy.int8)
      textID = glGenTextures(1)
      glBindTexture(GL_TEXTURE_2D, textID)
      glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
      #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)    #  Opcao para Truncar a figura
      #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)      
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)   #  Opcao para repetir a figura
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
      glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
      #glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_REPLACE)
      #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
      #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_SPOT_DIRECTIONAL)
      glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
      return textID

'''
Função Principal
'''
def main():

	'''
	As transformações dos objetos (translate, rotate, scale)podem ser chamadas em 
	um único eixo ou todos ao mesmo tempo.
	'''

	main_window  = Window('FireOpenGL', 720, 590)
	main_window.background = [.8,.8,.8, 1]
	main_window.camera.position[2] = 10
	main_window.camera.position[0] = 10
	
	ambiente=[0,0,0,1]
	difusa=[.4,.4,.4,1]
	especular = [1, 1, 1, 1] 
	position=[1, 20, 10]

	light1 = Light(ambiente, difusa, especular, position)
	light2 = light1
	light2.ambient[2] = 1
	main_window.addlight(light1)
	main_window.addlight(light2)

	# ---------------------------------------------------------------------------------

	cores = [
		(0.67, 0.8, 0.91),
		(0.57, 0.58, 0.79),
		(0.62, 0.81, 0.71),
		(0.66, 0.7, 0.69),
		(0.8, 0.71, 0.42),
		(1.0, 0.84, 0.01),
		(0.9, 0.4, 0.4),
		(0.96, 0.49, 0.26),
		(0.68, 0.44, 0.69),
		(0.03, 0.42, 0.71)]

	# SPHERE
	# PARAMETROS: radius, x, y, z, color = (1, 1, 1)opcional
	bola = Sphere(0.2, 0, 0, 0, (0, 0, 0))
	bola.scaleU(.4)


	# bola.animation = Translate('y', -1.5, 1.5)

	bola2 = Sphere(0.2, 0, 0, .6, (1, 0, 0))
	bola2.scaleU(.4)
	bola2.animation = Scale('u', 0.4, 1.5, True)

	#CYLLINDER
	# PARAMETROS: base, top, height, x, y, z, color = (1, 1, 1)opcional
	base = Cylinder(.02, .4, .6)
	# base.animation = Scale('y', 0, 1, False)

	# COMPLEX OBJECT
	# PARAMETROS: objects, position
	bastonete = ComplexObject([bola2,bola,base], [0, 0, 0])
	bastonete.scaleU(2)
	bastonete.animation = Rotation('x', 1, 180, False)

	bastonetes = [None] * 20

	dna = ComplexObject([], [0, 0, 0])

	for i in range(10):
		bastonetes[i] = bastonete.clone()
		bastonetes[i].objects[0].color = cores[9-i]
		bastonetes[i].x = i * 0.8
		bastonetes[i].y = (i * i * 1) * 0.1
		bastonetes[i].z = (i * i) * 0.1
		# bastonetes[i].objects[0].scaleU(1 + (i * 0.1))
		bastonetes[i].animation.degree = 1 + (i * 0.01)

		dna.objects.append(bastonetes[i])

	dna.rotateX(90)
	# dna.animation = Rotation('z', 0.4)
	main_window.addobj(dna)
	# ---------------------------------------------------------------------------------

	main_window.lights_disable()
	main_window.show()

if __name__ == '__main__': main()