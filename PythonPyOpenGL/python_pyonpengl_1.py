#!/usr/bin/env python3
# -*- utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 12 July, 2017
#
import sys
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("SolidSphere")
    glutSolidSphere(1.0, 8, 8)
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("WireTeapot")
    glutWireTeapot(0.75)
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("SolidTeapot")
    glutSolidTeapot(0.5)
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("SolidTorus")
    glutSolidTorus(0.175, 0.45, 6, 6)
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("WireCube")
    glutWireCube(1.0)
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("SolidCube")
    glutSolidCube(1.0)
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("SolidOctahedron")
    glutSolidOctahedron()
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("WireOctahedron")
    glutWireOctahedron()
    glFlush()
    time.sleep(1)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSetWindowTitle("SolidTetrahedron")
    glutSolidTetrahedron()
    glFlush()

def main(argv):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(640,480)
    glutCreateWindow(b"First")
    glutSetWindowTitle(b"First Second")
    glutDisplayFunc(drawFunc)
    glutMainLoop()

if __name__ == '__main__':
    main(sys.argv)
