# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.object import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
from classes.objetos.cylinder import *
from classes.constantes.rgb import *

'''
Função Principal
'''
def main():
	'''
	Definição da janela
	'''
	main_window  = Window('FireOpenGL', 720, 590)
	main_window.background = [0.6, 0.76, 0.8, 1]
	
	'''
	Definição dos objetos
	'''
	parede_lateral_esquerda = Cube(1, 0, 0, 0, COLOR_BLUE)
	parede_lateral_esquerda.scaleZ(.05)
	parede_lateral_esquerda.rotateY(90)
	main_window.addobj(parede_lateral_esquerda)

	parede_lateral_direita = Cube(1, 1, 0, 0, COLOR_BLUE)
	parede_lateral_direita.scaleZ(.05)
	parede_lateral_direita.rotateY(90)
	main_window.addobj(parede_lateral_direita)

	parede_trazeira = Cube(1, .5, 0.5, -.5, COLOR_BLUE)
	parede_trazeira.scaleZ(.05)
	parede_trazeira.scaleY(2)
	main_window.addobj(parede_trazeira)

	piso = Cube(1, .5, -.5, .1, COLOR_BLUE2)
	piso.scaleZ(.05)
	piso.rotateX(-90)
	piso.scaleY(1.2)
	main_window.addobj(piso)

	telhado = Cube(1, .5, 1, .12, COLOR_BLUE)
	telhado.scaleZ(.05)
	telhado.scaleY(1.6)
	telhado.rotateX(-50)
	main_window.addobj(telhado)

	teto = Cube(1, .5, .5, .1, COLOR_BLUE)
	teto.scaleZ(.05)
	teto.rotateX(-90)
	teto.scaleY(1.2)
	main_window.addobj(teto)


	pilar_esqueda = Cylinder(.03, 1, 1, 0, 0, 0, COLOR_BLUE)
	pilar_esqueda.rotateX(90)
	pilar_esqueda.translateZ(.67)
	pilar_esqueda.translateY(.5)
	pilar_esqueda.translateX(.1)
	main_window.addobj(pilar_esqueda)

	pilar_direita = Cylinder(.03, 1, 1, 0, 0, 0, COLOR_BLUE)
	pilar_direita.rotateX(90)
	pilar_direita.translateZ(.67)
	pilar_direita.translateY(.5)
	pilar_direita.translateX(.9)
	main_window.addobj(pilar_direita)
	
	
	ambiente=[1.0,0.0,0.0,1.0]
	difusa=[1.0,0.0,1.0,1.0]
	especular = [1.0, 0.0, 1.0, 1.0] 
	position=[1.0, 20.0, -20.0]

	light1 = Light(ambiente, difusa, especular, position)
	main_window.addlight(light1)


	main_window.lights_disable()
	
	main_window.show()


if __name__ == '__main__': main()
