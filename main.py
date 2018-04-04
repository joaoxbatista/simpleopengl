#-*- coding: utf-8 -*-
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from classes.colid_object import *
from classes.colid_object_group import *
import sys
import numpy

'''
Variáveis globais
'''
name = 'Sistema de Colisão'
 
sphere_object = ColidObject(0, 2, 2, 0.2, 0.2, 0.2) #x, y, z, width, height, depth
sphere_object.blue = 1
sphere_object.green = 1
sphere_object.red = 1

sphere_object_fixed = ColidObject(1, 0, -4, 0.4, 0.4, 0.4) #x, y, z, width, height, depth
sphere_object_fixed.red = 1

sphere_object_fixed2 = ColidObject(3, 0, -4, 0.6, 0.6, 0.6) #x, y, z, width, height, depth
sphere_object_fixed2.green = 1


sphere_object_fixed3 = ColidObject(-3, 0, -4, 1, 1, 1) #x, y, z, width, height, depth
sphere_object_fixed3.green = 0.5
sphere_object_fixed3.red = 0.2
sphere_object_fixed3.blue = 0.8


'''
Grupo de Objetos Colisivos 
'''
fixed_spheres = ColidObjectGroup([sphere_object_fixed, sphere_object_fixed2, sphere_object_fixed3])

sphere_object.arround_objects = fixed_spheres #adiciona a esfera um grupo de objetos que ela pode colidir



'''
Função principal
'''
def main():
	window()
	material()
	light()
	camera()
	glPushMatrix()
	glutMainLoop()
	return




'''
Função para desenhar a janela
'''
def window():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(400, 400)
	glutCreateWindow(name)
	glutKeyboardFunc(normal_keys_filter)
	glutSpecialFunc(especial_keys_filter)
	glutDisplayFunc(display)
	return




'''
Função para configurar a camera
'''
def camera():
	glMatrixMode(GL_PROJECTION)
	gluPerspective(40.,1.,1.,40.)
	glMatrixMode(GL_MODELVIEW)
	gluLookAt(0,0,10,
	          0,0,0,
	          0,1,0)




'''
Função para configurar o aspecto do material
'''
def material():
	glShadeModel(GL_SMOOTH)
	glEnable(GL_CULL_FACE)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)




'''
Função para configurar a iluminação
'''
def light():
	glClearColor(0, 0, 0, 0)
	lightZeroPosition = [1,4,10,1]
	lightZeroColor = [0.9,0.9,0.9,1.0]
	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.2)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	glEnable(GL_LIGHT0)




'''
Função para configurar a exibição
'''
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw()
    glutSwapBuffers()
    return




'''
Funções para filtar as teclas normais do teclado
'''
def normal_keys_filter(key, x, y):
	global sphere_object
	sphere_object.keys_filter(key) #Captura a tecla pressionada e repassa para objeto
	display()
	glutPostRedisplay()

def especial_keys_filter(key, x, y):
	global sphere_object
	sphere_object.especial_keys_filter(key) #Captura a tecla pressionada e repassa para objeto
	display()
	glutPostRedisplay()




'''
Função para desenhar os objetos
'''
def draw():
	global sphere_object
	global sphere_object_fixed
	global sphere_object_fixed2
	global sphere_object_fixed3

	sphere_object.draw_sphere()
	sphere_object_fixed.draw_sphere()
	sphere_object_fixed2.draw_sphere()
	sphere_object_fixed3.draw_sphere()


if __name__ == '__main__': main()
