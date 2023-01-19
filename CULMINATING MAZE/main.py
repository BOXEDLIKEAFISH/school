# ICS4U1 Culminating
# Kris Kuo
# 1/18/23
# Multi level maze game where you collect the tvs around the map 
# Must collect all tvs before going to the slurpfish and advancing to the next level

import pygame   # import pygame
import time    # import time

pygame.init()   # initialize pygame
pygame.mixer.init() # initialize pygame mixer
display = pygame.display.set_mode((1000, 1000))   # set display size
pygame.display.set_caption("Bert The TV Collector")   # set display caption

background = pygame.image.load("imports/background.png")    # declare all background images
background = pygame.transform.scale(background, (1000, 1000))   # transform images to display size

background2 = pygame.image.load("imports/background2.png")    
background2 = pygame.transform.scale(background2, (1000, 1000))   

background3 = pygame.image.load("imports/background3.png")
background3 = pygame.transform.scale(background3, (1000, 1000)) 

background4 = pygame.image.load("imports/background4.png")
background4 = pygame.transform.scale(background4, (1000, 1000)) 

background5 = pygame.image.load("imports/background5.png")
background5 = pygame.transform.scale(background5, (1000, 1000))


bert = pygame.image.load("imports/bert.png")    # load bert picture
bert = pygame.transform.scale(bert, (1000, 1000)) # transform bert picture size 

tv = pygame.image.load("imports/tv.png")    # load tv picture

wall = pygame.image.load("imports/coral.png")    # load wall picture

clock = pygame.time.Clock() # create clock to tick the game loop

levelstart = False  # set levelstart to false
level = 1  # level variable starts at level 1

startgame = True    # condition for game menu loop

class walls:    # wall class
    def __init__(self, x, y, width, rect):
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.width = width  # size of wall
        self.rect = rect    # rect object of the wall

    def draw(self, rect):   # draw wall
        display.blit(wall, rect)    

class tvs:  # tv class
    def __init__(self, x, y, width, rect):
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.width = width  # size of tv
        self.rect = rect    # rect object of the tv

    def draw(self, rect):   # draw tv
        display.blit(tv, rect)


walllist = []   # list of wall rects
tvlist = [] # list of tv rects
tvspawns = [1, 1]   # list of which tvs are currently uncollected 

tvcountperlevel = [2, 3, 4, 4, 5, 0]    # list of how many tvs are in each level

tvcounter = 0   # variable for amount of tvs collected in current level

start = (0, 0)  # set spawn location to (0, 0)
x = 0   # set x coordinate to 0
y = 0   # set y coordinate to 0

w = False   # booleans for movement directions
a = False   
s = False   
d = False   

direction = 'left'  # direction of movement

gameon = True   # boolean which controls the main loop

character = pygame.image.load("imports/flopper.png")    # load player character image
slurpfish = pygame.image.load("imports/slurpfish.png")  # load slurpfish image

characterrect = 0   # declare rect object of the player model
slurpfishrect = 0  # declare rect object of the slurpfish


level1 = [      # map of level 1
' XT  X XXP',   # P is the player start
' XX  X  X ',   # T is the tv spawns
' X  XX XX ',   # X is the walls
'          ',
'XXX X XXX ',
'   XX   X ',
' X  XXX XX',
' XX      X',
'  XXXX X X',
'E X    X T'    # E is the end of the level
]

level2 = [  
'           P',
' XXXXXXXXXXX',
' X          ',
' X XXXXXXX  ',
'   X        ',
'XX X XXXXXX ',
'   X    TX  ',
' XXXXXXXXX  ',
' X          ',
' X   XXXXXX ',
' XXX   X    ',
'TXT    XE   '
]

level3 = [
'T    X       XP  ',
'XXXX X XXXXX XXX ',
'       X      TX ',
' XXXXX XXXXXXX X ',
'   X         X   ',
' X X XXXXXXX XXXX',
' X X       X     ',
'XX XXX X X XXX X ',
'   X   X XT  X X ',
' XXXXXXX XXX X X ',
' XEX   X     X X ',
' X X X X XXX X XX',
' X   X X X   X   ',
' XXXXX X X XXXXX ',
'  X    X       X ',
'  X XXTXXXX       ',
'  X  XXX X       ',
'                 ',
]

