#Anna Breton
import pygame, sys, random, array, pygame.mixer, time 
from pygame.locals import * #imports keys
clock = pygame.time.Clock()#load clock
pygame.init()
#play the sound 
sound = pygame.mixer.music.load("16-dark-rooms.mp3")
pygame.mixer.music.play(-1,0.0)#-1 means repeat, 0.0 is where in the song it starts to play
#----------timer stuff
counter, text = 10, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 500)
font = pygame.font.SysFont('Consolas', 20)
#---------set window
size = (width,height)= (600,450)
window = pygame.display.set_mode(size)
#-----Create Luigi as a sprite
LuigiX =50 # width  of Luigi Image
LuigiY=50  # height of Luigi Image
s = pygame.sprite.Sprite()  # create a sprite
s.image = pygame.image.load("luigi.jpg")
s.image = pygame.transform.scale(s.image,(LuigiX,LuigiY))
s.rect = pygame.Rect(50, 100, LuigiX,LuigiY) # start luigi at location 50,100, scale is 50x50
pygame.display.flip()
#---- load the boos image
g = pygame.image.load("Boo_new.png")
g = pygame.transform.scale(g,(50,50))
g_w = 50
g_h = 50
#------------------------
logo = pygame.image.load("Logo_Luigi_Mansion.png")
boo_offset = 0
flashlight_range = 0
num_boos= 10
boo_x=[1,2,3,4,5,6,7,8,9,10]
boo_y=[1,2,3,4,5,6,7,8,9,10]
boo_found=[1,2,3,4,5,6,7,8,9,10]
#place boos randomly in window
for n in range(num_boos):
    boo_x[n] = random.randint(100,550)
    boo_y[n] = random.randint(100,400)
    boo_found[n]= 0
#---------------------------------------------------------------------    
wind=[1,2,3,4]
background = (0,0,0)
#----------------- Draw all the scary windows as sprites ------------
def DrawWindows():
    #window 1 sprite
    wind[1] = pygame.sprite.Sprite()  # create a sprite
    wind[1].image = pygame.image.load("luigi_window.png")
    wind[1].image = pygame.transform.scale(wind[1].image,(100,100))
    wind[1].rect = pygame.Rect(100, 0, 100,100) #Location, size
    #window 2 sprite
    wind[2] = pygame.sprite.Sprite()  # create a sprite
    wind[2].image = pygame.image.load("luigi_window.png")
    wind[2].image = pygame.transform.scale(wind[2].image,(100,100))
    wind[2].rect = pygame.Rect(300, 0, 100,100)
    #window 3 sprite
    wind[3] = pygame.sprite.Sprite()  # create a sprite
    wind[3].image = pygame.image.load("luigi_window.png")
    wind[3].image = pygame.transform.scale(wind[3].image,(100,100))
    wind[3].rect = pygame.Rect(500, 0, 100,100)
    #display the scary windows
    window.blit(wind[1].image, wind[1].rect.topleft)
    window.blit(wind[2].image, wind[2].rect.topleft)
    window.blit(wind[3].image, wind[3].rect.topleft)
    pygame.display.flip()
#-----------------------did Luigi bump against a window?
def ScaryWindowsCollision():
    if pygame.sprite.collide_rect(s, wind[1]):
        return 1
    if pygame.sprite.collide_rect(s, wind[2]):
        return 1 
    if pygame.sprite.collide_rect(s, wind[3]):
        return 1
    return 0
# ------------------is luigi against a wall
def AtWall(x,y):
    if s.rect.y  + y > 400:
        return 1
    if s.rect.y  +y < 0:
        return 1
    if s.rect.x  + x > 550:
        return 1
    if s.rect.x  +x < 0:
        return 1
    return 0
#----------------sets the teo key modes, e or x------------------------------
def getmode():
    mode = 0
    while mode == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_e:
                    mode = "e"
                    break
                if event.key == K_x:
                    mode = "x"
                    break
    return mode 
#-------------------------------------------------------------------------                
color= (255,0,0)
#---splash screen- the growing boo
splash = pygame.image.load("Boo_new.png")
background = (0,0,0)
for n in range(100,600,100):
    splash = pygame.transform.scale(splash,(n,n))
    window.blit(splash,(0,0))
    pygame.display.flip()
    pygame.time.delay(500)
    window.fill(background)
