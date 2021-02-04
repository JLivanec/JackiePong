import pygame
pygame.init()



WIN_HEIGHT = 500
WIN_WIDTH = 1000

score = 0

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Jackie Pong")
font = pygame.font.Font(pygame.font.get_default_font(), 36)

# Paddle attributes
paddle_width = 8
paddle_height = 150
paddle_vel = 25
paddle_x = WIN_WIDTH - 50
paddle_y = (WIN_HEIGHT / 2) - (paddle_height / 2)
#--------------------

ball_x = 500
ball_y = 250
ball_radius = 5
ball_vel_x = 6
ball_vel_y = 5
ball_accel = 1

run = True
while run :
    pygame.time.delay(25)

    # QUIT
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    # Right paddle behavior
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_UP] and paddle_y > 0:
        paddle_y -= paddle_vel
    
    if keys[pygame.K_DOWN] and paddle_y < 500-paddle_height:
        paddle_y += paddle_vel
    #-----------------------------------------

    # Ball behavior
    # Strike paddle
    if ball_x == paddle_x and (ball_y >= paddle_y and ball_y <= paddle_y+paddle_height):
        score += 1
        ball_vel_x = -ball_vel_x
        # accelerate
        if ball_vel_x < 0:
            ball_vel_x -= ball_accel
        if ball_vel_x > 0:
            ball_vel_x += ball_accel
        if ball_vel_y < 0:
            ball_vel_y -= ball_accel
        if ball_vel_y > 0:
            ball_vel_y += ball_accel
    # Boundaries
    if ball_y <= ball_radius or ball_y >= WIN_HEIGHT-ball_radius :
        ball_vel_y = -ball_vel_y

    if ball_x <= ball_radius :
        ball_vel_x = -ball_vel_x

    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Redraw window
    win.fill((0,0,0))
    text_surface = font.render(str(score), False, (255, 255, 255))
    win.blit(text_surface, (WIN_WIDTH/2-18,0))
    pygame.draw.rect(win, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(win, (255, 255, 255), (ball_x, ball_y), ball_radius)
    pygame.display.update()

pygame.quit()