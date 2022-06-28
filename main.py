import pygame

from pygame.locals import(
    MOUSEBUTTONUP
)
#variables

linecolor = (0,0,0)
SURFACE_COLOR = (255,255,255)
RED = (255,0,0)
COLOR = (255,100,98)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,color, pygame.Rect(0,0,width,height))

        self.rect = self.image.get_rect()
        #clicked
    def drawClickedCross(self):
        pygame.draw.line(self.image, linecolor, (20, 20), (self.width - 20, self.height - 20), 20)
        pygame.draw.line(self.image, linecolor, (self.width - 20, 20), (20, self.height - 20), 20)

    def drawClickedCircle(self):
        pygame.draw.ellipse(self.image, linecolor, [10, 10,self.height-20, self.width-20], 10)


def drawline(n):
    for i in range(n):
        pygame.draw.line(screen, linecolor, (0, i * 200), (600, i * 200), 5)
        pygame.draw.line(screen, linecolor, (i * 200, 0), (i * 200, 600), 5)

pygame.init()



# Set up the drawing window
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("Testing")
screen.fill((255,255,255))



group = pygame.sprite.Group()

for i in range(3):
    for j in range(3):
        block = Sprite(SURFACE_COLOR, 200, 200)
        block.rect.x = i*200
        block.rect.y = j*200
        group.add(block)



clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
check = 0
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            for block in group:
                if block.rect.collidepoint(pos):
                    print("yes")
                    if check == 0:
                        block.drawClickedCross()
                        check = 1
                    else:
                        block.drawClickedCircle()
                        check = 0
    group.update()
    screen.fill(SURFACE_COLOR)
    group.draw(screen)
    drawline(4)





    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()


