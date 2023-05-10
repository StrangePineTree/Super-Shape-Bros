import pygame
from settings import *

def levelSetUp(screen):
    global platformList,sX,sY
    sX, sY = screen.get_size()
    platformList= []
    from menu import mapchoice
    #set of if statements to set up platform lists
    #everything will be run as if game is 1980x1080 but will be scaled to fit screen (might be pygame function to scale everything) will also have to do this for menus
    if mapchoice == "rooftops":
        platformList = [
            pygame.Rect(100, 780, 400, 50),
            pygame.Rect(300, 580, 100, 250),
            pygame.Rect(400, 580, 300, 30)
        ]
    if mapchoice == "alley":
        platformList = [
            pygame.Rect(-300, sY-300, sX+600, 50)
        ]

    #continue this for every map

def drawLevel(screen):
    screen.fill((50,50,75))
    for platform in platformList:#draws all platforms in a list
        pygame.draw.rect(screen, (100, 100, 100), platform)

def displayStats(screen):
    pass
    #show percentages, shapes, and lives here
