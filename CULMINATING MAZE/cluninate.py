import pygame   # Import pygame
import time    # Import time

pygame.init()   # Initialize pygame
pygame.mixer.init() # Initialize pygame mixer
display = pygame.display.set_mode((1000, 1000))   # Set display size
pygame.display.set_caption("Bert The TV Boss")   # Set display caption

song = pygame.mixer.Sound('song.mp3')
pygame.mixer.Sound.play(song)

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1000, 1000)) 

background2 = pygame.image.load("background2.png")    
background2 = pygame.transform.scale(background2, (1000, 1000))   

background3 = pygame.image.load("background3.png")
background3 = pygame.transform.scale(background3, (1000, 1000)) 

background4 = pygame.image.load("background4.png")
background4 = pygame.transform.scale(background4, (1000, 1000)) 

background5 = pygame.image.load("background5.png")
background5 = pygame.transform.scale(background5, (1000, 1000))


bert = pygame.image.load("bert.png")
bert = pygame.transform.scale(bert, (600, 600))

tv = pygame.image.load("tv.png")    # Load tv image

wall = pygame.image.load("coral.png")    # Load wall image  

clock = pygame.time.Clock() # Set clock

levelstart = False  # Set levelstart to false
level = 1  # Set level to 1

class walls:
    def __init__(self, x, y, width, rect):
        self.x = x
        self.y = y
        self.width = width
        self.rect = rect

    def draw(self, rect):
        display.blit(wall, rect)

class tvs:
    def __init__(self, x, y, width, rect):
        self.x = x
        self.y = y
        self.width = width
        self.rect = rect

    def draw(self, rect):
        display.blit(tv, rect)


walllist = []   # Set walllist to empty list
tvlist = [] # Set tvlist to empty list
tvspawns = [1, 1]

tvcountperlevel = [2, 3, 4, 4, 5, 0]

tvcounter = 0

start = (0, 0)  # Set start to (0, 0)
x = 0   # Set x to 0
y = 0   # Set y to 0

w = False   # Set w to false
a = False   # Set a to false
s = False   # Set s to false
d = False   # Set d to false

direction = 'left'  # Set direction to left

gameon = True   # Set gameon to true

character = pygame.image.load("flopper.png")    # Load character image

slurpfish = pygame.image.load("slurpfish.png")  # Load slurpfish image


characterrect = 0    # Set characterrect to 0
slurpfishrect = 0  # Set slurpfishrect to 0




level1 = [      # map of level 1
' XT  X XXP',   # P is the player start
' XX  X  X ',
' X  XX XX ',
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


def draw_level(level):
    global wall
    global wallsize
    global start
    global slurpfishrect
    global character 
    global slurpfish
    global tv
    wallsize = 1000/len(level)
    wall = pygame.transform.scale(wall, (wallsize, wallsize)) # Scale wall image
    character = pygame.transform.scale(character, (wallsize * 0.6, wallsize * 0.6))
    slurpfish = pygame.transform.scale(slurpfish, (wallsize * 0.9, wallsize * 0.9))
    tv = pygame.transform.scale(tv, (wallsize, wallsize * 0.6))
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'X':
                walllist.append(walls(x, y, wallsize, wall.get_rect(topleft = (x * wallsize, y * wallsize))))
                walllist[-1].draw(walllist[-1].rect)
            elif level[y][x] == 'T' and tvspawns[len(tvlist)] == 1:
                tvlist.append(tvs(x, y, wallsize, tv.get_rect(topleft = (x * wallsize, y * wallsize + 20))))
                tvlist[-1].draw(tvlist[-1].rect)
            elif level[y][x] == 'T':
                tvlist.append(tvs(x, y, wallsize, tv.get_rect(topleft = (4000, 4000))))
            elif level[y][x] == 'P':
                start = (x * wallsize + wallsize/2, y * wallsize + wallsize/2)
            elif level[y][x] == 'E':
                slurpfishrect = slurpfish.get_rect(topleft = (x * wallsize, y * wallsize))
                display.blit(slurpfish, slurpfishrect)

def draw_flopper(direction, coordinates):
    global characterrect

    if direction == 'down':
        flopper = pygame.transform.rotate(character, 90)
    elif direction == 'up':
        flopper = pygame.transform.rotate(character, 270)
    elif direction == 'right':
        flopper = pygame.transform.flip(character, True, False)
    elif direction == 'left':
        flopper = pygame.transform.rotate(character, 0)
    characterrect = character.get_rect(center = coordinates)
    display.blit(flopper, characterrect)

def showscore(numtv, totaltv):

    font = pygame.font.SysFont('Arial', 43)
    text = font.render('I need more TVs!!! (' + str(numtv) + '/' + str(totaltv) + ')', True, (0, 0, 0))
    display.blit(bert, (200, 200))
    display.blit(text, (260, 300))


while gameon == True:
    walllist = []
    tvlist = []
    collide = False
    if level == 1:
        display.blit(background, (0, 0))
        draw_level(level1)
    elif level == 2:
        display.blit(background2, (0, 0))
        draw_level(level2)
    elif level == 3:
        display.blit(background3, (0, 0))
        draw_level(level3)
    elif level == 4:
        display.blit(background4, (0, 0))
        draw_level(level4)
    elif level == 5:
        display.blit(background5, (0, 0))
        draw_level(level5)
    elif level == 6:
        gameon = False
        

    if levelstart == False:
        x = start[0]
        y = start[1]
        characterrect = character.get_rect(center = (x, y))
        levelstart = True


    for i in walllist:
        if characterrect.colliderect(i.rect):
            if direction == 'up':
                y += 5
            if direction == 'left':
                x += 5
            if direction == 'down':
                y -= 5
            if direction == 'right':
                x -= 5
            collide = True
            break

    if characterrect.colliderect(slurpfishrect) and tvcounter == len(tvlist):
        tvspawns = []
        level += 1
        levelstart = False
        tvcounter = 0
        for i in range(tvcountperlevel[level - 1]):
            tvspawns.append(1)
    elif characterrect.colliderect(slurpfishrect) and tvcounter != len(tvlist):
        showscore(tvcounter, len(tvlist))
    
    for i in tvlist:
        if characterrect.colliderect(i.rect):
            tvcounter += 1
            tvspawns[tvlist.index(i)] = 0
            break
    

    if collide == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w = True
                elif event.key == pygame.K_a:
                    a = True
                elif event.key == pygame.K_s:
                    s = True
                elif event.key == pygame.K_d:
                    d = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w = False
                elif event.key == pygame.K_a:
                    a = False
                elif event.key == pygame.K_s:
                    s = False
                elif event.key == pygame.K_d:
                    d = False

        if w == True and y >= 1:
            y -= 25/level
            direction = 'up'
        elif a == True and x >=1 :
            x -= 25/level
            direction = 'left'
        elif s == True and y <= 999:
            y += 25/level
            direction = 'down'
        elif d == True and x <= 999:
            x += 25/level
            direction = 'right'

    draw_flopper(direction, (x, y))

    clock.tick(30)

pygame.mixer.stop()

endsong = pygame.mixer.Sound('endsong.mp3')
pygame.mixer.Sound.play(endsong)

bert = pygame.image.load("bert.png")
bert = pygame.transform.scale(bert, (1000, 1000))

font = pygame.font.SysFont('Arial', 70)
text = font.render('You won the game!!' , True, (0, 0, 0))

display.blit(bert, (0, 0))
display.blit(text, (100, 170))
pygame.display.update()

time.sleep(5)

nle = pygame.image.load("nlefloppa.png")
nle = pygame.transform.scale(nle, (1000, 1000))

display.blit(nle, (0, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