#---end splash and display the name of the game
logo = pygame.transform.scale(logo,(width,height-60))
window.blit(logo,(0,0))
pygame.display.flip()
pygame.font.init()
my_font = pygame.font.SysFont('Chiller', 60)
rendered =  my_font.render("Ghost hunt",0,(123,163,214))
window.blit(rendered, (20,height-60))
pygame.display.flip()
pygame.time.delay(2000)
#-------Ask if they want easy or expert
pygame.font.init()
my_font = pygame.font.SysFont('Chiller', 50)
rendered =  my_font.render("Press 'e' for easy or 'x' for expert",0,(255,0,0))
window.blit(rendered, (20,height//2))
pygame.display.flip()
mode = getmode()
#Set levels-----------------------------------------------------------
if mode == "e":
    flashlight_range = 50 # easier has a biger flashlight range
if mode == "x":
    flashlight_range = 20
pygame.key.set_repeat(10,10)
background = (0,0,0)
window.fill(background)
#---------instructions
pygame.font.init()
my_font = pygame.font.SysFont('Corbel', 25)
rendered =  my_font.render("Instructions: 10 ghosts have taken over Luigi's Masion!",0,(0,255,0))
window.blit(rendered, (0,height//2.25))
rendered =  my_font.render("Remeber where they are and help Luigi",0,(0,255,0))
window.blit(rendered, (0,height//2))
rendered =  my_font.render("catch them all before time runs out!",0,(0,255,0))
window.blit(rendered, (0,height//1.75))
pygame.display.flip()
pygame.time.delay(6000)
#----------flash all the ghosts in the beginning
for n in range(1,num_boos):
    window.blit(g,(boo_x[n],boo_y[n]))
    pygame.display.flip()
    pygame.time.delay(500)
    window.fill(background)
DrawWindows() # draw the scary windows
#---------------set countdown clock
counter =30 #time in seconds
pygame.time.set_timer(USEREVENT+1, 1000)#1 second is 1000 milliseconds 
#---------------main loop
Gameover = 0
while Gameover == 0:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            sound.play()
        if event.type == KEYDOWN and event.key == K_UP:
            if AtWall(0,-1) == 0:
                s.rect.y = s.rect.y -1
                if ScaryWindowsCollision() == 1:
                    s.rect.y = s.rect.y +1
            else: # we are at the wall at the top.  Move one space down
                s.rect.y = s.rect.y + 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            if AtWall(0,1) == 0:
                s.rect.y = s.rect.y +1
                if ScaryWindowsCollision() == 1:
                    s.rect.y = s.rect.y +1
            else :# we are at the wall at the bottom.  Move one space up
                  s.rect.y = s.rect.y -1
        elif event.type == KEYDOWN and event.key == K_LEFT:
            if AtWall(-1,0) == 0:
                s.rect.x = s.rect.x -1
                if ScaryWindowsCollision() == 1:
                    s.rect.x = s.rect.x +1
            else: # we are on the left side of the room
                s.rect.x = s.rect.x +1
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            if AtWall(1,0) == 0:
                s.rect.x = s.rect.x +1
                if ScaryWindowsCollision() == 1:
                    s.rect.x = s.rect.x -1
            else: # we are on the right side of the room 
                s.rect.x = s.rect.x -1
        #show the boo if luigi has found it         
        for n in range(num_boos):
            if (abs(s.rect.x-boo_x[n]) < flashlight_range) and (abs(s.rect.y-boo_y[n]) < flashlight_range):
                 #print("found boo",n,boo_x[n],boo_y[n])
                 boo_found[n]= 1
                 window.blit(g,(boo_x[n],boo_y[n]))
                 pygame.display.flip()
            else:
                window.blit(s.image,s.rect.topleft)
                pygame.display.flip()
        #redraw all the boos that are visible and test to see if you have all the boos
        num_found = 0
        for n in range(num_boos):
            if boo_found[n]== 1:
                num_found= num_found +1
                window.blit(g,(boo_x[n],boo_y[n]))
                pygame.display.flip()
        if num_found == 10:#----if you win the game
            my_font = pygame.font.SysFont('Chiller', 45)
            rendered =  my_font.render("GAME OVER.YOU WON! Press X to exit",0,(255,0,0))
            window.blit(rendered, (20,height//2))
            pygame.draw.rect(window, (0,0,0),(10,10,50,50))
            pygame.display.flip()
            Gameover = 1
        #---------this is the timer section
        if event.type == pygame.USEREVENT+1: 
            counter -= 1
            if counter > 0:
                text = str(counter).rjust(3)
            else:#---------show GAME OVER at end of game
                my_font = pygame.font.SysFont('Chiller', 45)
                rendered =  my_font.render("GAME OVER.YOU LOST! Press X to exit",0,(255,0,0))
                window.blit(rendered, (20,height//2))
                pygame.draw.rect(window, (0,0,0),(10,10,50,50))
                pygame.display.flip()
                Gameover = 1
        else: 
            pygame.draw.rect(window, (0,0,0),(10,10,50,50))
            window.blit(font.render(text, True, (0,255,0)), (10,10))
            pygame.display.flip()
        #-----------------------end timer section
pygame.display.flip()
#paint the window
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_x:
                pygame.quit()
                sys.exit()
