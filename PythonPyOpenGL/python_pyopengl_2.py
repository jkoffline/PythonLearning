#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://eyehere.net/2011/learn-opengl-3d-by-pyopengl-4/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 12 July, 2017
#

import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glEnd()
    glFlush()
    time.sleep(1)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glEnd()
    glFlush()
    time.sleep(1)

    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.3, 0.3)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.6, 0.6)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.9, 0.9)
    glEnd()
    glFlush()
    time.sleep(1)

    glColor3f(1.0, 1.0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.2, 0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, 0.2)
    glEnd()
    glFlush()
    time.sleep(1)
    
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.75)
    glVertex2f(0.5, 0.75)
    glEnd()
    glFlush()
    time.sleep(1)

    glBegin(GL_LINES)
    glVertex2f(0.25, 0.5)
    glVertex2f(0.25, -0.25)
    glEnd()
    glFlush()
    time.sleep(1)

    glColor3f(0.0, 1.0, 1.0)
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.8, -0.3)
    glVertex2f(-0.8, -0.6)
    glVertex2f(-0.5, -0.8)
    glVertex2f(-0.2, -0.6)
    glVertex2f(-0.2, -0.3)
    glEnd()
    glFlush()
    time.sleep(1)

    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_POLYGON)
    glVertex2f(0.5, -0.1)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.2, -0.6)
    glVertex2f(0.5, -0.8)
    glVertex2f(0.8, -0.6)
    glVertex2f(0.8, -0.3)
    glEnd()
    glFlush()
    time.sleep(1)

    glBegin(GL_LINES)
    glVertex2f(-0.75, 0.75)
    glVertex2f(-0.75, -0.25)
    glEnd()
    glFlush()

def main(argv):
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b"Quadrant")
    glutDisplayFunc(drawFunc)
    init()
    glutMainLoop()

if __name__ == '__main__':
    main(sys.argv)
