from random import randint, random
from obrazki import *
import sys, pygame, os, time
lat=obraz("latarnia.png")
latrect=lat.get_rect(left=0,bottom=1000)
latrect.center
pfire=[latrect.left+int(latrect.width/2)+1,latrect.top+100]
print(pfire)
x=0
y=1000




screen =tlostart()
color=240,240,255
while True:
    x=randint(100,670)
    xend=(-pfire[0]+x)*(1000-pfire[1])/(1000-pfire[1]-200)+pfire[0]  #xend=(xl-x)*wl/(wl-wc)
    time.sleep(0.6)
    
    sysex()
    # print(ballrect.top)
    screen.fill(color)
    screen.blit(lat,latrect)
    pygame.draw.circle(screen, [255,0,0], pfire, 10, width=0)
    pygame.draw.line(screen, [255,0,0], pfire, [xend,1000])
    pygame.draw.line(screen, [0,0,0], [x,y],[x,y-200] , width=1)
    pygame.draw.line(screen, [0,0,0], [x,y], [xend,1000], width=5)
    pygame.display.flip()