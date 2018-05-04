import pygame, sys

from pygame.locals import *

from random import *

from random import randrange

import math





pygame.init()

#WINDOW SETUP CONFIG

winTitle = 'Samúel'

winHeight = 600

winWidth = 900

window = winHeight*winWidth

FPS = 60 # frames per second setting

fpsClock = pygame.time.Clock()



# set up the window

screen = pygame.display.set_mode((winWidth, winHeight), 0, 32)

pygame.display.set_caption(winTitle)



WHITE = (255, 255, 255)

RED = (255,   0,   0)



class Player():

    def __init__(self, startPos, width):

        self.start = startPos

        self.width = width

        self.rect = pygame.Rect(self.start, (width, width))

        self.color = (0, 255, 0)

        self.speed = 6

        self.isFalling = True

        self.isLanded = True

        self.isMoving = False

        self.isJumping = False

        self.jumpTimer = 0

        self.jumpHeight = 20



    def draw(self):

        pygame.draw.rect(screen, self.color, self.rect)



    def move(self, dir):

        if player.rect.x <= 0:

            player.rect.x = screen.get_width()

        elif player.rect.x+player.rect.w > screen.get_width()+6:

            player.rect.x = 0

        if dir == "Left":

            player.rect.x -= self.speed

        elif dir == "Right":

            player.rect.x += self.speed



    def jump(self):

        if self.jumpTimer == 0 and not self.isJumping:

            self.isJumping = True

            self.isLanded = False

            self.jumpTimer = self.jumpHeight



        if self.isJumping:

            self.isFalling = False





class Object():

    def __init__(self, startPos, width, height):

        self.start = startPos

        self.width = width

        self.height = height

        self.end = (width, height)

        self.rect = pygame.Rect(startPos[0], startPos[1], width, height)

        self.width = 5

        self.color = (0,0 , min(((randint(0,250)), 255)))



    def draw(self):

        pygame.draw.rect(screen, self.color, (self.start, self.end))





gravity = 4

direction = ""

player = Player((screen.get_width()/2, 0), 20)

Ground = Object((-10,500),screen.get_width()+50, 5)



def generatePlatforms():

    global Ground

    global platforms, platformColl

    platforms = [Ground]

    platformColl = []



    for i in range(50,500, 50):

        if randint(0,100) > 90:

            platforms.append(Object((randint(0, screen.get_width()), i+randint(-50,50)), randint(50, 100), 5))

        platforms.append(Object((randint(-50, screen.get_width() + 50), i), randint(200,250), 5))



    for platform in platforms:

        print(int(math.fabs(platform.rect.top-255)))

        platformColl.append(platform.rect)



generatePlatforms()

# list for kx and ky
kx = []
ky = []

# random food ap
for i in range(0, 5):
    kx.append(random.randrange(0,90) * 10)
    ky.append(random.randrange(0,50) * 10)

# food



while True:#Keyrir leikinn

    screen.fill(WHITE)



    # boxes
    for i in range(0, 5):
        kassi = pygame.draw.rect(screen, RED, (kx[i], ky[i], 10, 10)) #kassi



    if player.isFalling and not player.isJumping:

        player.rect.y += gravity

    elif player.isJumping:

        if player.jumpTimer > 0:

            player.jumpTimer -= 1

            player.rect.y -= gravity+3

        else:

            player.isJumping = False

    player.draw()


    if player.rect.collidelist(platformColl) >= 0:

        if player.isFalling == True and player.jumpTimer == 0:

            player.isLanded = True

        player.isFalling = False

    else:

        player.isFalling = True



    if player.isMoving and direction:

        player.move(direction)



    for platform in platforms:

        platform.draw()





    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

        elif event.type == KEYDOWN:

            if (event.key == K_SPACE):

                if not player.isJumping and player.jumpTimer == 0 and player.isLanded:

                    player.jump()

            elif (event.key == K_LEFT):

                player.isMoving = True

                direction = "Left"

            elif (event.key == K_RIGHT):

                player.isMoving = True

                direction = "Right"

        elif event.type == KEYUP:

            if (event.key == K_LEFT):

                player.isMoving = False

            elif (event.key == K_RIGHT):

                player.isMoving = False

    pygame.display.update()

    fpsClock.tick(FPS)