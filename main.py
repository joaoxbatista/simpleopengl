# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.object import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
from classes.objetos.cylinder import *

'''
Função Principal
'''
def main():
	# CUBE
	# PARAMETROS: size, x, y, z, color = (1, 1, 1):opcional
	obj1 = Cube(1, 0.5, 0, 0, (0, 1, 0))

	'''
	As transformações (translate, rotate, scale)podem ser chamadas em 
	um único eixo ou todos ao mesmo tempo.
	'''
	#Escalonamento separado
	obj1.scaleY(.6)
	obj1.scaleZ(.4)

	#Escalonamento unido
	obj1.scale(.2, .6, .4)
	
	#Translação separada
	obj1.tanslateX(.1)
	obj1.tanslateY(.8)
	obj1.tanslateZ(.2)

	#Translação unida
	obj1.scale(.2, .6, .4)

	#Rotação separada
	obj1.rotateX(90)
	obj1.rotateY(90)
	obj1.rotateX(90)
	obj1.rotateZ(90)
	
	# SPHERE
	# PARAMETROS: radius, x, y, z, color = (1, 1, 1)opcional
	obj2 = Sphere(0.2, 0, 0, 0, (1, 0, 0))
	obj2.scaleU(.1)


	#CYLLINDER
	obj3 = Cylinder(.2, .4, .6, .4, .2, 0, [1, 0.2, .4])
	obj3.rotateX(90)
	obj3.scaleX(.2)
	obj3.scaleY(.2)

	main_window  = Window('FireOpenGL', 720, 590)
	main_window.background = [0.6, 0.76, 0.8, 1]
	main_window.objects = [obj3, obj2, obj1]
	main_window.show()


if __name__ == '__main__': main()