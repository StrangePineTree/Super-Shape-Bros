import pygame
from keys import *

p1ML, p1MR, p1D, p2ML, p2MR, p2D = False, False, False, False, False, False
def getInputs(p1,p2,event):
    global p1ML, p1MR, p1D, p2ML, p2MR, p2D
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        exit(0)


    if event.type == pygame.KEYDOWN:
        if keys[p1left]: #3 kinds of input types, key down, key up, and active while key is held down
            p1ML = True
        if keys[p1right]:
            p1MR = True
        if keys[p1down]:
            p1D = True
        if keys[p1jump]:
            p1.jump()

        if keys[p2jump]:
            p2.jump()
        if keys[p2left]:
            p2ML = True
        if keys[p2right]:
            p2MR = True
        if keys[p2down]:
            p2D = True

    if event.type == pygame.KEYUP:
        if event.key == p1left:
            p1ML = False
        if event.key == p1right:
            p1MR = False
        if event.key == p1down:
            p1D = False

        if event.key == p2left:
            p2ML = False
        if event.key == p2right:
            p2MR = False
        if event.key == p2down:
            p2D = False

def playerMovements(p1,p2):
    if p1ML:
        p1.left()
    if p1MR:
        p1.right()
    if p2ML:
        p2.left()
    if p2MR:
        p2.right()