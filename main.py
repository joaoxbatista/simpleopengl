#-*- coding: utf-8 -*-
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from classes.colid_object import *
import sys
import numpy

'''
Variáveis globais
'''
name = 'Sistema de Colisão'
 
sphere_object = ColidObject(0, 0, 0, 0.8, 0.8, 0.8) #x, y, z, width, height, depth
block_object = ColidObject(2, 2, 2, 1.0, 1.0, 1.0) #x, y, z, width, height, depth


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
	glutInitWindowSize(970,640)
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
	glClearColor(1, 1, 1, 1)
	lightZeroPosition = [1,4,10,1]
	lightZeroColor = [0.9,1.0,0.2,1.0]
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
    
	if key==chr(27):
	    sys.exit(0)

	elif key == b'w':
		sphere_object.addZ()
		if(sphere_object.colid(block_object)):
			sphere_object.decZ()
			sphere_object.decZ()
		# print('frente ' + str(sphere_object.z))    

	elif key == b's':
		sphere_object.decZ()
		if(sphere_object.colid(block_object)):
			sphere_object.addZ()
			sphere_object.addZ()
		# print('fundo ' + str(sphere_object.z))    

	else:
		print('tecla não mapeada')

	display()
	glutPostRedisplay()

def especial_keys_filter(key, x, y):
	global sphere_object
	
	if key == GLUT_KEY_UP:
		sphere_object.addY()
		if(sphere_object.colid(block_object)):
			sphere_object.decY()
			sphere_object.decY()
		# print('cima ' + str(sphere_object.y))

	elif key == GLUT_KEY_DOWN:
		sphere_object.decY()
		if(sphere_object.colid(block_object)):
			sphere_object.addY()
			sphere_object.addY()
		# print('baixo ' + str(sphere_object.y))

	elif key == GLUT_KEY_LEFT:
		sphere_object.decX()
		if(sphere_object.colid(block_object)):
			sphere_object.addX()
			sphere_object.addX()
		# print('esquerda ' + str(sphere_object.x))

	elif key == GLUT_KEY_RIGHT:
		sphere_object.addX()
		if(sphere_object.colid(block_object)):
			sphere_object.decX()
			sphere_object.decX()
		# print('direita ' + str(sphere_object.x))
	else:
		print('tecla não mapeada')

	display()
	glutPostRedisplay()




'''
Função para desenhar os objetos
'''
def draw():
	global sphere_object
	
	glPushMatrix()
	glMaterialfv(GL_FRONT,GL_DIFFUSE,sphere_object.color)
	glTranslate(sphere_object.x, sphere_object.y, sphere_object.z)
	glutSolidSphere(sphere_object.width,50,10)
	glPopMatrix()

	glPushMatrix()
	glMaterialfv(GL_FRONT,GL_DIFFUSE,sphere_object.color)
	glTranslate(block_object.x, block_object.y, block_object.z)
	glutSolidCube(block_object.width)
	glPopMatrix()



if __name__ == '__main__': main()
