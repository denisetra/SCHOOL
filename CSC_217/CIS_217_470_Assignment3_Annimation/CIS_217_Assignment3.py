# Denise Tranberg
# CIS 217_470 - Assignment 3
# Start date: 6/21
# Complete date: 6/28
#
# # Assignment:
# Create a small program that incoporates both sound and animation.
# The theme of the program should have to do with learning a concept in Python. Structure using functions.
# Don't forget to comment the functions so that it is clear to the user where the sound an animation have been integrated.
#
#
#############################################################################
#                   Variables & Imports                                     #
#############################################################################


import pygame, sys
from pygame.locals import *


pygame.init()

FPS = 60  # frames per second
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32) # set the surface size of display
pygame.display.set_caption("Denise's PYTHON Animation") # set captian
LTBLUE = (50,207,238) # assign value to color name
pygame.mixer.music.load('3-3-10018.mp3') # load audio file

bg=pygame.image.load("Cats-2016-2.jpg") # load cat image

#################################################################################
#                   Main processing                                             #
#################################################################################

def animation():

    heartImg=pygame.image.load ('heart3.jpg')  # load heart image
    heartx=10
    hearty=10
    direction='right'
    snakeImg=pygame.image.load ('snake2.JPG') # load snake image
    snakex=400
    snakey=400
    snakeDirection='left'


    while True: # run the game loop

        DISPLAYSURF.fill(LTBLUE)
        # below are instructions on direction to move for annimation of heart
        if direction == 'right':
            heartx += 5
            if heartx == 680:
                direction = 'down'
        elif direction == 'down':
            hearty += 5
            if hearty == 680:
                direction = 'left'
        elif direction == 'left':
            heartx -= 5
            if heartx == 10:
                direction = 'up'
        elif direction == 'up':
            hearty -= 5
            if hearty == 10:
                direction = 'right'
        ######
        # below are instructions on direction to move for annimation of snake
        if snakeDirection == 'left':
            snakex -= 5
            if snakex == 100:
                snakeDirection = 'down'
        elif snakeDirection == 'up':
            snakey -= 5
            if snakey==100:
                snakeDirection = 'left'
        elif snakeDirection == 'right':
            snakex += 5
            if snakex == 600:
                snakeDirection = 'up'
        elif snakeDirection == 'down':
            snakey += 5
            if snakey == 500:
                snakeDirection = 'right'

        if snakey==500 and snakex==100:
            pygame.mixer.music.play(0) ##play sound file each time the snake is at (y=500,x=100)




        DISPLAYSURF.blit(heartImg,(heartx,hearty)) # draw the heart at specified location
        DISPLAYSURF.blit(snakeImg,(snakex,snakey)) # draw the snake at specified location
        DISPLAYSURF.blit(bg,(200,200))             # draw the cat picture at specified location


        for event in pygame.event.get(): # has the program exit correctly
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update() # updates the entire surface area

        fpsClock.tick(FPS) # manages the framerate

animation() # call the annimation function.








