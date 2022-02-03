from ctypes.wintypes import WORD
import json
import pygame
from pygame.locals import *
import random
from keyboard import Keyboard

f = open("allowed-guesses.json",'r')
allowed_guesses = json.load(f)
f.close()
f = open("answers.json",'r')
answers = json.load(f)
f.close()


size = width, height = 800, 800

black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('arial', 10)

kb = None

running = True

round_over = True

correct_answer = ""

guesses = []*6

while running:
    screen.fill(black)
    
    if kb != None:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    print(kb.get_input(event.pos))

    if round_over:
        round_over = False
        correct_answer = random.choice(answers)
        kb = Keyboard((400,400),(60,60),3)

    
    kb.render(screen, font)
    kb.hover(pygame.mouse.get_pos())

    pygame.display.update()
    clock.tick(60)