level4 = [
'   X   X    PX       ',
' X X X X X XXX XXXXX ',
' XTX X   X X   X   X ',
' XXX X XXX X XXX X X ',
'     X X   X X   XTX ',
'XXXX X X XXX X XXXXX ',
'     X X X   X X   X ',
' X XXX X XXXXX X X X ',
' X XT  X     X X X X ',
' X XXXXXXXXX X X XXX ',
' X         X X X X   ',
' XXXXXXXXX X X X X XX',
' X  EX     X     X   ',
' X XXX XXXXXXXXX X X ',
' X   X     X   X   X ',
' XXX XXXXX X X XXXXX ',
'   X     X   X X     ',
'XX X XXX XXXXX XXX XX',
'   X X X   X     X XT',
' XXX X X XXX XXX X X ',
'     X   X   X   X   '
]

level5 = [
'T  X   X P   X X    ',
'XX    XX     X   XX ',
'         X X X   X  ',
' XXXXXXXXX X X     XX',
' X     X   X   X X X',
'XX XXX XXXXXXX X X X ',
'   X X   X       X   ',
' X X XXX XXX X XXX XX',
' XTX  TX   X X   X   ',
' XXX XXXXX XXXXXXXXX ',
'   X X   X     X     ',
'XX X X X XXX XXX X XX',
'   X   X   X   X X X ',
' XXXXXXX XXXXX X X X ',
'       X X     X X X ',
' XXXXX X X X XXX X X ',
' X     X X X X   X   ',
' XXXXXXX X X XXXXXXX ',
' X   XT    X X       ',
' X X XXXXXXX X XXXXX ',
'   X      EX   XT    '
]


def draw_level(level):  # draw level using the map variable
    global wall # all variables which will be changed
    global wallsize
    global start
    global slurpfishrect
    global character 
    global slurpfish
    global tv
    wallsize = 1000/len(level)  # set new wall size based on the size of the map
    wall = pygame.transform.scale(wall, (wallsize, wallsize))   # scale wall image to the right size
    character = pygame.transform.scale(character, (wallsize * 0.6, wallsize * 0.6)) # scale character model to the right size
    slurpfish = pygame.transform.scale(slurpfish, (wallsize * 0.9, wallsize * 0.9)) # scale slurpfish model to the right size
    tv = pygame.transform.scale(tv, (wallsize, wallsize * 0.6)) # scale tv model to the right size
    for y in range(len(level)): # loop for each row of the map
        for x in range(len(level[y])):  # loop for each column of the map
            if level[y][x] == 'X':  # if it is a wall
                walllist.append(walls(x, y, wallsize, wall.get_rect(topleft = (x * wallsize, y * wallsize))))   # add rect object to the list of wall rects
                walllist[-1].draw(walllist[-1].rect)    # draw wall
            elif level[y][x] == 'T' and tvspawns[len(tvlist)] == 1: # if it is a tv and it hasnt been collected yet
                tvlist.append(tvs(x, y, wallsize, tv.get_rect(topleft = (x * wallsize, y * wallsize + 20))))    # add rect object to the list of tv rects
                tvlist[-1].draw(tvlist[-1].rect)    # draw tv
            elif level[y][x] == 'T':    # if it is a tv and it has been collected
                tvlist.append(tvs(x, y, wallsize, tv.get_rect(topleft = (4000, 4000)))) # create dummy rect off the map and add to list
            elif level[y][x] == 'P':    # if it is the player spawn
                start = (x * wallsize + wallsize/2, y * wallsize + wallsize/2)  # change the start variable to the right coordinates
            elif level[y][x] == 'E':    # if it is the end of the level
                slurpfishrect = slurpfish.get_rect(topleft = (x * wallsize, y * wallsize))  # create rect object for the slurpfish
                display.blit(slurpfish, slurpfishrect)  # draw slurpfish

def draw_flopper(direction, coordinates):   # draw character model
    global characterrect

    if direction == 'down': # if moving down
        flopper = pygame.transform.rotate(character, 90)    # make flopper face down
    elif direction == 'up': # if moving up
        flopper = pygame.transform.rotate(character, 270)   # make flopper face up
    elif direction == 'right':  # if moving right
        flopper = pygame.transform.flip(character, True, False) # make flopper face right
    elif direction == 'left':   # if moving left
        flopper = pygame.transform.rotate(character, 0) # make flopper face left
    characterrect = character.get_rect(center = coordinates)    # create rect object for the character model
    display.blit(flopper, characterrect)    # draw character model

