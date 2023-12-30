import random
import pygame
import os

pygame.init()
WIDTH = 1500
HEIGHT = 750
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
fontt = pygame.font.Font('asset/fonts/font.ttf', 30)
cover_button_load = pygame.image.load('asset/images/buttons/cover_button.png')
COVERBUTTON = pygame.transform.scale(cover_button_load, (290, 90))
COVERBUTTON_1 = pygame.image.load('asset/images/buttons/button_cover_2.png')

highscore = 0
HIGHSCORE = 0


# level = Level(level_0, SCREEN)


class Button:
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = fontt.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = fontt.render(self.text_input, True, [150, 158, 214])
        else:
            self.text = fontt.render(self.text_input, True, [20, 44, 205])


def minegame_screen_1():
    # game constants
    white = (255, 255, 255)
    blue_1 = (20, 44, 205)

    # game variables
    highscore = 0
    score = 0
    player_x = 50
    player_y = 580
    y_change = 0
    gravity = 1
    x_change = 0
    obstacacles = [1500, 1800, 1900]
    obstacacle_speed = 5
    ACTIVE = False

    pygame.display.set_caption("endless")
    background = pygame.image.load('asset/images/screens/backgroud_1.png')
    # backround = pygame.transform.scale(backround_load, (1500, 750))
    fps = 60
    font = pygame.font.Font('asset/fonts/font.ttf', 16)
    timer = pygame.time.Clock()
    player1_load = pygame.image.load('asset/images/player/henk_hover.png')
    player1 = pygame.transform.scale(player1_load, (45, 70))
    enemy0_load = pygame.image.load('asset/images/enemys/henk_boos_hover_0.png')
    enemy0 = pygame.transform.scale(enemy0_load, (45, 70))
    enemy1_load = pygame.image.load('asset/images/enemys/henk_boos_hover_1.png')
    enemy1 = pygame.transform.scale(enemy1_load, (45, 70))
    enemy2_load = pygame.image.load('asset/images/enemys/henk_boos_hover_2.png')
    enemy2 = pygame.transform.scale(enemy2_load, (45, 70))
    pygame.mixer.music.load('asset/muiziek/play_level_1.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    running = True
    while running:
        if os.path.exists('score.txt'):
            with open('score.txt', 'r') as file:
                high = int(file.read())
        timer.tick(fps)
        SCREEN.blit(background, (0, 0))
        score_text = font.render(f'Score: {score}', True, white, [98, 98, 35])
        SCREEN.blit(score_text, (100, 700))
        score_text = font.render(f'HighScore: {highscore}', True, white, [98, 98, 35])
        SCREEN.blit(score_text, (270, 700))
        score_text = font.render(f'Max HighScore: {high}', True, white, [98, 98, 35])
        SCREEN.blit(score_text, (500, 700))
        text = font.render('press SPACE to start', True, blue_1, [197, 237, 240])
        SCREEN.blit(text, (30, 390))
        text = font.render('press Q go to menu', True, blue_1, [197, 237, 240])
        SCREEN.blit(text, (30, 370))
        text = font.render('press Ece to quit', True, blue_1, [197, 237, 240])
        SCREEN.blit(text, (30, 350))
        player = SCREEN.blit(player1, (player_x, player_y))
        obstacacles0 = SCREEN.blit(enemy0, [obstacacles[0], 580, 20, 20])
        obstacacles1 = SCREEN.blit(enemy1, [obstacacles[1], 580, 20, 20])
        obstacacles2 = SCREEN.blit(enemy2, [obstacacles[2], 580, 20, 20])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not ACTIVE:
                if event.key == pygame.K_SPACE:
                    obstacacles = [1500, 1800, 2100]
                    player_x = 50
                    score = 0
                    ACTIVE = True
                if event.key == pygame.K_q:
                    menu()
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.KEYDOWN and ACTIVE:
                if event.key == pygame.K_SPACE and y_change == 0:
                    sound = pygame.mixer.Sound('asset/muiziek/jump.mp3')
                    sound.play()
                    y_change = 18
                if event.key == pygame.K_d:
                    x_change = 4
                if event.key == pygame.K_a:
                    x_change = -4
                if event.key == pygame.K_q:
                    menu()
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_LEFT:
                        x_change = 0

        for i in range(len(obstacacles)):
            if ACTIVE:
                obstacacles[i] -= obstacacle_speed
                if obstacacles[i] < 10:
                    obstacacles[i] = random.randint(1510, 1600)
                    score += 1
                if player.colliderect(obstacacles0) or player.colliderect(obstacacles1) or player.colliderect(
                        obstacacles2):
                    ACTIVE = False

        if 0 <= player_x <= 1300:
            player_x += x_change
        if player_x < 0:
            player_x = 0
        if player_x > 1300:
            player_x = 1300

        if y_change > 0 or player_y < 580:
            player_y -= y_change
            y_change -= gravity
            if player_y > 580:
                player_y = 580
            if player_y == 580 and y_change < 0:
                y_change = 0

        if score > highscore:
            highscore = score

        if highscore > high:
            high = high
            with open('score.txt', 'w') as file:
                file.write(str(highscore))
        if os.path.exists('score.txt'):
            with open('score.txt', 'r') as file:
                high = int(file.read())

        pygame.display.flip()
    pygame.quit()


def menu():
    # game constants
    pygame.display.set_caption('menu')
    fps = 60
    timer = pygame.time.Clock()
    background_1 = pygame.image.load('asset/images/screens/begin_screen_2.png')
    play_button_load = pygame.image.load('asset/images/buttons/play_buttton.png')
    play_button = pygame.transform.scale(play_button_load, (290, 90))
    cover_button_load = pygame.image.load('asset/images/buttons/cover_button.png')
    cover_button = pygame.transform.scale(cover_button_load, (290, 90))
    exit_button_load = pygame.image.load('asset/images/buttons/exit_button.png')
    exit_button = pygame.transform.scale(exit_button_load, (290, 90))
    options_button_load = pygame.image.load('asset/images/buttons/cover_button_3.png')
    options_button = pygame.transform.scale(options_button_load, (290, 90))
    tutorial_button_load = pygame.image.load('asset/images/buttons/cover_button_3.png')
    tutorial_button = pygame.transform.scale(tutorial_button_load, (290, 90))
    play = Button(cover_button, 685, 325, 'Play')
    options = Button(tutorial_button, 685, 205, '')
    exit = Button(cover_button, 685, 445, 'Exit')
    tutorial = Button(options_button, 685, 565, '')
    pygame.mixer.music.load('asset/muiziek/menu_screen.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    if os.path.exists('score.txt'):
        with open('score.txt', 'r') as file:
            high = int(file.read())

    running = True
    while running:
        timer.tick(fps)
        SCREEN.blit(background_1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.checkForInput(pygame.mouse.get_pos()):
                    minegame_screen_1()
                score_0 = fontt.render(f'HighScore: {high}', True, [98, 98, 35])
                if os.path.exists('score.txt'):
                    with open('score.txt', 'r') as file:
                        high = int(file.read())
                SCREEN.blit(score_0, (0, 0))

                if exit.checkForInput(pygame.mouse.get_pos()):
                    running = False
                if tutorial.checkForInput(pygame.mouse.get_pos()):
                    pass
        tutorial.update()
        options.update()
        play.update()
        exit.update()
        play.changeColor(pygame.mouse.get_pos())
        options.changeColor(pygame.mouse.get_pos())
        exit.changeColor(pygame.mouse.get_pos())
        tutorial.changeColor(pygame.mouse.get_pos())
        pygame.display.flip()
    pygame.quit()


menu()
