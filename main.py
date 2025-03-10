import pygame
pygame.init()
import random as rand
from pygame.locals import *

WIDTH = 288
HEIGHT = 512
GRAVITY = 0.5
FLAP_VELOCITY = -8.0
GAP = 150

class GameState:
    PLAYING = 1,
    GAME_OVER = 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
speed = 2.0

bg = pygame.image.load('./assets/sprites/background-day.png')
game_state = GameState.PLAYING

game_over_img = pygame.image.load('./assets/sprites/gameover.png')

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

# PIPES
top = pygame.sprite.Sprite()
top.image = pygame.image.load('./assets/sprites/pipe-green.png')
top.image = pygame.transform.flip(top.image, False, True)
top.rect = top.image.get_rect()
top.rect.top = rand.randint(-200, -50)
top.rect.x = 200

bot = pygame.sprite.Sprite()
bot.image = pygame.image.load('./assets/sprites/pipe-green.png')
bot.rect = bot.image.get_rect()
bot.rect.top = top.rect.bottom + GAP
bot.rect.x = 200

pipe_group = pygame.sprite.Group()
pipe_group.add(top)
pipe_group.add(bot)

# PLAYER
player = pygame.sprite.Sprite()
player.image = pygame.image.load('./assets/sprites/bluebird-midflap.png')
player.rect = player.image.get_rect()
player.rect.x = 40
player.rect.y = HEIGHT / 2
player.velocity = 0.0

player_group = pygame.sprite.Group()
player_group.add(player)


def update_ground():
    g1.rect.x -= speed
    g2.rect.x -= speed

    if g1.rect.right < 0:
        g1.rect.left = g2.rect.right

    if g2.rect.right < 0:
        g2.rect.left = g1.rect.right

def update_pipes():
    top.rect.x -= speed
    bot.rect.x -= speed

    if top.rect.right < 0:
        top.rect.left = WIDTH
        top.rect.y = rand.randint(-200, -50)
        bot.rect.left = WIDTH
        bot.rect.y = top.rect.bottom + GAP

def update_player():
    global game_state
    player.velocity += GRAVITY
    player.rect.y += player.velocity

    # collision between ground
    if player.rect.centery > g1.rect.top:
        print('dead')
        game_state = GameState.GAME_OVER



clock = pygame.time.Clock()

while True:

    clock.tick(60)

    # draw
    screen.blit(bg, (0, 0))
    pipe_group.draw(screen)
    ground_group.draw(screen)
    player_group.draw(screen)

    if game_state == GameState.GAME_OVER:
        screen.blit(game_over_img, (50, 50))

    # update
    update_ground()
    update_pipes()
    update_player()

    # input
    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

        if event.type == MOUSEBUTTONDOWN:
            player.velocity = FLAP_VELOCITY

    pygame.display.update()