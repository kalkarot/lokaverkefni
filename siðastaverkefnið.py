#PyVerkefni 29. Forritun 203. Kennari: Bjarni
import pygame, sys
from pygame.locals import *
import random

class Player:
    def _init_(self,x,y):
        self.x=x
        self.y=y
        self.width=32
        self.height=32
        self.velocity=0
        self.falling=True
        self.onGround=False
    def jump(self):
        if(self.onGround==False):
            return
        self.velocity=8
        self.onGround=False
def walls():
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, BLACK, (50,350), (350,350), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (50,350), (50,50), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (50,50), (350,50), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (350,50), (350,350), 5)
#platforms
    pygame.draw.line(DISPLAYSURF, BLACK, (200,250), (250,250), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (100,150), (150,150), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (250,300), (300,300), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (240,200), (280,200), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (200,150), (250,150), 5)
def stig(score):
    WINDOWWIDTH = 400
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    scoreSurf = BASICFONT.render('Stig: %s' % (score), True, GREEN)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def gameover():
    WINDOWWIDTH = 400
    WHITE = (255, 255, 255)
    gameOverFont = pygame.font.Font('freesansbold.ttf', 55)
    gameSurf = gameOverFont.render('Game', True, RED)
    overSurf = gameOverFont.render('Over', True, RED)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    #drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()


pygame.init()
FPS = 20 # frames per second setting
fpsClock = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('loka verk')   #nafnið á glugganum

#Býr til litina
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
litur = BLACK
#staðsetning í byrjun
x = 200
y = 200

kx=[]
ky=[]

lx=[]
ly=[]

for i in range(0, 10):
    kx.append (random.randrange(1,40) * 5)
    ky.append (random.randrange(1,40) * 5)

#x-ás, y-ás, x-radius, y-radius


score = 0

lx.append(x)
ly.append(y)


#loopa sem keyrir leikinn
while True:
    walls()
    
    del lx[0]
    del ly[0]

    
    for i in range(0, 10):
        kassi = pygame.draw.rect(DISPLAYSURF, GREEN, (kx[i], ky[i], 10, 10)) #kassi
        
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN: 
            if (event.key == K_LEFT ):
                x-=10
            elif (event.key == K_RIGHT ): 
                x+=10
            elif (event.key == K_UP ): 
                y-=10
            elif (event.key == K_DOWN ): 
                y+=10
       
    if x == kx and y == ky:
        score = score + 1

    for i in range (0, 10):
        if kx[i]==x and ky[i]==y:
            lx.append(x)
            ly.append(y)
            score += 1
            kx[i] = (random.randrange(1,40) * 10)
            ky[i] = (random.randrange(1,40) * 10)
            FPS += 1.5

    pygame.draw.rect(DISPLAYSURF, litur, (x, y, 10, 10)) #kassi

    #bætir við núverandi hnitum á x og y við listann
    lx.append(x)
    ly.append(y)

    #Teiknar halann
    if len(lx)>0:
        for i in range(0, len(lx)):
            pygame.draw.rect(DISPLAYSURF, litur, (lx[i], ly[i], 10, 10))
    
    pygame.display.update()

    fpsClock.tick(FPS)