def showscore(numtv, totaltv):  # show number of tvs collected
    font = pygame.font.SysFont('Arial', 35) # set font
    text = font.render('I need more TVs!!! (' + str(numtv) + '/' + str(totaltv) + ')', True, (0, 0, 0)) # display message and number of tvs collected
    display.blit(bert, (200, 200))  # display bert picture
    display.blit(text, (260, 300))  # display text

startloop = 0  # variable to loop through the opening screen

pygame.mixer.music.load('imports/clown.mp3') # load starting menu music 
pygame.mixer.music.play(-1) # play and loop starting menu music

while startgame == True:
    display.blit(bert, (0, 0))  # display bert background
    font = pygame.font.SysFont('Arial', 30) # set font
    if startloop != 5:      # if not on the last screen
        text = font.render('(Press any key to continue)', True, (0, 0, 0))  # display press and key to continue
        display.blit(text, (230, 300))
    
    if startloop == 0:  #first screen
        font = pygame.font.SysFont('Arial', 70) # display message
        text = font.render('Hey, kid.', True, (0, 0, 0))
        display.blit(text, (260, 160))

    elif startloop == 1:    # second screen
        font = pygame.font.SysFont('Arial', 70)
        text = font.render('I need some TVs.', True, (0, 0, 0))
        display.blit(text, (150, 160))

    elif startloop == 2:    # third screen
        font = pygame.font.SysFont('Arial', 70)
        text = font.render('Can you help me?', True, (0, 0, 0))
        display.blit(text, (140, 160))

    elif startloop == 3:   # fourth screen
        font = pygame.font.SysFont('Arial', 45)
        text = font.render('There\'s 5 floors of this store.', True, (0, 0, 0))
        display.blit(text, (110, 170))

    elif startloop == 4:    # fifth screen
        font = pygame.font.SysFont('Arial', 45)
        text = font.render('I need you to get all the Tvs.', True, (0, 0, 0))
        display.blit(text, (120, 170))

    elif startloop == 5:    # last screen
        font = pygame.font.SysFont('Arial', 45)
        text = font.render('I\'ll be waiting for you', True, (0, 0, 0))
        display.blit(text, (170, 150))
        text = font.render('at the end of each floor.', True, (0, 0, 0))
        display.blit(text, (170, 200))
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('(Press any key to start)', True, (0, 0, 0))
        display.blit(text, (230, 300))

    pygame.display.update() # update display
    for event in pygame.event.get():    # check user inputs
        if event.type == pygame.QUIT:   # if user closes pygame window
            pygame.quit()   # quit pygame
        if event.type == pygame.KEYDOWN:    # if user presses a key
            if startloop == 5:  # if on the last screen
                startgame = False   # stop the opening screen loop
            startloop += 1  # else go to the next screen

pygame.mixer.stop()    # stop starting menu music
pygame.mixer.music.load('imports/song.mp3') # load background music 
pygame.mixer.music.play(-1) # play and loop background music

bert = pygame.transform.scale(bert, (600, 600)) # transform bert picture size 


