import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_sound(name):
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)

    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл со звуком '{fullname}' не найден")
        sys.exit()
    sound = pygame.mixer.Sound(fullname)
    return sound


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
FPS = 50
maps = ["""WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWW          WWWW        WWWW        WW
WWWW          WWWW        WWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW      WWWWWWWW              WW      WW
WW      WWWWWWWW              WW      WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW  WWWWWW    WWWWWWWW                WW
WW  WWWWWW    WWWWWWWW                WW
WW      WW          WW  WW    WWWW    WW
WW      WW          WW  WW    WWWW    WW
WW      WW  WWWW    WW      WWWW    WWWW
WW      WW  WWWW    WW      WWWW    WWWW
WW            WW      WW    WW        WW
WW            WW      WW    WW        WW
WW    WW          WWWW        WW      WW
WW    WW          WWWW        WW      WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW          WW      WW      WW  WW    WW
WW@         WW      WW      WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WW  WW  WWWW          WWWW            WW
WW  WW  WWWW     R    WWWW            WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW          WW       WW         WW    WW
WW          WW       WW         WW    WW
WW      WW        WW        WW        WW
WW      WW        WW        WW        WW
WW    WW      WW        WW      WW    WW
WW    WW      WW        WW      WW    WW
WW        WW            WW      WW     F
WW        WW            WW      WW     F
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW""",
        """WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWW          WWWW        WWWW        WW
WWWW          WWWW        WWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW      WWWWWWWW              WW      WW
WW      WWWWWWWW              WW      WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW  WWWWWW    WWWWWWWW                WW
WW  WWWWWW    WWWWWWWW                WW
WW      WW          WW  WW    WWWW    WW
WW      WW          WW  WW    WWWW    WW
WW      WW  WWWW    WW      WWWW    WWWW
WW      WW  WWWW    WW      WWWW    WWWW
WW            WW      WW    WW        WW
WW            WW      WW    WW        WW
WW    WW          WWWW        WW      WW
WW    WW          WWWW        WW      WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW          WW      WW      WW  WW    WW
WW@         WW      WW      WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WW  WW  WWWW          WWWW            WW
WW  WW  WWWW          WWWW            WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW          WW       WW         WW    WW
WW          WW       WW         WW    WW
WW      WW        WW        WW        WW
WW      WW        WW        WW        WW
WW    WW      WW        WW      WW    WW
WW    WW      WW        WW      WW    WW
WW        WW            WW      WW     F
WW        WW            WW      WW     F
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW""",
        """WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWW          WWWW        WWWW        WW
WWWW          WWWW        WWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW      WWWWWWWW              WW      WW
WW      WWWWWWWW              WW      WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW  WWWWWW    WWWWWWWW                WW
WW  WWWWWW    WWWWWWWW                WW
WW      WW          WW  WW    WWWW    WW
WW      WW          WW  WW    WWWW    WW
WW      WW  WWWW    WW      WWWW    WWWW
WW      WW  WWWW    WW      WWWW    WWWW
WW            WW      WW    WW        WW
WW            WW      WW    WW        WW
WW    WW          WWWW        WW      WW
WW    WW          WWWW        WW      WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW@         WW      WW      WW  WW    WW
WW          WW      WW      WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WW  WW  WWWW          WWWW            WW
WW  WW  WWWW          WWWW            WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW          WW       WW         WW    WW
WW          WW       WW         WW    WW
WW      WW        WW        WW        WW
WW      WW        WW        WW        WW
WW    WW      WW        WW      WW    WW
WW    WW      WW        WW      WW    WW
WW        WW            WW      WW      
WW        WW            WW      WW      
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW""",
        """WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWW          WWWW        WWWW        WW
WWWW          WWWW        WWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW    WWWW          WWWWWWWWWW        WW
WW      WWWWWWWW              WW      WW
WW      WWWWWWWW              WW      WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW      WW    WWWWWWWW    WWWWWWWW    WW
WW  WWWWWW    WWWWWWWW                WW
WW  WWWWWW    WWWWWWWW                WW
WW      WW          WW  WW    WWWW    WW
WW      WW          WW  WW    WWWW    WW
WW      WW  WWWW    WW      WWWW    WWWW
WW      WW  WWWW    WW      WWWW    WWWW
WW            WW      WW    WW        WW
WW            WW      WW    WW        WW
WW    WW          WWWW        WW      WW
WW    WW          WWWW        WW      WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW    WW  WWWWWW  WWWWWW  WW  WW  WW  WW
WW          WW      WW      WW  WW    WW
WW@         WW      WW      WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WWWWWW      WW        WW    WW  WW    WW
WW  WW  WWWW          WWWW            WW
WW  WW  WWWW          WWWW            WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW  WW    WW  WWWWWWWW      WWWWWW    WW
WW          WW       WW         WW    WW
WW          WW       WW         WW    WW
WW      WW        WW        WW        WW
WW      WW        WW        WW        WW
WW    WW      WW        WW      WW    WW
WW    WW      WW        WW      WW    WW
WW        WW            WW      WW     F
WW        WW        L   WW      WW     F
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"""]
size = WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode(size)
sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()

