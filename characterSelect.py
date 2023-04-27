import pygame
from buttons import button
from settings import *

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
sX, sY = screen.get_size()

buttonlist: list[button] = []

startbutton = button((((sX/2) - 150), 700), (300, 150), (100,100,100))

p1square = button((sX/2-260, 290), (100, 100), (150,150,150))
p1circle = button((sX/2-370, 290), (100, 100), (150,150,150))
p1triangle = button((sX/2-150, 290), (100, 100), (150,150,150))
p1hexagon = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
p1diamond = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)

p2square = button((sX/2 + 160, 290), (100, 100), (150,150,150)) 
p2circle = button((sX/2+270, 290), (100, 100), (150,150,150))
p2triangle = button((sX/2 + 50, 290), (100, 100), (150,150,150))
p2hexagon = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
p2diamond = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)

buttonlist.append(startbutton)
buttonlist.append(p1square)
buttonlist.append(p1circle)
buttonlist.append(p1triangle)

buttonlist.append(p2square)
buttonlist.append(p2circle)
buttonlist.append(p2triangle)
randshape = ''#TODO randomize player shape OR make it so each player starts off with no shape


platformlist: list[pygame.Rect] = [] #makes a list for platforms to be stored in

def characterSelect(screen):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:#actually closes the program when you close it 
            exit(0)
        elif e.type == pygame.MOUSEBUTTONDOWN:#lets you interact with buttons when you click on them
            for b in buttonlist:
                if b.box.collidepoint(pygame.mouse.get_pos()):
                    if b is startbutton:
                        return False
                    if b is p1triangle:
                        pass
                    if b is p1circle:
                        pass
                    if b is p1square:
                        pass
                    if b is p2triangle:
                        pass
                    if b is p2circle:
                        pass
                    if b is p2square:
                        pass

    #pretty standard render section
    screen.fill((48, 52, 70))

    pygame.draw.line(screen, (100,50,50),(sX/2, 200), (sX/2,700),10 )

    for b in buttonlist:
        b.draw()

    pygame.draw.polygon(screen, (205, 50, 30), [[sX/2 - 75, 360], [sX/2 - 100, 310], [sX/2-125, 360]])
    pygame.draw.polygon(screen, (30, 190, 50), [[sX/2+75, 358], [sX/2+100, 308], [sX/2+125, 358]])
    pygame.draw.rect(screen, (205, 50, 30), (sX/2-235, 315, 50, 50))
    pygame.draw.rect(screen, (30, 190, 50), (sX/2+185, 315, 50, 50))
    pygame.draw.circle(screen, (30, 190, 50), (sX/2+320, 340), 25)	
    pygame.draw.circle(screen, (205, 50, 30), (sX/2-320, 340), 25)	

    font = pygame.font.Font(None, 100)
    text = font.render(str('FIGHT!'), True, (130,215,215))
    screen.blit(text, (sX/2 - 118,750))
    text = font.render(str('Player Two'), True, (30, 190, 50))
    screen.blit(text, (sX/2+50,220))
    text = font.render(str('Player One'), True, (205, 50, 30))
    screen.blit(text, (sX/2-410,220))
    font = pygame.font.Font(None, 190)
    text = font.render(str('CHOOSE YOUR SHAPE'), True, (150,255,255))
    screen.blit(text, (200,50))
    pygame.display.flip()