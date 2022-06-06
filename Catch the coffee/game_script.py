#Catch the coffee varasion 1.0
#game isn't completed yet
#Made by Alon BR.

import pygame
import os

from sys import exit#stop's the game's code instantly
from random import choice#random number / index / a part from a list or tuple  etc.
from math import ceil#round up
from WITH_HEIGHT import WITH,HEIGHT#game's window with and height
pygame.init()#inint pygame

#game vars:

app = pygame.display.set_mode((WITH,HEIGHT))
pygame.display.set_caption("Catch the coffee")

#tables for duificulties:
from start_game import duificulty
duificulty_life_taking_table = {
    "easy" : 0.5,
    "normal" : 1,
    "hard" : 1.5,
    "hardcore" : 2
}

duificulty_health_table = {
    "easy" : 100,
    "normal" : 50,
    "hard" : 25,
    "hardcore" : 10
}

duificulty_speed_potion_time_table = {
    "easy" : 50,
    "normal" : 20,
    "hard" : 10,
    "hardcore" : 7
}

duificulty_speed_potion_time = duificulty_speed_potion_time_table[duificulty]
duificulty_health = duificulty_health_table[duificulty]
duificulty_life_taking = duificulty_life_taking_table[duificulty]

players_health=duificulty_health# player's health

#image loading:
coffee_bean_size_X = 70
coffee_bean_size_Y = 50
coffee_bean = pygame.transform.scale(pygame.image.load(os.path.join("Assets","coffee bean.png")) , (coffee_bean_size_X,coffee_bean_size_Y))

player_size_X = 80
player_size_Y = 100
player = pygame.transform.scale(pygame.image.load(os.path.join("Assets","player.png")),(player_size_X,player_size_Y))

heart_size_X = 40
heart_size_Y = 40
heart_image = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets","heart.png")
),(heart_size_X,heart_size_Y))

speed_potion_size_X = 40
speed_potion_size_Y = 50
speed_potion_image = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets","speed potion.png"
)),(speed_potion_size_X,speed_potion_size_Y))

SCALE_PER_METER = 20
GRAVITY = 9.80665

PLAYERS_MASS = 1.15

#Velocities and Accelerations:

#inner area -> PLAYER:
PLAYER_Y_ACCELERATION = (GRAVITY*PLAYERS_MASS)/SCALE_PER_METER
PLAYER_Y_VELOCITY = 0

#FONTS:
GAME_FONT_SIZE = 24
GAME_FONT = pygame.font.SysFont(None,GAME_FONT_SIZE)# making the font to render!
#rendering fonts in the while loop if not const font!!!

#functions for use:

def init():
    global players_health,PLAYER_Y_VELOCITY

    # inner function vars:
    FPS=60
    clock = pygame.time.Clock()#limited FPS!!! dont remove never ever!
    
    
    speed_boost = 0# how much speed bost/ speed potion boost
    score=0#score of the game
    speed_time = 0#for speed potion

    #cords of entities X,Y and rects:
    # entity can move!!! or else its no an entity!!!
    
    coffee_beanXY = pygame.Rect(choice(range(coffee_bean_size_X,WITH-coffee_bean_size_X)),
    choice(range(coffee_bean_size_Y,HEIGHT-coffee_bean_size_Y)),
    coffee_bean_size_X,coffee_bean_size_Y)

    playerXY=pygame.Rect(WITH/2,HEIGHT/2,player_size_X,player_size_Y)

    speed_potionXY = pygame.Rect(choice(range(0,WITH-speed_potion_size_X)),choice(range(0,HEIGHT-speed_potion_size_Y)),speed_potion_size_X,speed_potion_size_Y)

   #game loop:
    run = True

    #game deadline and target and gameplay
    last_deadline = 5000
    deadline = last_deadline
    target = 5
    game_round = 1


    while run:

        clock.tick(FPS)

        #pygame event handeler:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    PLAYER_Y_VELOCITY=-10
        keys=pygame.key.get_pressed()# KEYS, needs to stay in the loop for updating
        
        #font display render:
        score_display = GAME_FONT.render(f"score: {score}",True,(0,0,0))
        health_display = GAME_FONT.render(str(players_health),True,(0,0,0))


        time_potion_display = GAME_FONT.render(f"time left for speed: {speed_time}",True,(0,0,0))

        #picture XY not entities!
        # if you want to find the square of an entity then search entities in cntrl+F

        # inner area -> heart image cords:
        heart_X = heart_size_X
        heart_Y = HEIGHT-heart_size_Y

        # display area / blits:
        app.fill((80,200,230))

        app.blit(speed_potion_image,(speed_potionXY.x,speed_potionXY.y))

        app.blit(coffee_bean,(coffee_beanXY.x,coffee_beanXY.y))

        app.blit(player,(playerXY.x,playerXY.y))
        
        app.blit(score_display,(20,20))

        app.blit(heart_image,(heart_X,heart_Y))
        app.blit(health_display,(heart_X+(heart_size_X/2-(GAME_FONT_SIZE/2)),
        heart_Y+(heart_size_Y/2-(GAME_FONT_SIZE/2))))
        
        if speed_time>0:
            app.blit(time_potion_display, (WITH/2,20))

        # work and logic area:
        PLAYER_Y_VELOCITY+=PLAYER_Y_ACCELERATION

        if keys[pygame.K_LEFT]:
            playerXY.x-=(4+speed_boost)
        if keys[pygame.K_RIGHT]:
            playerXY.x+=(4+speed_boost)

        playerXY.y+=PLAYER_Y_VELOCITY

        if playerXY.y>(HEIGHT+player_size_Y):
            playerXY.y=0
        
        if playerXY.y<(0-player_size_Y):
            playerXY.y=(HEIGHT-player_size_Y)
        
        if playerXY.x > WITH+player_size_X:
            playerXY.x = player_size_X
        
        if playerXY.x < -player_size_X:
            playerXY.x = WITH-player_size_X
        
        # inner area -> collides:
        if playerXY.colliderect(coffee_beanXY):
            score+=1
            coffee_beanXY.x = choice(range(coffee_bean_size_X,WITH-coffee_bean_size_X))
            coffee_beanXY.y = choice(range(coffee_bean_size_Y,HEIGHT-coffee_bean_size_Y))
        
        # speed potion gets speed
        #speed time near rendering text for now!!!
        if playerXY.colliderect(speed_potionXY) or speed_boost!=0:
            speed_time-=1
            #print(speed_time)
            if speed_time<1:
                speed_boost = 0
        
        if playerXY.colliderect(speed_potionXY):
            speed_boost=4
            speed_time = FPS*duificulty_speed_potion_time
            speed_potionXY.x = choice(range(speed_potion_size_X,WITH-speed_potion_size_X))
            speed_potionXY.y = choice(range(speed_potion_size_Y,HEIGHT-speed_potion_size_Y))
        
        # inner area -> health logic:

        if PLAYER_Y_VELOCITY > 40:
            players_health-=ceil(PLAYER_Y_VELOCITY/1000)
        
        if players_health<1:
            run = False
            pygame.quit()
            import start_game
            start_game.init()
        #deadline tick and life taking deadline area:
        deadline-=1
        if deadline <1:
            if score < target :
                players_health -= 1
            game_round+=1
            last_deadline+=5
            deadline = last_deadline
            
            coffee_beanXY.x = choice(range(coffee_bean_size_X,WITH-coffee_bean_size_X))
            coffee_beanXY.y = choice(range(coffee_bean_size_Y,HEIGHT-coffee_bean_size_Y))
            
            speed_potionXY.x = choice(range(speed_potion_size_X,WITH-speed_potion_size_X))
            speed_potionXY.y = choice(range(speed_potion_size_Y,HEIGHT-speed_potion_size_Y))

            playerXY.x = player_size_X
            playerXY.y = HEIGHT/2
        
        #FPS and update display:
        pygame.display.update()

if __name__ == '__main__':
    init()