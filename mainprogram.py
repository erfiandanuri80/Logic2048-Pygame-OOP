import pygame
import board

black = (0,0,0)
white = (255,255,255)
green = (11, 232, 129)
red = (255, 63, 52)
blue =(15, 188, 249)

display_width = 450
display_height = 550

pygame.init()

b1 = board.Board()

size = [display_width, display_height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("logic 2048")
logo = pygame.image.load("logo1.png")
clock = pygame.time.Clock()

on = True
def intro():
	intro = True
	menu1_x = 425
	menu1_y = 350
	menu2_x = 425
	menu2_y = 450
	menu_width = 150
	menu_height = 75
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		screen.fill(black)
		message_display("Logic 2048",50,display_width/2,display_height/2-20)
		screen.blit(logo,((display_width/2)-100,10))	
		pygame.draw.rect(screen,green,(display_width/2-75,325,150,75))
		pygame.draw.rect(screen,red,(display_width/2-75,425,150,75))
		
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		
		if display_width/2-75 < mouse[0] < display_width/2-75+menu_width and menu1_y-25 < mouse[1] < menu1_y-25+menu_height:
			pygame.draw.rect(screen,blue,(display_width/2-75,325,150,75))
			if click[0] == 1:
				intro = False
		if display_width/2-75 < mouse[0] < display_width/2-75+menu_width and menu2_y-25 < mouse[1] < menu2_y-25+menu_height:
			pygame.draw.rect(screen,blue,(display_width/2-75,425,150,75))
			if click[0] == 1:
				pygame.quit()
				quit()
	
		message_display("Start",40,display_width/2,365)
		message_display("Exit",40,display_width/2,465)
		
		pygame.display.update()
		clock.tick(60)

def gameloop():
    on= True
    while on:
        # graphics
        screen.fill((0,0,0))
        b1.display(screen)
        
        pygame.display.flip()
        clock.tick(60)
        # input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_UP:    
                    b1.swipe_up(screen)
                if event.key == pygame.K_DOWN:
                    b1.swipe_down(screen)
                elif event.key == pygame.K_LEFT:
                    b1.swipe_left(screen)
                elif event.key == pygame.K_RIGHT:
                    b1.swipe_right(screen)
                elif event.key == pygame.K_r :
                    b1.restart()
                elif event.key == pygame.K_ESCAPE:
                    on = False
					
                elif event.key == pygame.K_SPACE: # fill function
                    b1.display_score(screen)
            
                b1.box_add_check()
                b1.judge(screen)
				
def message_display(text,size,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text_surface , text_rectangle = text_objects(text,font)
	text_rectangle.center =(x,y)
	screen.blit(text_surface,text_rectangle)
    
def text_objects(text,font):
	textSurface = font.render(text,True,white)
	return textSurface,textSurface.get_rect()

intro()
gameloop()    
    
pygame.quit()

