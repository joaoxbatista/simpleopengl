# *-* coding: utf-8 -*-

from classes.utilitarios.window import *
from classes.objetos.cube import *
from classes.objetos.sphere import *
from classes.objetos.cylinder import *
from classes.objetos.complex_object import *
from classes.objetos.animacoes.rotation import *
from classes.objetos.animacoes.scale import *
from classes.objetos.animacoes.translate import *
from classes.constantes.rgb import *

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


	cube_center = Cube(.2)
	cube_center.scaleX(2)
	cube_center.rotateX(45)
	cube_center.rotateY(90)

	cylinder_1 = Cylinder(.02, .4, .6)
	cylinder_1.color = COLOR['orange']
	cylinder_1.rotateY(90)
	cylinder_1.rotateZ(45)
	cylinder_1.animation = Scale('y', 0, 1, True)

	cylinder_2 = cylinder_1.clone()
	cylinder_2.color = COLOR['pink']
	cylinder_2.rotateZ(90)

	cylinder_3 = cylinder_2.clone()
	cylinder_3.color = COLOR['purple']
	cylinder_3.rotateZ(90)

	cylinder_4 = cylinder_3.clone()
	cylinder_4.color = COLOR['lime']
	cylinder_4.rotateZ(90)

	cylinder_5 = cylinder_4.clone()
	cylinder_5.color = COLOR['white']
	cylinder_5.rotateZ(45)
	cylinder_5.scaleZ(1.5)
	cylinder_5.translateY(0.435)
	cylinder_5.translateX(-0.45)

	cylinder_6 = cylinder_5.clone()
	cylinder_6.color = COLOR['white']
	cylinder_6.rotateZ(-90)
	cylinder_6.translateY(0.01)
	

	cylinder_7 = cylinder_5.clone()
	cylinder_7.translateY(-0.88)

	cylinder_8 = cylinder_6.clone()
	cylinder_8.translateX(0.9)


	helice = ComplexObject([cylinder_1, cylinder_2,cylinder_3,cylinder_4,cylinder_5,cylinder_6,cylinder_7,cylinder_8], [0,0,0])
	

	helice.animation = Translate('y', 0.5, -0.5)

	ventilador = ComplexObject([helice], [0,0,0])
	ventilador.animation = Rotation('z', 1, 180)

	main_window.addobj(ventilador)

	main_window.lights_disable()
	main_window.show()

if __name__ == '__main__': main()