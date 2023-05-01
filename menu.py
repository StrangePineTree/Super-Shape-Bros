from buttons import button
from settings import *
import pygame

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
sX, sY = screen.get_size()
mapchoice = "alley" #map choice should be set in main or something
buttonlist: list[button] = []
maplist: list[button] = []

startbutton = button((sX/2 -150, 400), (300, 150), (100,100,100))
quitbutton = button((sX/2 -150, 575), (300, 150), (100,100,100))
stockupbutton = button((sX/2- 200, 410), (50, 50), (48, 52, 70))
stockdownbutton = button((sX/2-200, 480), (50, 50), (48, 52, 70))
mapbutton = button((sX/2+160, 400), (150, 150), (100,100,100))

mapdropdown = button((sX/2+160, 400), (150, 440), (140,140,140))

map1 = button((sX/2+165, 405), (140, 140), (80,80,80))
map2 = button((sX/2+165, 550), (140, 140), (110,110,110))
map3 = button((sX/2+165, 695), (140, 140), (110,110,110))


maplist.append(mapdropdown)
maplist.append(map1)
maplist.append(map2)
maplist.append(map3)

buttonlist.append(startbutton)
buttonlist.append(quitbutton)
buttonlist.append(stockupbutton)
buttonlist.append(stockdownbutton)
buttonlist.append(mapbutton)

def Menu(screen):
    global mapchoice
    global LIVES
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
        elif e.type == pygame.MOUSEBUTTONDOWN:#interats with buttons when the mouse button is down
            for b in buttonlist:
                if b.box.collidepoint(pygame.mouse.get_pos()):
                    if b is startbutton:
                        return False
                    if b is quitbutton:
                        exit(0)
                    if b is stockupbutton and LIVES < 99:
                        LIVES+=1
                        if LIVES == 0:
                            LIVES = 1
                    if b is stockdownbutton and LIVES > -1:
                        LIVES-=1
                        if LIVES == 0:
                            LIVES = -1
                            
            for b in maplist:
                if b.box.collidepoint(pygame.mouse.get_pos()):
                    if b is map1:
                        if mapchoice != 'alley':
                            maptype = 'flat'
                            mapchoice = 'alley'
                        map1.color = (80,80,80)
                        map2.color = (110,110,110)
                        map3.color = (110,110,110)

                    if b is map2:
                        if mapchoice != 'rooftops':
                            maptype = 'floating'
                            mapchoice = 'rooftops'	
                        map1.color = (110,110,110)
                        map2.color = (80,80,80)
                        map3.color = (110,110,110)

                    if b is map3:
                        if mapchoice != '?????':
                            maptype = 'floating'
                            mapchoice = '?????'		
                        map1.color = (110,110,110)
                        map2.color = (110,110,110)
                        map3.color = (80,80,80)

    dropDown = False#sets dropdown to false unless these next lines make it true
    for b in buttonlist:
        if b.box.collidepoint(pygame.mouse.get_pos()):#if the map button is hovered over the map menu drops down
            if b is mapbutton:
                dropDown = True
    for b in maplist:
        if b.box.collidepoint(pygame.mouse.get_pos()):#if the map drop down is hovered over it stays down
            if b is mapdropdown:
                dropDown = True

    screen.fill((48, 52, 70)) #just fills the screen a certian collor

    for b in buttonlist:#draws the menu buttons
        b.draw()

    font = pygame.font.Font(None, 40)
    if dropDown == True: #draws the map buttons if drop down is true
        for b in maplist:
            b.draw()
        #draws the text for the map menu
        text = font.render(str("alley"), True, (150, 255, 255))
        screen.blit(text, (sX/2+165, 405))
        text = font.render(str("rooftops"), True, (150, 255, 255))
        screen.blit(text, (sX/2+165, 550))
        text = font.render(str("??????"), True, (150, 255, 255))
        screen.blit(text, (sX/2+165, 695))
    if dropDown == False:
        font = pygame.font.Font(None, 40)
        text = font.render(str(mapchoice), True, (150, 255, 255))
        screen.blit(text, (sX/2+165,405))
    #draws the text for the rest of the menu
    font = pygame.font.Font(None, 100)
    text = font.render(str('QUIT'), True, (150, 255, 255))
    screen.blit(text, (sX/2-90,620))
    text = font.render(str('PLAY'), True, (150,255,255))
    screen.blit(text, (sX/2-90,450))
    font = pygame.font.Font(None, 190)
    text = font.render(str('SUPER SHAPE BROS'), True, (150,255,255))
    screen.blit(text, (250,50))
    font = pygame.font.Font(None, 40)
    text = font.render(str(LIVES), True, (150,255,255))
    screen.blit(text, (sX/2-200 if LIVES >= 10 else sX/2-194,457))
    pygame.draw.polygon(screen, (200,100,100), [[sX/2-200, 450], [sX/2-185, 420], [sX/2-170, 450]])
    pygame.draw.polygon(screen, (200,100,100), [[sX/2-200, 490], [sX/2-185, 520], [sX/2-170, 490]])
    
    
