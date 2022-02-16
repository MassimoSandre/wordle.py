from tkinter import Button

import pygame

class Keyboard:
    class Button:
        def __init__(self, value, active=True) -> None:
            self.value = value
            self.active = active

            self.hover_time = 0
            self.HOVER_LIMIT = 20

        def disable(self):
            self.active = False
        def enable(self):
            self.active = True


    
    def __init__(self,center, dim, spacing) -> None:
        self.center = center
        self.dim = dim
        self.spacing = spacing

        

        first_line = list("QWERTYUIOP")
        second_line = list("ASDFGHJKL")
        third_line = list("_ZXCVBNM_")
        third_line[0] = "ENTER"
        third_line[-1] = "BACK"

        self.button_lines = [[],[],[]]
        for b in first_line:
            new_button = self.Button(b)
            self.button_lines[0].append(new_button)

        for b in second_line:
            new_button = self.Button(b)
            self.button_lines[1].append(new_button)

        for b in third_line:
            new_button = self.Button(b)
            self.button_lines[2].append(new_button)

    def render(self,screen, font1, font2):
        height = self.dim[1]*3 + 2*self.spacing

        EN_BS_OFFSET = 20

        for l in range(len(self.button_lines)):
            base_y = self.center[1]-(height//2) +(l*self.dim[1]) + (l*self.spacing)
            width = len(self.button_lines[l])*self.dim[0] + (len(self.button_lines[l])-1)*self.spacing
            base_x = self.center[0]-(width//2)
            for i in range(len(self.button_lines[l])):
                current_x = base_x + self.dim[0]*i + self.spacing*i
                color = []
                if not self.button_lines[l][i].active:
                    color = [50]*3
                else:
                    color = [200-self.button_lines[l][i].hover_time*2]*3
                
                

                if l == 2 and i == 0:
                    pygame.draw.rect(screen, color, pygame.Rect((current_x-EN_BS_OFFSET,base_y),(self.dim[0]+EN_BS_OFFSET, self.dim[1])),0,5)
                elif l==2 and i == len(self.button_lines[l])-1:
                    pygame.draw.rect(screen, color, pygame.Rect((current_x,base_y),(self.dim[0]+EN_BS_OFFSET, self.dim[1])),0,5)
                else:
                    pygame.draw.rect(screen, color, pygame.Rect((current_x,base_y),self.dim),0,5)
                
                if len(self.button_lines[l][i].value) > 1:
                    text_surface = font2.render(self.button_lines[l][i].value, False, (70,70,70))
                else:
                    text_surface = font1.render(self.button_lines[l][i].value, False, (70,70,70))


                r = text_surface.get_rect()

                dx = (r.width)//2
                dy = (r.height)//2
                if l == 2 and i == 0:
                    screen.blit(text_surface, (current_x-EN_BS_OFFSET+(self.dim[0]+EN_BS_OFFSET)//2-dx, base_y+self.dim[1]//2-dy))
                elif l==2 and i == len(self.button_lines[l])-1:
                    screen.blit(text_surface, (current_x+(self.dim[0]+EN_BS_OFFSET)//2-dx, base_y+self.dim[1]//2-dy))
                else:
                    screen.blit(text_surface, (current_x+self.dim[0]//2-dx, base_y+self.dim[1]//2-dy))
                
    def get_input(self, mouse_pos):
        height = self.dim[1]*3 + 2*self.spacing

        x,y = mouse_pos

        for l in range(len(self.button_lines)):
            base_y = self.center[1]-(height//2) +(l*self.dim[1]) + (l*self.spacing)
            width = len(self.button_lines[l])*self.dim[0] + (len(self.button_lines[l])-1)*self.spacing
            base_x = self.center[0]-(width//2)
            for i in range(len(self.button_lines[l])):
                current_x = base_x + self.dim[0]*i + self.spacing*i
                if x >= current_x and  x <= current_x + self.dim[0] and y >= base_y and y <= base_y+self.dim[1]:
                    return self.button_lines[l][i].value
        
        return None

    def hover(self, mouse_pos):
        height = self.dim[1]*3 + 2*self.spacing

        x,y = mouse_pos

        for l in range(len(self.button_lines)):
            base_y = self.center[1]-(height//2) +(l*self.dim[1]) + (l*self.spacing)
            width = len(self.button_lines[l])*self.dim[0] + (len(self.button_lines[l])-1)*self.spacing
            base_x = self.center[0]-(width//2)
            for i in range(len(self.button_lines[l])):
                current_x = base_x + self.dim[0]*i + self.spacing*i
                if x >= current_x and  x <= current_x + self.dim[0] and y >= base_y and y <= base_y+self.dim[1]:
                    self.button_lines[l][i].hover_time = min(self.button_lines[l][i].hover_time+1, self.button_lines[l][i].HOVER_LIMIT)
                else:
                    self.button_lines[l][i].hover_time = max(self.button_lines[l][i].hover_time-1, 0)

        
        