tile_images = {
    'wall': pygame.transform.scale(load_image('break.jpg'), (18, 10)),
    'empty': pygame.transform.scale(load_image('download.png'), (18, 10)),
    'rutile': pygame.transform.scale(load_image('rutile.jpg'), (18, 10)),
    'lamp': pygame.transform.scale(load_image('lamp.jpg'), (18, 10))
}
player_image = pygame.transform.scale(load_image('gg.jpg', -1), (18, 10))

tile_width, tile_height = 18, 10
f = open('data/saves.txt', encoding='utf8')
current_level = int(f.read())
f.close()


class Sprite(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Player(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)
        self.is_paused = False

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(tile_width * self.pos[0] + 5,
                                               tile_height * self.pos[1] + 1)
        pygame.time.set_timer(30, 500)

    def switch_pause(self):
        self.is_paused = not self.is_paused


class Tile(Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.abs_pos = (self.rect.x, self.rect.y)


class Finish(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images['empty']
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.abs_pos = (self.rect.x, self.rect.y)


class Rutile(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images['rutile']
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.abs_pos = (self.rect.x, self.rect.y)


lamp = False


def start_screen():
    global lamp
    intro_text = ["Главная страница",
                  " ",
                  "Продолжить"]

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 125
    intro_rect_x = [65, 100, 90]
    for line in range(len(intro_text)):
        string_rendered = font.render(intro_text[line], 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = intro_rect_x[line]
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        mouse_click = load_sound("mouse_click.mp3")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    215 > event.pos[0] > 90 and 215 > event.pos[1] > 195:
                return  # продолжить
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    410 > event.pos[0] > 390 and 205 > event.pos[1] > 175:
                if current_level == 16:
                    lamp = True
                    return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click.play()
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, ' ')), level_map))


def generate_level(level, a=None, b=None):
    new_player, x, y, rutile, lampochka = None, None, None, None, None
    finishes = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ' ':
                Tile('empty', x, y)
            elif level[y][x] == 'W':
                Tile('wall', x, y)
            elif level[y][x] == 'F':
                finish = Finish(x, y)
                finishes.append(finish)
            elif level[y][x] == '@':
                if a is not None and b is not None:
                    Tile('empty', a, b)
                    new_player = Player(a, b)
                    level[a][b] = " "
                else:
                    Tile('empty', x, y)
                    new_player = Player(x, y)
            elif level[y][x] == 'R':
                rutile = Rutile(x, y)
            elif level[y][x] == 'L':
                lampochka = Tile('lamp', x, y)
    return new_player, x, y, finishes, rutile, lampochka


def move(hero, movement):
    x, y = hero.pos
    if movement == "up":
        if y > 0 and level_map[y - 1][x] == " ":
            hero.move(x, y - 1)
    elif movement == "down":
        if y < max_y - 1 and level_map[y + 1][x] == " ":
            hero.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level_map[y][x - 1] == " ":
            hero.move(x - 1, y)
    elif movement == "right":
        if x < max_x - 1 and level_map[y][x + 1] == " ":
            hero.move(x + 1, y)


def map_change(indx):
    f = open('data/map.map', 'w')
    f.write(maps[indx])
    f.close()


level_map = load_level("map.map")
hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
pygame.mixer.music.load("data/sonata.mp3")
pygame.mixer.music.play(loops=-1, start=6.5)
start_screen()
running = True
clock = pygame.time.Clock()
move_right = False
move_left = False
move_down = False
move_up = False


def one_third_fifth_seventh_nineteenth_levels():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    if current_level != 1:
        level_map = load_level("map.map")
        hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    FPS = 0
    if current_level == 1 or current_level == 5 or current_level == 19:
        FPS = 20
    elif current_level == 3:
        FPS = 5
    elif current_level == 7:
        FPS = 200
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if current_level == 1 or current_level == 3 or current_level == 7 or current_level == 19:
            if move_right:
                move(hero, "right")
            if move_left:
                move(hero, "left")
            if move_up:
                move(hero, "up")
            if move_down:
                move(hero, "down")
        elif current_level == 5:
            if move_right:
                move(hero, "down")
            if move_left:
                move(hero, "up")
            if move_up:
                move(hero, "right")
            if move_down:
                move(hero, "left")

        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                if current_level != 19:
                    hero_group.remove(hero)
                    if current_level == 1:
                        map_change(0)
                    if current_level == 7:
                        map_change(3)
                    current_level += 1
                    print(current_level)
                    return
                else:
                    end_screen()
                    return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def second_level():
    global running, move_up, move_left, move_down, move_right, current_level
    FPS = 20
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    r = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        if rutile and hero.rect.colliderect(rutile.rect):
            r = True
            map_change(1)
            x, y = hero.pos
            level_map = load_level("map.map")
            hero_group.remove(hero)
            hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
        for finish in finishes:
            if hero.rect.colliderect(finish.rect) and r:
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def fourth_tenth_level():
    FPS = 20
    global running, move_up, move_left, move_down, move_right, current_level
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if current_level == 4:
                        for i in range(10):
                            move(hero, 'left')
                    elif current_level == 10:
                        for i in range(10):
                            move(hero, 'right')
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    if current_level == 4:
                        for i in range(10):
                            move(hero, 'left')
                    elif current_level == 10:
                        for i in range(10):
                            move(hero, 'right')
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    if current_level == 4:
                        for i in range(10):
                            move(hero, 'left')
                    elif current_level == 10:
                        for i in range(10):
                            move(hero, 'right')
                    move_down = False
                elif event.key == pygame.K_UP:
                    if current_level == 4:
                        for i in range(10):
                            move(hero, 'left')
                    elif current_level == 10:
                        for i in range(10):
                            move(hero, 'right')
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def sixth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    if current_level != 1:
        level_map = load_level("map.map")
        hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                elif event.key == pygame.K_d:
                    move_right = True
                elif event.key == pygame.K_s:
                    move_down = True
                elif event.key == pygame.K_w:
                    move_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                elif event.key == pygame.K_d:
                    move_right = False
                elif event.key == pygame.K_s:
                    move_down = False
                elif event.key == pygame.K_w:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def eighteenth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    FPS = 20
    minimized = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
            elif event.type == pygame.WINDOWMINIMIZED:
                minimized = True
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect) and minimized:
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def seventeenth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    FPS = 20
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero_group.remove(hero)
                current_level += 1
                map_change(1)
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def sixteenth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    if current_level != 1:
        level_map = load_level("map.map")
        hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    FPS = 20
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect) and lamp:
                hero_group.remove(hero)
                current_level += 1
                map_change(2)
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def fourteenth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    FPS = 20
    menu_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    menu_count += 1
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect) and menu_count == 3:
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def eighth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    FPS = 20
    x = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        if hero.rect.colliderect(lampochka.rect):
            x = True
        for finish in finishes:
            if hero.rect.colliderect(finish.rect) and x:
                hero_group.remove(hero)
                current_level += 1
                map_change(1)
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def end_screen():
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    text_coord = 125
    intro_rect_x = [250, 100]

    if current_level == 19:
        text = ["Happy End",
                f"Пройденные уровни {current_level}/19. Девушка смогла очнуться."]
        screen.fill(pygame.Color('white'))
        for line in range(len(text)):
            string_rendered = font.render(text[line], 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = intro_rect_x[line]
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif current_level < 19:
        text = ["Bad End",
                f"Пройденные уровни {current_level}/19. Девушка еще в воспоминаниях."]
        screen.fill(pygame.Color('black'))
        for line in range(len(text)):
            string_rendered = font.render(text[line], 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = intro_rect_x[line]
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    else:
        text = ["Bad End",
                f"Почему? Это не должно быть так."]
        screen.fill(pygame.Color('black'))
        for line in range(len(text)):
            string_rendered = font.render(text[line], 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = intro_rect_x[line]
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    while True:
        mouse_click = load_sound("mouse_click.mp3")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click.play()
        pygame.display.flip()
        clock.tick(FPS)


def eleventh_level():
    global tile_images
    tile_images = {
        'wall': pygame.transform.scale(load_image('break_black.jpg'), (18, 10)),
        'empty': pygame.transform.scale(load_image('download.png'), (18, 10)),
        'rutile': pygame.transform.scale(load_image('rutile.jpg'), (18, 10)),
        'lamp': pygame.transform.scale(load_image('lamp.jpg'), (18, 10))
    }
    global running, move_up, move_left, move_down, move_right, current_level
    FPS = 20
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def twelfth_level():
    global player_image
    player_image = pygame.transform.scale(load_image('break_black.jpg'), (18, 10))
    global running, move_up, move_left, move_down, move_right, current_level
    FPS = 20
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def thirteenth_level():
    global player_image, tile_images
    tile_images = {
        'wall': pygame.transform.scale(load_image('break_black.jpg'), (18, 10)),
        'empty': pygame.transform.scale(load_image('download.png'), (18, 10)),
        'rutile': pygame.transform.scale(load_image('rutile.jpg'), (18, 10)),
        'lamp': pygame.transform.scale(load_image('lamp.jpg'), (18, 10))
    }
    player_image = pygame.transform.scale(load_image('break_black.jpg', -1), (18, 10))
    global running, move_up, move_left, move_down, move_right, current_level
    FPS = 20
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_UP:
                    move_up = True
                if event.type == pygame.K_p:
                    hero.switch_pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def ninth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    if current_level != 1:
        level_map = load_level("map.map")
        hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    move_left = True
                elif event.key == pygame.K_f:
                    move_right = True
                elif event.key == pygame.K_v:
                    move_down = True
                elif event.key == pygame.K_m:
                    move_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_i:
                    move_left = False
                elif event.key == pygame.K_f:
                    move_right = False
                elif event.key == pygame.K_v:
                    move_down = False
                elif event.key == pygame.K_m:
                    move_up = False
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                map_change(0)
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def fifteenth_level():
    global running, move_up, move_left, move_down, move_right, current_level, finishes, hero
    if current_level != 1:
        level_map = load_level("map.map")
        hero, max_x, max_y, finishes, rutile, lampochka = generate_level(level_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('data/saves.txt', 'w')
                f.write(str(current_level))
                f.close()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero_group.remove(hero)
                    current_level += 1
                    return
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


if current_level == 1:
    one_third_fifth_seventh_nineteenth_levels()
if current_level == 2:
    second_level()
if current_level == 3:
    one_third_fifth_seventh_nineteenth_levels()
if current_level == 4:
    fourth_tenth_level()
if current_level == 5:
    one_third_fifth_seventh_nineteenth_levels()
if current_level == 6:
    sixth_level()
if current_level == 7:
    one_third_fifth_seventh_nineteenth_levels()
if current_level == 8:
    eighth_level()
if current_level == 9:
    ninth_level()
if current_level == 10:
    fourth_tenth_level()
if current_level == 11:
    eleventh_level()
if current_level == 12:
    twelfth_level()
if current_level == 13:
    thirteenth_level()
if current_level == 14:
    fourteenth_level()
if current_level == 15:
    fifteenth_level()
if current_level == 16:
    sixteenth_level()
if current_level == 17:
    seventeenth_level()
if current_level == 18:
    eighteenth_level()
if current_level == 19:
    one_third_fifth_seventh_nineteenth_levels()
end_screen()
