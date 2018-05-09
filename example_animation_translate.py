# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.object import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
from classes.objetos.cylinder import *
from classes.objetos.complex_object import *
from classes.objetos.animacoes.rotation import *
from classes.objetos.animacoes.translate import *

'''
Função Principal
'''
def main():

	'''
	As transformações dos objetos (translate, rotate, scale)podem ser chamadas em 
	um único eixo ou todos ao mesmo tempo.
	'''

	main_window  = Window('FireOpenGL', 720, 590)
	main_window.background = [0.6, 0.76, 0.8, 1]
	main_window.camera.position[2] = 20
	

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

	'''
	Definição dos objetos simples
	'''
	# SPHERE
	# PARAMETROS: radius, x, y, z, color = (1, 1, 1)opcional
	bola = Sphere(0.2, 0, 0, 0)
	bola.scaleU(.4)
	bola.animation = Translate('x', 0, 4, True)

	# SPHERE
	# PARAMETROS: radius, x, y, z, color = (1, 1, 1)opcional
	bola2 = Sphere(0.2, 0, 0, .6)
	bola2.scaleU(.4)
	bola.animation = Translate('x', 0, 4)

	#CYLLINDER
	# PARAMETROS: base, top, height, x, y, z, color = (1, 1, 1)opcional
	base = Cylinder(.02, .4, .6)
	base.animation = Translate('y', 0, 0.5, False, 0.001)


	# ---------------------------------------------------------------

	'''
	Definição de Objetos Complexos
	'''
	# COMPLEX OBJECT
	# PARAMETROS: objects, position
	bastonete = ComplexObject([bola2,bola,base], [0, 0, 0])
	bastonete.scaleU(2)
	bastonete.animation = Rotation('y', 1, 360, True)

	# COMPLEX OBJECT
	# PARAMETROS: objects, position
	dna = ComplexObject([], [0, 0, 0]) 

	bastonetes = [None] * 10 #Criar um array vazio com 10 posições

	for i in range(10):
		bastonetes[i] = bastonete.clone()
		bastonetes[i].objects[0].color = cores[9-i]
		bastonetes[i].x = 1
		bastonetes[i].y = i * 0.8
		bastonetes[i].z = 0
		bastonetes[i].animation.degree = 1 + (i * 0.009)
		dna.objects.append(bastonetes[i])

	dna2 = dna.clone() #Cria um clone do objeto dna
	
	dna2.rotateX(90)
	
	
	# ---------------------------------------------------------------------------------

	main_window.lights_disable()
	main_window.show()
	main_window.objects = [dna1, dna2]

if __name__ == '__main__': main()