while gameon == True:   # main game loop
    walllist = []   # clear list of wall rects
    tvlist = [] # clear list of tv rects
    collide = False # set collision boolean to false
    if level == 1:  # level 1
        display.blit(background, (0, 0))    # set background
        draw_level(level1)  # draw level
    elif level == 2:    # level 2
        display.blit(background2, (0, 0))   # set background
        draw_level(level2)  # draw level
    elif level == 3:    # level 3
        display.blit(background3, (0, 0))   # set background
        draw_level(level3)  # draw level
    elif level == 4:    # level 4
        display.blit(background4, (0, 0))   # set background
        draw_level(level4)  # draw level
    elif level == 5:    # level 5
        display.blit(background5, (0, 0))   # set background
        draw_level(level5)  # draw level
    elif level == 6:    # all levels completed
        gameon = False  # end main game loop
        

    if levelstart == False: # if level hasnt been set up yet
        x = start[0]    # set x coordinate to start 
        y = start[1]    # set y coordinate to start
        characterrect = character.get_rect(center = (x, y)) # create rect object for the character
        levelstart = True   # set levelstart boolean to true to signify the set up is done

    for i in walllist:  # for every wall
        if characterrect.colliderect(i.rect):   # if character is collided with the wall
            if direction == 'up':   # move in the opposite direction to go out of the wall
                y += 5  
            if direction == 'left':
                x += 5
            if direction == 'down':
                y -= 5
            if direction == 'right':
                x -= 5
            collide = True  # set the collide boolean to true
            break   # break loop to not trigger multiple times on a single collision

    if characterrect.colliderect(slurpfishrect) and tvcounter == len(tvlist):   # if character is at the end and all tvs have been collected
        tvspawns = []   # reset tv spawns
        level += 1  # add 1 to level variable to go to the next level
        levelstart = False  # set up level on the next loop
        tvcounter = 0   # set number of collected tvs back to 0
        for i in range(tvcountperlevel[level - 1]): # set tvs collected to none
            tvspawns.append(1)
    elif characterrect.colliderect(slurpfishrect) and tvcounter != len(tvlist): # if character is at the end and tvs have not been collected
        showscore(tvcounter, len(tvlist))   # call show score function to display number of tvs collected
    
    for i in tvlist:    # for every tv
        if characterrect.colliderect(i.rect):   # if character is collided with the tv
            tvcounter += 1  # add 1 to number of tvs collected
            tvspawns[tvlist.index(i)] = 0   # set that tv to collected so it doesnt get drawn again
            break   # break loop to not trigger multiples times on a single collision
    

    if collide == False:    # does not trigger in a collision so that you cannot change direction while collided
        for event in pygame.event.get():    # check user inputs
            if event.type == pygame.QUIT:   # if pygame is closed
                pygame.quit()   # quit pygame
            if event.type == pygame.KEYDOWN:    # if input is a button press
                if event.key == pygame.K_w: # if input is 'w'
                    w = True    # set 'w' boolean to true
                elif event.key == pygame.K_a:   # if input is 'a'
                    a = True    # set 'a' boolean to true
                elif event.key == pygame.K_s:   # if input is 's'
                    s = True    # set 's' boolean to true
                elif event.key == pygame.K_d:   # if input is 'd'
                    d = True    # set 'd' boolean to true
            elif event.type == pygame.KEYUP:    # if input is a button release
                if event.key == pygame.K_w: # if w key was released
                    w = False   # set 'w' boolean to false
                elif event.key == pygame.K_a:   # if a key was released
                    a = False   # set 'a' boolean to false
                elif event.key == pygame.K_s:   # if s key was released
                    s = False   # set 's' boolean to false
                elif event.key == pygame.K_d:   # if d key was released
                    d = False   # set 'd' boolean to false

        if w == True and y >= 1:    # if moving up and not outside the map
            y -= 20//level  # move up 
            direction = 'up'    # set direction to up
        elif a == True and x >=1 :  # if moving left and not outside the map
            x -= 20//level  # move left
            direction = 'left'  # set direction to left
        elif s == True and y <= 999:    # if moving down and not outside the map
            y += 20//level  # move down
            direction = 'down'  # set direction to down
        elif d == True and x <= 999:    # if moving right and not outside the map
            x += 20//level  # move right
            direction = 'right' # set direction to right

    draw_flopper(direction, (x, y)) # call function to draw the character
    pygame.display.update() # update display

    clock.tick(30)  # tick 30 times in a second

# OUTSIDE OF GAME LOOP
# TRIGGERS WHEN GAME ENDS

pygame.mixer.stop() # stop current music

pygame.mixer.music.load('imports/endsong.mp3')  # load ending music
pygame.mixer.music.play(-1) # play and loop ending music

bert = pygame.image.load("imports/bert.png")    # load bert picture
bert = pygame.transform.scale(bert, (1000, 1000))   # scale bert picture to display size

font = pygame.font.SysFont('Arial', 70) # set font
text = font.render('You won the game!!' , True, (0, 0, 0))  # set text 

display.blit(bert, (0, 0))  # display bert picture
display.blit(text, (100, 170))  # display text
pygame.display.update() # update display

time.sleep(5)   # delay 5 seconds

nle = pygame.image.load("imports/nlefloppa.png")    # load nle floppa picture
nle = pygame.transform.scale(nle, (1000, 1000)) # scale nle floppa picture to display size

display.blit(nle, (0, 0))   # display nle floppa picture
pygame.display.update() # update display

while True: # loop forever
    for event in pygame.event.get():    # check user input
        if event.type == pygame.QUIT:   # if user closes the pygame window
            pygame.quit()   # quit pygame