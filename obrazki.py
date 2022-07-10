import os, pygame,sys

def obraz(a):
    mypath=os.getcwd()  
    
    if mypath!='D:\praca\programowanie\python\pygame\pic':
        
        mypath+="\\pygame\\pic" 
        os.chdir(mypath)
    return pygame.image.load(a)

def tlostart():
    size=w,h=1000,1000
    return pygame.display.set_mode(size)

def sysex():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    