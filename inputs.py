import pygame
from keys import *

def getInputs(p1,p2,event):
    keys = pygame.key.get_pressed()
    if keys[p1left]: #3 kinds of inputy types, key down, key up, and active while key is held down
        p1.left()
    if keys[p1right]:
        p1.right()
    if keys[p1jump]:
        p1.jump()
    if keys[p1down]:
        pass

    if keys[p2left]:
        p2.left()
    if keys[p2right]:
        p2.right()
    if keys[p2jump]:
        p2.jump()
    if keys[p2down]:
        pass

    if event.type == pygame.KEYDOWN:
        pass

    if event.type == pygame.KEYUP:
        pass