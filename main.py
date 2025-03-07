import pygame
pygame.init()

WIDTH = 288
HEIGHT = 512

screen = pygame.display.set_mode((WIDTH, HEIGHT))
speed = 1

bg = pygame.image.load('./assets/sprites/background-day.png')

g1 = pygame.sprite.Sprite()
g1.image = pygame.image.load('./assets/sprites/base.png')
g1.rect = g1.image.get_rect()
g1.rect.x = 0
g1.rect.y = HEIGHT - g1.rect.height

g2 = pygame.sprite.Sprite()
g2.image = pygame.image.load('./assets/sprites/base.png')
g2.rect = g2.image.get_rect()
g2.rect.x = g2.rect.width
g2.rect.y = HEIGHT - g2.rect.height

ground_group = pygame.sprite.Group()
ground_group.add(g1)
ground_group.add(g2)


player = pygame.sprite.Sprite()
player.image = pygame.image.load('./assets/sprites/bluebird-midflap.png')
player.rect = player.image.get_rect()
player.rect.x = 40
player.rect.y = HEIGHT / 2

player_group = pygame.sprite.Group()
player_group.add(player)


def update_ground():
    g1.rect.x -= speed
    g2.rect.x -= speed

    if g1.rect.right < 0:
        g1.rect.left = g2.rect.right

    if g2.rect.right < 0:
        g2.rect.left = g1.rect.right

while True:

    # draw
    screen.blit(bg, (0, 0))
    player_group.draw(screen)
    ground_group.draw(screen)


    # update
    update_ground()


    # input
    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    pygame.display.update()