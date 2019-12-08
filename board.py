import pygame
import random
import box
import time

pygame.init()

blank = pygame.image.load('gfx/blank.png')

pic_0 = pygame.image.load('no/0.bmp')
pic_1 = pygame.image.load('no/1.bmp')
pic_2 = pygame.image.load('no/2.bmp')
pic_3 = pygame.image.load('no/3.bmp')
pic_4 = pygame.image.load('no/4.bmp')
pic_5 = pygame.image.load('no/5.bmp')
pic_6 = pygame.image.load('no/6.bmp')
pic_7 = pygame.image.load('no/7.bmp')
pic_8 = pygame.image.load('no/8.bmp')
pic_9 = pygame.image.load('no/9.bmp')
SCORE = pygame.image.load('no/SCORE.bmp')
HIGHSCORE = pygame.image.load('no/HIGHSCORE.bmp')
crtl = pygame.image.load('no/crtl.bmp')

class Board(object):
    
    width = 4
    length = 4
    
    moves_counter = 0
    score = 0
    
    boxes = []
    def __init__(self): 
        
        self.add_box()
        self.add_box()
        self.refresh_boxes()
        
    def create_box(self, x, y):
        self.boxes.append(box.Box2(x,y))
        
    def add_box(self): # game ending case
        
        list1 = []
    
        for x in range(0,4):
            for y in range(0,4):
                list1.append((x,y))
                
        for elm in self.boxes:
            list1.remove(elm.get_xy())
        
        if list1 != []:    
            xy = random.choice(list1)
            self.create_box(xy[0], xy[1])
        pass
    
    def display_bck(self, surface):
        for x in range(0,4):
            for y in range(0,4):
                surface.blit(blank, (20 + 105 * x, 20 + 105 * y))
        
        surface.blit(crtl,(24, 450))   
            
    def display_boxes(self,surface):
        for elm in self.boxes:
            elm.display(surface)
            
    def display(self, surface):
        self.display_bck(surface)
        self.display_boxes(surface)
    
    def get_box(self, x, y):
        
        for box in self.boxes:
            if box.get_xy() == (x,y):
                return box
        
        return None    
    
    def refresh_boxes(self): # enables possibility to add boxes to each other
        for elm in self.boxes:
            elm.refresh()
          
    def fusion(self, xy, val, surface): # destroys 2 boxes in one position and creates new one without possibility to fuse
        
        self.score += 2**(val+1)
        self.boxes.remove(self.get_box(xy[0],xy[1]))
        self.boxes.remove(self.get_box(xy[0],xy[1]))
        
        if val + 1 == 12:
            self.display_score(surface)
            self.restart()
        else:
            self.boxes.append(box.Boxes[val](xy[0],xy[1]))
                 
    def swipe_down(self, surface):    
        
        for x in range(0,4):
            for y in range(3,-1, -1):
                if self.get_box(x,y) != None: # if box with xy exists
 
                    tmp = self.get_box(x,y)
                    self.box_down(tmp, surface)
                            
        self.refresh_boxes() # not sure yet if it should be here           
                
    def swipe_up(self, surface):    
        
        for x in range(0,4):
            for y in range(0,4):
                if self.get_box(x,y) != None: # if box with xy exists
                    
                    tmp = self.get_box(x,y)
                    self.box_up(tmp,surface)
                            
        self.refresh_boxes()            
    
    def swipe_left(self, surface):    
        
        for y in range(0,4):
            for x in range(0, 4):
                if self.get_box(x,y) != None: # if box with xy exists
                    
                    tmp = self.get_box(x,y)
                    self.box_left(tmp, surface)
                            
        self.refresh_boxes()            
    
    def swipe_right(self, surface):    
        
        for y in range(0,4):
            for x in range(3,-1, -1):
                if self.get_box(x,y) != None: # if box with xy exists
                    
                    tmp = self.get_box(x,y)
                    self.box_right(tmp, surface)
                            
        self.refresh_boxes()            
    
    def box_down(self, tmp, surface):
        
        if tmp.y < 3:
            tmp2 = self.get_box(tmp.x, tmp.y + 1)
            if tmp2 != None:
                if tmp.get_val() == tmp2.get_val():                 
                    if tmp2.get_status() == True:                        
                        self.moves_counter += 1                        
                        temp_y = tmp.y + 1
                        
                        for var in range(5):
                            tmp.y = tmp.y + 0.2
                            surface.fill((0,0,0))
                            self.display(surface)
                            pygame.display.flip()
                    
                        tmp.y = temp_y
                        
                        self.fusion(tmp.get_xy(), tmp.get_val(), surface)
   
            else:
                
                self.moves_counter += 1
                temp_y = tmp.y + 1
                
                for var in range(2):
                    tmp.y = tmp.y + 0.5
                    surface.fill((0,0,0))
                    self.display(surface)
                    pygame.display.flip()
                
                tmp.y = temp_y
    
                self.box_down(tmp, surface)
        
    def box_up(self, tmp, surface):
        
        if tmp.y > 0:
            
            tmp2 = self.get_box(tmp.x, tmp.y - 1)
            
            if tmp2 != None:
            
                if tmp.get_val() == tmp2.get_val():
                    
                    if tmp2.get_status() == True:
                    
                        self.moves_counter += 1
                        
                        temp_y = tmp.y - 1
                        
                        for var in range(2):
                            tmp.y = tmp.y - 0.5
                            surface.fill((0,0,0))
                            self.display(surface)
                            pygame.display.flip()
                    
                        tmp.y = temp_y
                        
                        self.fusion(tmp.get_xy(), tmp.get_val(), surface)
   
            else:
                
                self.moves_counter += 1
                
                temp_y = tmp.y - 1
                
                for var in range(2):
                    tmp.y = tmp.y - 0.5
                    surface.fill((0,0,0))
                    self.display(surface)
                    pygame.display.flip()
                
                tmp.y = temp_y
    
                self.box_up(tmp, surface)    
        
    def box_left(self, tmp, surface):
        
        if tmp.x > 0:
            
            tmp2 = self.get_box(tmp.x - 1, tmp.y)
            
            if tmp2 != None:
                
                if tmp.get_val() == tmp2.get_val():
                                      
                    if tmp2.get_status() == True:
                    
                        self.moves_counter += 1
                        
                        temp_x = tmp.x - 1
                        
                        for var in range(2):
                            tmp.x = tmp.x - 0.5
                            surface.fill((0,0,0))
                            self.display(surface)
                            pygame.display.flip()
                    
                        tmp.x = temp_x
                        
                        self.fusion(tmp.get_xy(), tmp.get_val(), surface)
   
            else:
                
                self.moves_counter += 1
                
                temp_x = tmp.x - 1
                
                for var in range(2):
                    tmp.x = tmp.x - 0.5
                    surface.fill((0,0,0))
                    self.display(surface)
                    pygame.display.flip()
                
                tmp.x = temp_x
    
                self.box_left(tmp, surface)    
        
    def box_right(self, tmp, surface):
        
        if tmp.x < 3:
            
            tmp2 = self.get_box(tmp.x + 1, tmp.y)
            
            if tmp2 != None:
                
                if tmp.get_val() == tmp2.get_val():
                                      
                    if tmp2.get_status() == True:
                        
                        self.moves_counter += 1
                        
                        temp_x = tmp.x + 1
                        
                        for var in range(2):
                            tmp.x = tmp.x + 0.5
                            surface.fill((0,0,0))
                            self.display(surface)
                            pygame.display.flip()
                    
                        tmp.x = temp_x
                        
                        self.fusion(tmp.get_xy(), tmp.get_val(), surface)
   
            else:
                
                self.moves_counter += 1
                
                temp_x = tmp.x + 1
                
                for var in range(2):
                    tmp.x = tmp.x + 0.5
                    surface.fill((0,0,0))
                    self.display(surface)
                    pygame.display.flip()
                
                tmp.x = temp_x
    
                self.box_right(tmp, surface)    
        
    def box_add_check(self):
        if self.moves_counter > 0:
            self.moves_counter = 0
            self.add_box()
            self.refresh_boxes()
 
    def judge(self, surface):
                
        if len(self.boxes) == 16:
            for x in range(0,4):
                for y in range (0,4):
                    tmp = self.get_box(x,y)
                        
                    if self.get_box(x,y-1) != None:
                        if (self.get_box(x,y-1)).get_val() == tmp.get_xy():
                            break
                            
                    if self.get_box(x,y+1) != None:
                        if (self.get_box(x,y+1)).get_val() == tmp.get_xy():
                            break
                    
                    if self.get_box(x+1,y) != None:
                        if (self.get_box(x+1,y)).get_val() == tmp.get_xy():
                            break
                            
                    if self.get_box(x-1,y) != None:
                        if (self.get_box(x-1,y)).get_val() == tmp.get_xy():
                            break
                        
            self.display_score(surface)           
            self.restart()
 
    def display_score(self, surface):
        
        surface.fill((0,0,0))
        
        as_word = str(self.score) 
        cnt = 5 - len(as_word)
        
        
        if self.score > 99999:
            as_word = 99999
        
        for var in range(cnt):
            as_word = '0' + as_word
         
        for x in range (5):
            
            if as_word[x] == '0':
                surface.blit(pic_0, (120 + 44 * x, 114))
            if as_word[x] == '1':
                surface.blit(pic_1, (120 + 44 * x, 114))    
            if as_word[x] == '2':
                surface.blit(pic_2, (120 + 44 * x, 114))   
            if as_word[x] == '3':
                surface.blit(pic_3, (120 + 44 * x, 114))    
            if as_word[x] == '4':
                surface.blit(pic_4, (120 + 44 * x, 114))    
            if as_word[x] == '5':
                surface.blit(pic_5, (120 + 44 * x, 114))    
            if as_word[x] == '6':
                surface.blit(pic_6, (120 + 44 * x, 114))    
            if as_word[x] == '7':
                surface.blit(pic_7, (120 + 44 * x, 114))    
            if as_word[x] == '8':
                surface.blit(pic_8, (120 + 44 * x, 114))    
            if as_word[x] == '9':
                surface.blit(pic_9, (120 + 44 * x, 114))
        
        readdocsHS=open("highscore.txt","r").read()

        if self.score > int(readdocsHS):
            docsHS= open("highscore.txt","w")
            docsHS.write(str(self.score))
            newscore = str(self.score)
            docsHS.close()
        else:
            newscore = readdocsHS

        as_word1=list("0"*(5-len(newscore))+str(newscore))   

        for y in range(5):
            if as_word1[y] == '0':
                surface.blit(pic_0, (120 + 44 * y, 350))
            if as_word1[y] == '1':
                surface.blit(pic_1, (120 + 44 * y, 350))    
            if as_word1[y] == '2':
                surface.blit(pic_2, (120 + 44 * y, 350))   
            if as_word1[y] == '3':
                surface.blit(pic_3, (120 + 44 * y, 350))    
            if as_word1[y] == '4':
                surface.blit(pic_4, (120 + 44 * y, 350))    
            if as_word1[y] == '5':
                surface.blit(pic_5, (120 + 44 * y, 350))    
            if as_word1[y] == '6':
                surface.blit(pic_6, (120 + 44 * y, 350))    
            if as_word1[y] == '7':
                surface.blit(pic_7, (120 + 44 * y, 350))    
            if as_word1[y] == '8':
                surface.blit(pic_8, (120 + 44 * y, 350))    
            if as_word1[y] == '9':
                surface.blit(pic_9, (120 + 44 * y, 350))    
            
        surface.blit(HIGHSCORE, (120,225))            
        surface.blit(SCORE, (120,50))    
        pygame.display.flip()
        time.sleep(3)
       
    def restart(self):
        self.moves_counter = 0
        self.score = 0
        self.boxes = []
        self.add_box()
        self.add_box()
 
pygame.quit()
