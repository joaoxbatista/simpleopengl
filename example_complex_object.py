# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.object import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
from classes.objetos.cylinder import *
from classes.objetos.complex_object import *

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
	

	# ---------------------------------------------------------------------------------

	# SPHERE
	# PARAMETROS: radius, x, y, z, color = (1, 1, 1)opcional
	bola = Sphere(0.2, 0, 0, 0, (1, 0, 0))
	bola.scaleU(.4)

	#CYLLINDER
	# PARAMETROS: base, top, height, x, y, z, color = (1, 1, 1)opcional
	base = Cylinder(.02, .4, .6)
	base.rotateX(90)

	# COMPLEX OBJECT
	# PARAMETROS: objects, position
	pirulito = ComplexObject([bola, base], [0, 0, 0])
	pirulito.rotateZ(45)
	pirulito.scaleU(2)
	pirulito.translateY(1)
	main_window.addobj(pirulito)

	# ---------------------------------------------------------------------------------

	main_window.lights_disable()
	main_window.show()

if __name__ == '__main__': main()