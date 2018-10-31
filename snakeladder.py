import random
import pygame
import os, sys
from time import sleep


APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))




width=800 #game playing area width
hight=800 #game playing area hight
side_width=400 #game side pannel width
size = (width+side_width,hight) #list of game window size coordinate

button_x=20 #player button starting x position
button_y=hight-(20+50) #player button starting y position
dice_cor=(960,210) #the coordinates where the dice appears

number_players=2 # default number of players
running = True #the game is running flag
game_finish=False #game is finished flag

background = pygame.image.load(APP_FOLDER+"/graphics/snakeladder.png") #game background



pygame.init()
screen = pygame.display.set_mode(size)



def cast_dice():
    global dice_cor
    dice1 = pygame.image.load(APP_FOLDER+"/graphics/dice1.png")
    dice2 = pygame.image.load(APP_FOLDER+"/graphics/dice2.png")
    dice3 = pygame.image.load(APP_FOLDER+"/graphics/dice3.png")
    dice4 = pygame.image.load(APP_FOLDER+"/graphics/dice4.png")
    dice5 = pygame.image.load(APP_FOLDER+"/graphics/dice5.png")
    dice6 = pygame.image.load(APP_FOLDER+"/graphics/dice6.png")

    screen.blit(dice2,dice_cor)
    pygame.display.update()
    #sleep(0.2)
    screen.blit(dice5,dice_cor)
    pygame.display.update()
    #sleep(0.2)
    screen.blit(dice3,dice_cor)
    pygame.display.update()
    #sleep(0.2)
    screen.blit(dice6,dice_cor)
    pygame.display.update()
    #sleep(0.2)
    screen.blit(dice1,dice_cor)
    pygame.display.update()
    #sleep(0.2)
    screen.blit(dice4,dice_cor)
    pygame.display.update()
    #sleep(0.2)

    random.seed()
    rnd=random.randrange(1,6)

    if (rnd==1):
        screen.blit(dice1,dice_cor)
    if (rnd==2):
        screen.blit(dice2,dice_cor)
    if (rnd==3):
        screen.blit(dice3,dice_cor)
    if (rnd==4):
        screen.blit(dice4,dice_cor)
    if (rnd==5):
        screen.blit(dice5,dice_cor)
    if (rnd==6):
        screen.blit(dice6,dice_cor)

    pygame.display.update()
    return rnd


class Player:
    global screen
    global background
    color=0 #button color
    name="" #player name
    position=1 #button step position
    x=0 #button x coordinate on screen
    y=0 #button y coordinate on screen
    win=False #wining status
    win_count=0 #number of wins
    player_image=None

    def __init__(self, player_name,x_cor,y_cor,color):
        self.name = player_name
        self.x=x_cor
        self.y=y_cor
        #self.color = pygame.image.load(APP_FOLDER+"/graphics/"+color+"_button.png")
        self.color = pygame.sprite.Sprite()
        self.color.image = pygame.image.load(APP_FOLDER+"/graphics/"+color+"_button.png").convert()

    def change_position(self, steps,shift): #shift for a second and third, .. buttons so they can't overlaps when they are in the same position
        if (self.position==(10*int(self.position/10))):
            row = int(self.position/10)
        else:
            row = int(self.position/10)+1
        print("row ",row )


        if ((self.position+steps)>100):
            steps = 100-self.position



        self.position=self.position+steps
        print ("position ",self.position)

        if (self.position > 10*row ):
            print("change row")
            self.x=button_x + ( ( (self.position -1) - (row*10)) * 80)
            self.y=button_y - (row*80) + shift
        else:
            self.x=self.x+(steps*80)

        if (self.position>=100):
            self.win=True
            self.win_count+=1

    def update_play_ground(self):
        #screen.blit(self.color, (self.x,self.y))
        self.color.rect = self.color.image.get_rect().move(self.x,self.y)



def winner(win):
    print(win.name+" is the winner")


def text_to_screen(screen, text, x, y, size = 50, color = (200, 000, 000), font_type = 'data/fonts/orecrusherexpand.ttf'):

    text = str(text)
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

# -------- Main Program Loop -----------


def main():
    global APP_FOLDER, width, hight, side_width, red_x, red_y, blue_x, blue_y, dice_cor
    global screen, number_players, running, game_finish

    turn=0 #player turn, 0: first player, 1: second player and so on

    if(number_players==2):
        red=Player("Ali", button_x, button_y,"red")
        blue=Player("Ahmed", button_x+5, button_y+5,"blue")
        players=[red,blue]




    pygame.display.set_caption("Snakes and Ladder")
    side_pannel = pygame.image.load(APP_FOLDER+"/graphics/side_pannel.png")
    text_to_screen(screen, "0", 860,510 )
    text_to_screen(screen, "0", 1060,510 )
    screen.blit(side_pannel, (width,0))
    screen.blit(background, (0,0))
    red.update_play_ground()
    blue.update_play_ground()
    pygame.display.flip()


    cast_dice()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and game_finish==False:

                    dice_no=cast_dice()
                    print(dice_no)
                    players[turn].change_position(dice_no, turn*5)
                    screen.blit(background, (0,0))
                    for i in range(number_players):
                        players[i].update_play_ground()

                    pygame.display.update()

                    if (players[turn].win==True):
                        winner(players[turn])
                        game_finish=True

                    turn+=1
                    if(turn>number_players-1):
                        turn=0






if __name__ == '__main__':
    main()


pygame.quit()