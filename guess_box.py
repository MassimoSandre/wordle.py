from mimetypes import guess_all_extensions
import pygame

class Guess_box:
    def __init__(self, word_list, center, cell_dim, spacing) -> None:
        self.word_list = word_list
        self.center =center
        self.dim = cell_dim
        self.spacing = spacing

    def reset(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.guesses = []

        self.current = ""

    def guess(self, word):
        self.guesses.append(word)
        
    def push_letter(self, letter):
        if letter != None:
            if letter == "BACK":
                if len(self.current) >= 1:
                    self.current = self.current[0:len(self.current)-1]
            elif letter == "ENTER":
                
                if len(self.current) == 5:
                    for w in self.word_list:
                        if self.current.lower() in w:
                            self.guess(self.current)
                            self.current = ""
                            break
                    
            else:
                if len(self.current) < 5:
                    self.current+=letter

    def outcome(self):
        if len(self.guesses) > 0:
            if self.guesses[-1] == self.word_to_guess:
                return 1
        if len(self.guesses) >= 6:
            return -1
        return 0

    def render(self, screen, font):
        bx = self.center[0]-(self.dim[0]*2 + self.dim[0]//2 + 2*self.spacing)
        by = self.center[1]-(3*self.dim[1] + 2*self.spacing + self.spacing//2)

        for i in range(0,6):
            hints = []
            for j in range(0,5):
                if len(self.guesses) >= i+1:
                    cx = bx + (self.dim[0]+self.spacing)*j
                    cy = by + (self.dim[1]+self.spacing)*i

                    color = [200]*3
                    if self.guesses[i][j] in self.word_to_guess.upper() and self.guesses[i][j] not in hints:
                        hints.append(self.guesses[i][j])
                        if self.word_to_guess[j] == self.guesses[i][j].lower():
                            color = (0,200,0)
                        else:
                            color = (180,180,0)

                    pygame.draw.rect(screen, color, pygame.Rect((cx,cy),self.dim),0)
                    
                    text_surface = font.render(self.guesses[i][j], False, (230,230,230))

                    r = text_surface.get_rect()

                    dx = (r.width)//2
                    dy = (r.height)//2
                    screen.blit(text_surface, (cx+self.dim[0]//2-dx, cy+self.dim[1]//2-dy))
                    
                else:
                    if len(self.guesses) == i and len(self.current) >= j+1:
                        cx = bx + (self.dim[0]+self.spacing)*j
                        cy = by + (self.dim[1]+self.spacing)*i
                        pygame.draw.rect(screen, [200]*3, pygame.Rect((cx,cy),self.dim),1)
                        
                        text_surface = font.render(self.current[j], False, (230,230,230))

                        r = text_surface.get_rect()

                        dx = (r.width)//2
                        dy = (r.height)//2
                        screen.blit(text_surface, (cx+self.dim[0]//2-dx, cy+self.dim[1]//2-dy))
                    else:
                        # spazi vuoti
                        cx = bx + (self.dim[0]+self.spacing)*j
                        cy = by + (self.dim[1]+self.spacing)*i
                        pygame.draw.rect(screen, [200]*3, pygame.Rect((cx,cy),self.dim),1)
                        #print("sium")
