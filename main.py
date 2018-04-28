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

	'''
	As transformações dos objetos (translate, rotate, scale)podem ser chamadas em 
	um único eixo ou todos ao mesmo tempo.
	'''

	main_window  = Window('FireOpenGL', 720, 590)
	main_window.background = [0.6, 0.76, 0.8, 1]

	# CUBE
	# PARAMETROS: size, x, y, z, color = (1, 1, 1):opcional
	obj1 = Cube(1, 0.5, 0, 0, (0, 1, 0))

	
	#Escalonamento separado
	obj1.scaleY(.6)
	obj1.scaleZ(.4)

	#Escalonamento unido
	obj1.scale(.2, .6, .4)
	
	#Translação separada
	obj1.translateX(.1)
	obj1.translateY(.8)
	obj1.translateZ(.2)

	#Translação unida
	obj1.scale(.2, .6, .4)

	#Rotação separada
	obj1.rotateX(90)
	obj1.rotateY(90)
	obj1.rotateX(90)
	obj1.rotateZ(90)

	main_window.addobj(obj1)
	
	# ---------------------------------------------------------------------------------
	
	# SPHERE
	# PARAMETROS: radius, x, y, z, color = (1, 1, 1)opcional
	obj2 = Sphere(0.2, 0, 0, 0, (1, 0, 0))
	obj2.scaleU(.1)
	main_window.addobj(obj2)

	# ---------------------------------------------------------------------------------

	#CYLLINDER
	obj3 = Cylinder(.2, .4, .6, .4, .2, 0, [1, 0.2, .4])
	obj3.rotateX(90)
	obj3.scaleX(.2)
	obj3.scaleY(.2)
	main_window.addobj(obj3)
	
	# ---------------------------------------------------------------------------------
	#LIGHT

	luzAmbiente1=[1.0,0.0,0.0,1.0]
	luzDifusa1=[1.0,0.0,1.0,1.0]
	luzEspecular1 = [1.0, 0.0, 1.0, 1.0] 
	posicaoLuz1=[1.0, 20.0, -20.0]
	light1 = Light(luzAmbiente1, luzDifusa1, luzEspecular1, posicaoLuz1)
	main_window.addlight(light1)



	main_window.lights_disable()
	main_window.show()

if __name__ == '__main__': main()