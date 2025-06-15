from shot import Shot
from asteroid import Asteroid
from player import Player
import random
import pygame
import os
import sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)


# Init
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My Game Felipe")


# Groups
objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()


# Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("Resources/Desert.png")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)


# Music
pygame.mixer.music.load("Resources/BackgroundSound.mp3")
pygame.mixer.music.play(-1)

# Sounds
shoot = pygame.mixer.Sound("Resources/swing.wav")
gameOverSound = pygame.mixer.Sound("Resources/GameOver.wav")


gameLoop = True
gameOver = False
timer = 0
clock = pygame.time.Clock()
while gameLoop:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot.play()
                newShot = Shot(objectGroup, shotGroup)
                newShot.rect.center = player.rect.center

    # Update logic

    if not gameOver:
        objectGroup.update()

        timer += 1

        if timer > 30:
            timer = 0
            if random.random() < 0.80:
                Asteroid(objectGroup, asteroidGroup)

        collisions = pygame.sprite.spritecollide(
            player, asteroidGroup, False, pygame.sprite.collide_mask)

        if collisions:
            print("Game Over")
            gameOver = True
            gameOverSound.play()

        hits = pygame.sprite.groupcollide(
            shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

    # Draw

    display.fill([46, 46, 46])

    objectGroup.draw(display)

    pygame.display.update()
