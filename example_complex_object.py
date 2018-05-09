# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.object import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
from classes.objetos.cylinder import *
from classes.objetos.complex_object import *
from classes.objetos.animacoes.rotation import *

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
	bola = Sphere(0.2, 0, 0, 0, (1, 1, 1))
	bola.scaleU(.4)

	bola2 = Sphere(0.2, 0, 0, .6, (1, 0, 0))
	bola2.scaleU(.4)

	#CYLLINDER
	# PARAMETROS: base, top, height, x, y, z, color = (1, 1, 1)opcional
	base = Cylinder(.02, .4, .6)

	# COMPLEX OBJECT
	# PARAMETROS: objects, position
	pirulito = ComplexObject([bola2,bola,base], [0, 0, 0])
	pirulito.rotateZ(45)
	pirulito.scaleU(2)
	pirulito.translateY(1)
	pirulito.animation = Rotation('x', 1)
	main_window.addobj(pirulito)

	pirulito2 = pirulito.clone()
	pirulito2.objects[0].color = (0, 1, 0)
	pirulito2.animation = Rotation('y', 1, 180, True)
	pirulito2.x += 1
	pirulito2.y += 1
	pirulito2.z += 0
	main_window.addobj(pirulito2)

	pirulito3 = pirulito2.clone()
	pirulito3.rotateX(90)
	pirulito3.objects[0].color = (0, 0, 1)
	pirulito3.animation = Rotation('x', 1)
	pirulito3.x += 1
	pirulito3.y += 1
	pirulito3.z += 0
	main_window.addobj(pirulito3)

	pirulito4 = pirulito3.clone()
	pirulito4.rotateX(90)
	pirulito4.objects[0].color = (1, 0, 1)
	pirulito4.animation = Rotation('x', 1)
	pirulito4.x -= 2
	pirulito4.y += 1
	pirulito4.z += 0
	main_window.addobj(pirulito4)

	# ---------------------------------------------------------------------------------

	main_window.lights_disable()
	main_window.show()

if __name__ == '__main__': main()