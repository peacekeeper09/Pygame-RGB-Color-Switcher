import pygame
pygame.init()

interval = int(input("Enter the color switch interval (in seconds): ")) * 1000

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

clock = pygame.time.Clock()

color_index = 0

animation_running = True

done = False
while not done:

    screen.fill(colors[color_index])


    pygame.display.flip()

    color_index = (color_index + 1) % len(colors)

    clock.tick(1000 / interval)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Toggle the animation state
                animation_running = not animation_running


    while not animation_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    animation_running = not animation_running

pygame.quit()
