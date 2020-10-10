import pygame
import random
if __name__ == '__main__':
    pygame.init()
    # dimensions
    length = 500
    breadth = 500
    # surface
    screen = pygame.display.set_mode((length, breadth))
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen.fill(white)
    pygame.display.set_caption("Snake Game")
    pygame.display.update()
    # scoring
    score: int = 0
    game_over: bool = False
    # position in surface
    x_axis = 250
    y_axis = 250
    changed_x_axis = 0
    changed_y_axis = 0
    food_x = random.randrange(10, length-10, 10)
    food_y = random.randrange(10, breadth-10, 10)
    snake_l = []
    snake_length = 1
    U = 0
    D = 0
    L = 0
    R = 0
    # movement time
    clock = pygame.time.Clock()
    # text on surface
    font = pygame.font.SysFont('arial', 15)
    # snake loop
    while not game_over:
        for random_event in pygame.event.get():
            if random_event.type == pygame.QUIT:
                game_over: bool = True
            if random_event.type == pygame.KEYDOWN:
                if random_event.key == pygame.K_LEFT and L == 0:
                    L = 0
                    U = 0
                    D = 0
                    R = 1
                    changed_x_axis = -10
                    changed_y_axis = 0
                elif random_event.key == pygame.K_RIGHT and R == 0:
                    changed_x_axis = 10
                    changed_y_axis = 0
                    R = 0
                    U = 0
                    D = 0
                    L = 1
                elif random_event.key == pygame.K_UP and U == 0:
                    changed_y_axis = -10
                    changed_x_axis = 0
                    U = 0
                    D = 1
                    L = 0
                    R = 0
                elif random_event.key == pygame.K_DOWN and D == 0:
                    changed_y_axis = 10
                    changed_x_axis = 0
                    D = 0
                    U = 1
                    L = 0
                    R = 0
        x_axis += changed_x_axis
        y_axis += changed_y_axis
        if y_axis == 0 or y_axis == 500 or x_axis == 0 or x_axis == 500:
            game_over: bool = True
        # repeat
        screen.fill(white)
        snake_h = [x_axis, y_axis]
        snake_l.append(snake_h)
        if len(snake_l) > snake_length:
            del snake_l[0]
        for x in snake_l[:-1]:
            if x == snake_h and snake_length > 2:
                game_over: bool = True
        pygame.draw.rect(screen, red, [food_x, food_y, 10, 10])
        text = font.render("Your Score=" + str(score), True, blue)
        textRect = text.get_rect()
        textRect.center = (length // 2, 10)
        screen.blit(text, textRect)
        for x in snake_l:
            pygame.draw.rect(screen, blue, [x[0], x[1], 10, 10])
        pygame.display.update()
        if x_axis == food_x and y_axis == food_y:
            food_x = random.randrange(10, length - 10, 10)
            food_y = random.randrange(10, breadth - 10, 10)
            score += 10
            snake_length += 1
        clock.tick(10)
    pygame.quit()
    quit()
