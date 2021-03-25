import pygame
import random
import Pygame_Plus as pg_plus

chovek = pg_plus.Kvadrat(500, 400, 30, 30, 0, 5, pg_plus.color.purple)

boosts = []
i = 0
while i < 12:
    rx = random.randrange(40, 960)
    ry = random.randrange(0, 1000) - 500
    boosts.append(pg_plus.Krag(rx, ry, 10, 3, chovek.vel, pg_plus.color.red))
    i = i + 1


isJump = False
jumps = 6

g = 30
V = 0
rV = 0

def Grav(g, V, fps):
    V -= g / fps
    return V

def MoVe():
    chovek.x += chovek.vel

def DrAw(win):
    win.fill(pg_plus.color.cyan)
    for iq in boosts:
        iq.draw(win)
    chovek.draw(win)
    pygame.display.update()


width, height = 1000, 650

pygame.init()

win = pygame.display.set_mode((width, height))


clock = pygame.time.Clock()
fps = 60
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if chovek.x + chovek.w >= width or chovek.x <= 0:
        chovek.vel *= -1

    if key[pygame.K_SPACE] and not isJump and jumps:
        V = 20
        jumps -= 1
        isJump = True

    if not key[pygame.K_SPACE]:
        isJump = False

    i = 0
    while i < len(boosts):
        if chovek.x <= boosts[i].x <= chovek.x + chovek.w and chovek.y <= boosts[i].y <= chovek.y + chovek.h:
            jumps += 1
            boosts[i].x = random.randrange(40, 960)
            boosts[i].y = random.randrange(0, 500)
            b = random.randrange(1, 2)
            jj = 0
            while jj < b:
                rx = random.randrange(40, 960)
                ry = random.randrange(0, 1000) - 500
                boosts.append(pg_plus.Krag(rx, ry, 10, 3, chovek.vel, pg_plus.color.red))
                jj += 1

        i += 1

    V = Grav(g, V, fps)
    rV = round(V)
    for ii in boosts:
        ii.y += rV


    MoVe()
    DrAw(win)      
    print(str(jumps) + " " + str(len(boosts)))


pygame.quit()