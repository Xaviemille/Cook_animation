import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = int(SCREEN_WIDTH) * 1

#Creating game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Giving a window title
pygame.display.set_caption("Dinnerdash")


#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
BG = (144, 201, 120)
RED = (255, 0, 0)

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = []
        self.frame_index = 0 
        self.update_time = pygame.time.get_ticks()
        for i in range (2):
            img = pygame.image.load(f'image/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width()* scale), int(img.get_height()* scale)))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        #Takes the side of the image and creates a boundary box around it, to control position and collision
        self.rect.center= (x,y)

    

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.frame_index]
        #Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0
        
    def draw(self):
          screen.blit(self.image, self.rect)

player = Player(200, 300, 0.03)
#Coordinates where I want to draw the player


run = True
while run:
    clock.tick(FPS)
    
    draw_bg()
    
    player.update_animation()

    player.draw()
    
    for event in pygame.event.get():
    #Creating an interaction to quit the game
         if event.type == pygame.QUIT:
            run =  False

    pygame.display.update()

pygame.quit()
