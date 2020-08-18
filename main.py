import pygame
import random


def main():
    #initialize pygame
    pygame.init()

    #creates screen
    screen=pygame.display.set_mode((800,600))

    #Title and Icon
    pygame.display.set_caption("PythonMon")
    icon = pygame.image.load("person.png")
    pygame.display.set_icon(icon)

    #Grass
    grass = pygame.image.load("newGrass.png")

    #Player
    playerImg= pygame.image.load("person.png")
    playerX = 370
    playerY = 480

    #Game Loop
    running=True
    while running:
        screen.fill((0, 100, 40))
        screen.blit(grass, (200, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if playerY != 550: #keeps player out of bounds
                        playerY += 10
                        checkPokemonAppearance(screen, playerX, playerY)
                if event.key == pygame.K_w:
                    if playerY != 10: #keeps player out of bounds
                        playerY -= 10
                        checkPokemonAppearance(screen, playerX, playerY)
                if event.key == pygame.K_a:
                    if playerX != 10: #keeps player out of bounds
                        playerX -= 10
                        checkPokemonAppearance(screen, playerX, playerY)
                if event.key == pygame.K_d:
                    if playerX != 790: #keeps player out of bounds
                        playerX += 10
                        checkPokemonAppearance(screen, playerX, playerY)


        player(screen, playerImg, playerX, playerY)
        pygame.display.update()


def player(screen, playerImg, playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))

def checkPokemonAppearance(screen, playerX, playerY):
    #if player is in the ranges of 200-300x and 200-300y
    if playerX >= 200  and playerX <= 300:
        if playerY >=200 and playerY <= 300:
            #10% chance player runs into a pokemon every step they take
            if random.randint(0, 10) == 0:
                setUpBattle(screen)

def setUpBattle(screen):
    battling= True
    while battling:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    battling=False
            pygame.display.update()


if __name__ == '__main__':
    main()

