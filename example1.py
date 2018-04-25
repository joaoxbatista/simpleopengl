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
	
	cube1 = Cube(1, 0, 0, 0)
	cube1.scaleZ(.05)
	cube1.rotateY(90)
	cube1.color = [0, .8, .2]

	cube2 = Cube(1, 1, 0, 0)
	cube2.scaleZ(.05)
	cube2.rotateY(90)
	cube2.color = [0, .8, .2]

	cube3 = Cube(1, .5, 0.5, -.5)
	cube3.scaleZ(.05)
	cube3.scaleY(2)
	cube3.color = [0, .8, .2]

	cube4 = Cube(1, .5, -.5, .1)
	cube4.scaleZ(.05)
	cube4.rotateX(-90)
	cube4.scaleY(1.2)
	cube4.color = [0, .8, .2]

	cube6 = Cube(1, .5, .5, .1)
	cube6.scaleZ(.05)
	cube6.rotateX(-90)
	cube6.scaleY(1.2)
	cube6.color = [0, .8, .2]

	cube5 = Cube(1, .5, 1, .12)
	cube5.scaleZ(.05)
	cube5.scaleY(1.6)
	cube5.rotateX(-50)
	cube5.color = [0, .8, .2]

	cylinder1 = Cylinder(.03, 1, 1)
	cylinder1.color = [0, .8, .2]
	cylinder1.rotateX(90)
	cylinder1.translateZ(.67)
	cylinder1.translateY(.5)
	cylinder1.translateX(.1)

	cylinder2 = Cylinder(.03, 1, 1)
	cylinder2.color = [0, .8, .2]
	cylinder2.rotateX(90)
	cylinder2.translateZ(.67)
	cylinder2.translateY(.5)
	cylinder2.translateX(.9)

	main_window  = Window('FireOpenGL', 720, 590)
	main_window.background = [0.6, 0.76, 0.8, 1]
	main_window.objects = [cube1, cube2, cube3, cube4, cube5, cube6, cylinder1, cylinder2]
	main_window.show()


if __name__ == '__main__': main()
