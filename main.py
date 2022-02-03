from ctypes.wintypes import WORD
import json
import pygame
from pygame.locals import *
import random
from keyboard import Keyboard
from guess_box import Guess_box

# TODO
# - stats and stats file
# - animations for guesses



f = open("allowed-guesses.json",'r')
allowed_guesses = json.load(f)
f.close()
f = open("answers.json",'r')
answers = json.load(f)
f.close()


size = width, height = 800, 800

bgcolor = 40,40,40


screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.font.init()
kb_font = pygame.font.SysFont('arial', 10)
gb_font = pygame.font.SysFont('arial', 30)

kb = None
gb = Guess_box(allowed_guesses, (400,200), (60,60), 3)

running = True

round_over = True

correct_answer = ""

guesses = []*6

while running:
    screen.fill(bgcolor)
    
    if kb != None:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    gb.push_letter(kb.get_input(event.pos))

    if round_over:
        round_over = False
        correct_answer = random.choice(answers)
        kb = Keyboard((400,600),(60,60),3)
        gb.reset(correct_answer)
        print(correct_answer)

    
    kb.render(screen, kb_font)
    gb.render(screen, gb_font)

    kb.hover(pygame.mouse.get_pos())

    pygame.display.update()
    clock.tick(60)