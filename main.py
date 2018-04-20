# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.object import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
'''
Função Principal
'''
def main():

	obj1 = Cube(1, 0.5, 0, 0, (0, 1, 0))
	obj1.transform["rotate"].append([90, 1, 0, 1])
	obj1.transform["scale"].append([0.1, 0.1, 0.1])

	obj2 = Sphere(0.2, 0, 0, 0, (1, 0, 0))

	main_window  = Window('FireOpenGL', 720, 590)
	main_window.background = [0.45, 0.76, 0.8, 1]
	main_window.objects = [obj2, obj1]	
	main_window.show()


if __name__ == '__main__': main()