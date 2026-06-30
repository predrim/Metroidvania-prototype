import pygame

WIDTH = 1280
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player = pygame.Rect(10, 10, 50, 50)
collide_right = False
collide_left = False

floor = pygame.Rect(100, HEIGHT - 100, WIDTH-200, 100)

on_floor = False

def jump(actor, max_jump_height, dt):
    if max_jump_height > 0:
        actor.y -= 1 * dt

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_floor:
                jump(player, 200, dt)
                on_floor = False

    can_move_right = True
    can_move_left = True

    if on_floor:
        player.bottom = floor.top
        gravity = 0
    else:
        gravity = 5

    # collision checks
    if player.bottom >= floor.top and player.top <= floor.top:
        on_floor = True
    elif player.bottom >= floor.top and player.left <= floor.right:
        can_move_left = False
    else: on_floor = False
    
    if player.bottom >= floor.top and player.top <= floor.top:
        on_floor = True
    elif player.bottom >= floor.top and player.right >= floor.left:
        can_move_right = False
    else: on_floor = False
    
    if player.right < floor.left or player.left > floor.right:
        on_floor = False

    player.y += gravity

    screen.fill("purple")

    pygame.draw.rect(screen, "yellow", player)
    pygame.draw.rect(screen, "green", floor)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 300 * dt
    if keys[pygame.K_s]:
        player.y += 300 * dt
    if keys[pygame.K_a] and can_move_left:
        player.x -= 300 * dt
    if keys[pygame.K_d] and can_move_right:
        player.x += 300 * dt

    pygame.display.update()

    print(can_move_left)

    dt = clock.tick(60)/1000

pygame.quit()