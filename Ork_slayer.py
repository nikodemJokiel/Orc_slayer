import sys
import pygame
from random import randint

# do testowania mechanik polecam w linijce 706 zmienić 'money += 25' na 'money += 50' lub nawet 'money += 100'
# dla wyzwania polecam w linijce 706  zmienić 'money += 25' na 'money += 15' lub nawet 'money += 10'

pygame.init()
window = pygame.display.set_mode((1280, 720))

music = pygame.mixer.music.load('sound/music.wav') 

pygame.mixer.music.play(-1)

axe_sound = pygame.mixer.Sound("sound/axe.ogg") 

axe_sound2 = pygame.mixer.Sound("sound/axe2.ogg") 

axe_sound3 = pygame.mixer.Sound("sound/axe3.wav")

hit_sound = pygame.mixer.Sound("sound/bite.wav")

level = 0

pixel_font = pygame.font.Font("assets/depixelhalbfett.woff", 60)

pixel_font_thin = pygame.font.Font("assets/depixelbreit.woff", 20)

pixel_font2 = pygame.font.Font("assets/depixelhalbfett.woff", 30)

def rotation(surface, angle, weapon_cord_x, weapon_cord_y):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(weapon_cord_x,weapon_cord_y))
    return rotated_surface, rotated_rect

class Player:
    def __init__(self):

        self.image = pygame.image.load("assets/player1.png")

        self.height = self.image.get_height()
        self.width = self.image.get_width()

        self.x_cord = 640
        self.y_cord = 360

        self.rect = self.image.get_rect()
        self.rect.center = [self.x_cord, self.y_cord]



    def tick(self, keys, speed, weapon_size ,draw_weapon, animation_status):

        if draw_weapon and keys[pygame.K_a]:
            if weapon_size == 1:
                self.image = pygame.image.load("assets/player1_attackl.png")
            if weapon_size == 2:
                self.image = pygame.image.load("assets/player2_attackl.png")
            if weapon_size == 3:
                self.image = pygame.image.load("assets/player3_attackl.png")
            if weapon_size == 4:
                self.image = pygame.image.load("assets/player4_attackl.png")

        elif draw_weapon:
            if weapon_size == 1:
                self.image = pygame.image.load("assets/player1_attack.png")
            if weapon_size == 2:
                self.image = pygame.image.load("assets/player2_attack.png")
            if weapon_size == 3:
                self.image = pygame.image.load("assets/player3_attack.png")
            if weapon_size == 4:
                self.image = pygame.image.load("assets/player4_attack.png")

        elif animation_status and keys[pygame.K_a]:
            if weapon_size == 1:
                self.image = pygame.image.load("assets/player1_walkl.png")
            if weapon_size == 2:
                self.image = pygame.image.load("assets/player2_walkl.png")
            if weapon_size == 3:
                self.image = pygame.image.load("assets/player3_walkl.png")
            if weapon_size == 4:
                self.image = pygame.image.load("assets/player4_walkl.png")

        elif animation_status:
            if weapon_size == 1:
                self.image = pygame.image.load("assets/player1_walk.png")
            if weapon_size == 2:
                self.image = pygame.image.load("assets/player2_walk.png")
            if weapon_size == 3:
                self.image = pygame.image.load("assets/player3_walk.png")
            if weapon_size == 4:
                self.image = pygame.image.load("assets/player4_walk.png")

        elif keys[pygame.K_a]:
            if weapon_size == 1:
                self.image = pygame.image.load("assets/player1l.png")
            if weapon_size == 2:
                self.image = pygame.image.load("assets/player2l.png")
            if weapon_size == 3:
                self.image = pygame.image.load("assets/player3l.png")
            if weapon_size == 4:
                self.image = pygame.image.load("assets/player4l.png")

        else:
            if weapon_size == 1:
                self.image = pygame.image.load("assets/player1.png")
            if weapon_size == 2:
                self.image = pygame.image.load("assets/player2.png")
            if weapon_size == 3:
                self.image = pygame.image.load("assets/player3.png")
            if weapon_size == 4:
                self.image = pygame.image.load("assets/player4.png")

        if keys[pygame.K_w] and self.y_cord >= 40:
            self.y_cord -= speed

        if keys[pygame.K_a] and self.x_cord >= 40:
            self.x_cord -= speed

        if keys[pygame.K_s] and self.y_cord <= 720 - 40:
            self.y_cord += speed

        if keys[pygame.K_d] and self.x_cord <= 1280 - 40:
            self.x_cord += speed

        self.rect = self.image.get_rect()
        self.rect.center = [self.x_cord, self.y_cord]

    def player_cord_x(self):
        return self.x_cord

    def player_cord_y(self):
        return self.y_cord

    def draw(self):
        window.blit(self.image, self.rect)
        
class Ork:
    def __init__(self):
        corner = randint(1,4)
        if corner == 1:
            self.x_cord = randint(0, 1280)

            self.y_cord = randint(-200, 240)

        elif corner == 2:
            self.x_cord = randint(-200, 426)

            self.y_cord = randint(0, 720)

        elif corner == 3:
            self.x_cord = randint(0, 1280)

            self.y_cord = randint(480, 920)

        elif corner == 4:
            self.x_cord = randint(825, 1480)

            self.y_cord = randint(0, 720)
        
        self.image= pygame.image.load("assets/ork.png")
        
        self.width = self.image.get_width()
        
        self.height = self.image.get_height()
        
        self.rect = self.image.get_rect()
        self.rect.center = [self.x_cord, self.y_cord]


    def tick(self, player_x_cord, player_y_cord, ork_speed, animation_status, ork_dead):

        if ork_dead:
            self.image = pygame.image.load("assets/ork_dead1.png")

        elif animation_status:
            if player_y_cord < self.y_cord:
                self.y_cord -= ork_speed
                self.image = pygame.image.load("assets/ork.png")

            if player_y_cord > self.y_cord:
                self.y_cord += ork_speed
                self.image = pygame.image.load("assets/orkl.png")

            if player_x_cord < self.x_cord:
                self.x_cord -= ork_speed
                self.image = pygame.image.load("assets/orkl.png")

            if player_x_cord > self.x_cord:
                self.x_cord += ork_speed
                self.image = pygame.image.load("assets/ork.png")

        elif animation_status == False:
            if player_y_cord < self.y_cord:
                self.y_cord -= ork_speed
                self.image = pygame.image.load("assets/ork_walk.png")

            if player_y_cord > self.y_cord:
                self.y_cord += ork_speed
                self.image = pygame.image.load("assets/ork_walkl.png")

            if player_x_cord < self.x_cord:
                self.x_cord -= ork_speed
                self.image = pygame.image.load("assets/ork_walkl.png")

            if player_x_cord > self.x_cord:
                self.x_cord += ork_speed
                self.image = pygame.image.load("assets/ork_walk.png")

        self.rect = self.image.get_rect()
        self.rect.center = [self.x_cord, self.y_cord]

    def draw(self):
        window.blit(self.image,self.rect)
        
class Weapon:
    
    def __init__(self):

        self.image = pygame.image.load("assets/axe1_range.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_cord = 640
        self.y_cord = 360

    def tick(self, keys, speed, weapon_size):

        if weapon_size == 1:
            self.image = pygame.image.load("assets/axe1_range.png")
        if weapon_size == 2:
            self.image = pygame.image.load("assets/axe2_range.png")
        if weapon_size == 3:
            self.image = pygame.image.load("assets/axe3_range.png")
        if weapon_size == 4:
            self.image = pygame.image.load("assets/axe4_range.png")


        if keys[pygame.K_w] and self.y_cord >= 0 + 80/2:
            self.y_cord -= speed

        if keys[pygame.K_a] and self.x_cord >= 0 + 80/2:
            self.x_cord -= speed

        if keys[pygame.K_s] and self.y_cord <= 720 - 80/2:
            self.y_cord += speed

        if keys[pygame.K_d] and self.x_cord <= 1280 - 80/2:
            self.x_cord += speed

        self.rect = self.image.get_rect()
        self.rect.center = [self.x_cord, self.y_cord]

    def weapon_cord_x(self):
        return self.x_cord

    def weapon_cord_y(self):
        return self.y_cord

    def draw2(self):
        window.blit(self.image, self.rect)

    def draw3(self, weapon_rotated, weapon_rect_rotated):
        window.blit(weapon_rotated, weapon_rect_rotated)


class Shop_size:
    def __init__(self):

        self.image = pygame.image.load("assets/size_shop.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_cord = 0
        self.y_cord = 20

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x_cord, self.y_cord]

    def draw(self, shop_alpha):
        self.image.set_alpha(shop_alpha)
        window.blit(self.image, self.rect)

class Shop_cooldown:
    def __init__(self):

        self.image = pygame.image.load("assets/cooldown_shop.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_cord = 0
        self.y_cord = 230

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x_cord, self.y_cord]

    def draw(self, shop_alpha):
        self.image.set_alpha(shop_alpha)
        window.blit(self.image, self.rect)


class Shop_duration:
    def __init__(self):

        self.image = pygame.image.load("assets/duration_shop.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_cord = 0
        self.y_cord = 440

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x_cord, self.y_cord]

    def draw(self, shop_alpha):
        self.image.set_alpha(shop_alpha)
        window.blit(self.image, self.rect)

class Shop_speed:
    def __init__(self):

        self.image = pygame.image.load("assets/speed_shop.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_cord = 1280
        self.y_cord = 20

        self.rect = self.image.get_rect()
        self.rect.topright = [self.x_cord, self.y_cord]

    def draw(self, shop_alpha):
        self.image.set_alpha(shop_alpha)
        window.blit(self.image, self.rect)

class Shop_health:
    def __init__(self):

        self.image = pygame.image.load("assets/health_shop.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_cord = 1280
        self.y_cord = 230

        self.rect = self.image.get_rect()
        self.rect.topright = [self.x_cord, self.y_cord]

    def draw(self, shop_alpha):
        self.image.set_alpha(shop_alpha)
        window.blit(self.image, self.rect)

class Health_indicator:
    def __init__(self):
        self.image = pygame.image.load("assets/hearts3.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_cord = 1280
        self.y_cord = 680

        self.image.set_alpha(200)

        self.rect = self.image.get_rect()
        self.rect.bottomright = [self.x_cord, self.y_cord]

    def tick(self, health):

        if health == 3:
            self.image = pygame.image.load("assets/hearts3.png")
        if health == 2:
            self.image = pygame.image.load("assets/hearts2.png")
        if health == 1:
            self.image = pygame.image.load("assets/hearts1.png")
        if health == 0:
            self.image = pygame.image.load("assets/hearts0.png")

        self.rect = self.image.get_rect()
        self.rect.bottomright = [self.x_cord, self.y_cord]

        self.image.set_alpha(200)

    def draw(self):
        window.blit(self.image, self.rect)

def main(pixel_font, pixel_font_thin,level):
    run = True

    shop_size = Shop_size()
    shop_cooldown = Shop_cooldown()
    shop_duration = Shop_duration()
    shop_speed = Shop_speed()
    shop_health = Shop_health()

    shop_alpha = 255
    wave_info_alpha = 255
    alpha_direction = bool

    money = 0

    shop_size_price = 200
    shop_duration_price = 200
    shop_cooldown_price = 200
    shop_speed_price = 200
    shop_health_price = 200

    shop_size_price_bonus = 100
    shop_duration_price_bonus = 100
    shop_cooldown_price_bonus = 100
    shop_speed_price_bonus = 100
    shop_health_price_bonus = 0

    weapon_size = 1
    weapon = Weapon()
    weapon_clock = 3

    weapon_duration = 1
    weapon_cooldown_reduction = 6
    speed = 4
    health = 3

    ork_speed = 3

    player = Player()

    Orks = []
    wave = True
    ork_dead = False

    wave_pointer = bool

    corner = randint(1, 4)

    level_count = 0

    plik = open("best_score.txt", 'r').read()
    best_level = (int(plik))

    print(best_level)

    health_indicator = Health_indicator()

    angle = 0

    animation_clock = 0
    animation_clock_ork = 0

    animation_status = bool
    animation_status_ork = bool

    background = pygame.image.load("assets/background.png")

    while run:
        weapon_clock += pygame.time.Clock().tick(60) / 100

        pygame.time.Clock().tick(120)

        weapon_cooldown = weapon_duration + weapon_cooldown_reduction

        animation_clock_ork += 1
        if animation_clock_ork > 15-2*ork_speed:
            animation_status_ork = True
        if animation_clock_ork < 15-2*ork_speed:
            animation_status_ork = False
        if animation_clock_ork >= 30-4*ork_speed:
            animation_clock_ork = 0

        animation_clock += 1
        if animation_clock > 22 - 2 * speed:
            animation_status = True
        if animation_clock < 22 - 2 * speed:
            animation_status = False
        if animation_clock >= 44 - 4 * speed:
            animation_clock = 0

        if weapon_clock < weapon_cooldown:
            cooldown_ready = weapon_clock*40
        else:
            cooldown_ready = weapon_cooldown*40

        if weapon_size == 1:
            weapon_animation = pygame.image.load("assets/axe1.png")
        if weapon_size == 2:
            weapon_animation = pygame.image.load("assets/axe2.png")
        if weapon_size == 3:
            weapon_animation = pygame.image.load("assets/axe3.png")
        if weapon_size == 4:
            weapon_animation = pygame.image.load("assets/axe4.png")

        cooldown_indicator_bg = pygame.Surface([weapon_cooldown*40, 30])
        cooldown_indicator_bg.set_alpha(100)
        cooldown_indicator_bg.fill((150, 150, 150))
        cooldown_indicator_bg_rect = cooldown_indicator_bg.get_rect(bottomright=(1280, 720))

        cooldown_indicator = pygame.Surface([cooldown_ready, 30])
        cooldown_indicator.set_alpha(100)

        cooldown_indicator_rect = cooldown_indicator.get_rect(bottomright=(1280, 720))

        duration_indicator = pygame.Surface([5, 30])
        duration_indicator.set_alpha(180)
        duration_indicator.fill((0, 255, 0))
        duration_indicator_rect = duration_indicator.get_rect(bottomleft=(1280 - weapon_duration*40, 720))

        cooldown_indicator2 = pygame.Surface([5, 30])
        cooldown_indicator2.set_alpha(180)
        cooldown_indicator2.fill((255, 0, 0))
        cooldown_indicator2_rect = cooldown_indicator2.get_rect(bottomleft=(1280 - weapon_cooldown*40, 720))

        if cooldown_ready/40 < weapon_cooldown:
            cooldown_indicator.fill((255, 255, 255))
        if cooldown_ready/40 >= weapon_cooldown:
            duration_indicator.set_alpha(0)
            cooldown_indicator2.set_alpha(0)
            cooldown_indicator.fill((0, 255, 0))

        keys = pygame.key.get_pressed()
        weapon_cord_x = weapon.weapon_cord_x()
        weapon_cord_y = weapon.weapon_cord_y()
        draw_weapon = bool
        if weapon_clock >= weapon_duration:
            draw_weapon = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if Orks == [] and event.key == pygame.K_x:
                    wave_pointer = True
                    wave = True
                    level += 1
                    level_count += 1

                if event.key == pygame.K_SPACE and weapon_clock >= weapon_cooldown:
                    draw_weapon = True
                    weapon_clock = 0
                    if weapon_duration == 1:
                        
                        axe_sound.play()
                        
                    if weapon_duration == 3: 

                        axe_sound3.play(1)

                        axe_sound.play()

                    elif weapon_duration == 5: 

                        axe_sound2.play()
                        
                        axe_sound3.play(2)
                        
                        axe_sound.play() 

                    elif weapon_duration == 7: 

                        axe_sound3.play(3)
                        axe_sound.play(1)

                    elif weapon_duration == 9: 

                        axe_sound2.play(1)

                        axe_sound3.play(4)

                        axe_sound.play(2)

                if event.key == pygame.K_b and player.rect.colliderect(shop_size.rect) and money >= shop_size_price and weapon_size < 4 and wave_pointer == False:
                    money -= shop_size_price
                    shop_size_price += shop_size_price + shop_size_price_bonus
                    weapon_size += 1
                    shop_size_price_bonus += 100

                if event.key == pygame.K_b and player.rect.colliderect(shop_cooldown.rect) and money >= shop_cooldown_price and weapon_cooldown_reduction > 2 and wave_pointer == False:
                    money -= shop_cooldown_price
                    shop_cooldown_price += shop_cooldown_price + shop_cooldown_price_bonus
                    weapon_cooldown_reduction -= 1
                    shop_cooldown_price_bonus += 100

                if event.key == pygame.K_b and player.rect.colliderect(shop_duration.rect) and money >= shop_duration_price and weapon_duration < 9 and wave_pointer == False:
                    money -= shop_duration_price
                    shop_duration_price += shop_duration_price + shop_duration_price_bonus
                    weapon_duration += 2
                    shop_duration_price_bonus += 100

                if event.key == pygame.K_b and player.rect.colliderect(shop_speed.rect) and money >= shop_speed_price and speed < 8 and wave_pointer == False:
                    money -= shop_speed_price
                    shop_speed_price += shop_speed_price + shop_speed_price_bonus
                    speed += 1
                    shop_speed_price_bonus += 100

                if event.key == pygame.K_b and player.rect.colliderect(shop_health.rect) and money >= shop_health_price and health < 3 and wave_pointer == False:
                    money -= shop_health_price
                    health += 1
                    shop_health_price += shop_health_price

        for i in range(level):
            if wave:
                Orks.append(Ork())
        wave = False

        if Orks == []:
            wave_pointer = False

        if wave_pointer:
            shop_alpha = 150
            wave_info_alpha = 0
        else:
            shop_alpha = 255
            if wave_info_alpha >= 255:
                alpha_direction = False
            if wave_info_alpha <= 0:
                alpha_direction = True

            if alpha_direction:
                wave_info_alpha += 10
            if alpha_direction == False:
                wave_info_alpha -= 10

        if level > best_level:
            best_level = level
            plik = open("best_score.txt", "w")
            plik.write(str(best_level))
            plik.close()
        
        if level_count >= 10:
            ork_speed += 1
            level_count = 0

        money_image = pixel_font.render(f"{money}", True, 'white')
        money_image_rect = money_image.get_rect(bottomleft=(115, 719))
        #money_image_rect = money_image.get_rect(bottomleft=(140, 705))
        money_image.set_alpha(180)

        level_image1 = pixel_font.render(f"Level", True, 'white')
        level_image_rect1 = level_image1.get_rect(bottomright=(1280, 510))
        level_image1.set_alpha(180)

        level_image = pixel_font.render(f"{level}", True, 'white')
        level_image_rect = level_image.get_rect(center=(1173, 550))
        level_image.set_alpha(180)

        money_size = pixel_font_thin.render(f"Increase range: {shop_size_price}", True, 'white')

        money_size_rect = money_size.get_rect(topleft=(2, 130))
        money_size.set_alpha(180)

        money_cooldown = pixel_font_thin.render(f"Decrease cooldown: {shop_cooldown_price}", True, 'white')
        money_cooldown_rect = money_cooldown.get_rect(topleft=(2, 340))
        money_cooldown.set_alpha(180)

        money_duration = pixel_font_thin.render(f"Increase attack duration: {shop_duration_price}", True, 'white')
        money_duration_rect = money_duration.get_rect(topleft=(2, 550))
        money_duration.set_alpha(180)

        money_speed = pixel_font_thin.render(f"Increase speed: {shop_speed_price}", True, 'white')
        money_speed_rect = money_speed.get_rect(topright=(1280, 130))
        money_speed.set_alpha(180)

        money_health = pixel_font_thin.render(f"Buy health: {shop_health_price}", True, 'white')
        money_health_rect = money_health.get_rect(topright=(1280, 340))
        money_health.set_alpha(180)

        coin_icon = pygame.image.load("assets/coin_1.2.png")
        coin_icon_rect = coin_icon.get_rect(bottomleft=(5, 715))
        coin_icon.set_alpha(180)

        wave_information = pixel_font_thin.render(f"Press X to start the next level", True, 'white')
        wave_information_rect = wave_information.get_rect(center=(640, 360))
        wave_information.set_alpha(wave_info_alpha)

        window.blit(background, (0, 0))

        shop_size.draw(shop_alpha)
        shop_cooldown.draw(shop_alpha)
        shop_duration.draw(shop_alpha)
        shop_speed.draw(shop_alpha)
        shop_health.draw(shop_alpha)

        health_indicator.tick(health)

        weapon.tick(keys, speed, weapon_size)

        angle += 60

        player_x_cord = player.player_cord_x()
        player_y_cord = player.player_cord_y()

        weapon_rotated, weapon_rotated_rect = rotation(weapon_animation, angle, weapon_cord_x, weapon_cord_y)
        if draw_weapon:
            weapon.draw2()
            weapon.draw3(weapon_rotated,weapon_rotated_rect)

        for ork in Orks:
            if weapon.rect.colliderect(ork.rect) and draw_weapon:
                money += 25
                ork_dead = True
                ork.tick(player_x_cord, player_y_cord, ork_speed, animation_status_ork, ork_dead)
                ork.draw()
                Orks.remove(ork)
                ork_dead = False
            elif player.rect.colliderect(ork.rect):
                hit_sound.play()
                Orks.remove(ork)
                health -= 1
        if health == 0:
            end_screen(window,level)

        player.tick(keys, speed, weapon_size, draw_weapon, animation_status)
        player.draw()

        for ork in Orks:
            ork.tick(player_x_cord, player_y_cord, ork_speed, animation_status_ork, ork_dead)
            ork.draw()

        window.blit(money_image,money_image_rect)
        window.blit(level_image,level_image_rect)
        window.blit(level_image1, level_image_rect1)

        if weapon_size < 4:
            window.blit(money_size,money_size_rect)
        if weapon_cooldown_reduction > 2:
            window.blit(money_cooldown,money_cooldown_rect)
        if weapon_duration < 9:
            window.blit(money_duration,money_duration_rect)
        if speed < 8:
            window.blit(money_speed,money_speed_rect)
        window.blit(money_health,money_health_rect)

        health_indicator.draw()

        window.blit(cooldown_indicator_bg, cooldown_indicator_bg_rect)
        window.blit(cooldown_indicator, cooldown_indicator_rect)
        window.blit(duration_indicator, duration_indicator_rect)
        window.blit(cooldown_indicator2, cooldown_indicator2_rect)
        window.blit(wave_information, wave_information_rect)

        window.blit(coin_icon, coin_icon_rect)

        pygame.display.update()

def start_screen(window):
    run = True
    plik = open("best_score.txt", "r").read()
    best_level = plik
    alpha = 0
    alpha_direction = bool

    while run:
        background2 = pygame.image.load("assets/background1.png")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    main(pixel_font, pixel_font_thin,level)

        game_title = pixel_font.render(f"Orc Slayer", True, 'white')

        game_title_rect = game_title.get_rect(midtop=(640, 1))

        ork_start = pygame.image.load("assets/ork_start2.png")

        ork_start_rect = ork_start.get_rect(midtop =(960,100))

        legend1 = pixel_font_thin.render(f"Press W to move up", True, 'white')
        legend1_rect = legend1.get_rect(topleft =(20,60))

        legend2 = pixel_font_thin.render(f"Press A to move left", True, 'white')
        legend2_rect = legend2.get_rect(topleft =(20,120))

        legend3 = pixel_font_thin.render(f"Press D to move right", True, 'white')
        legend3_rect = legend3.get_rect(topleft =(20,180))

        legend4 = pixel_font_thin.render(f"Press S to move down", True, 'white')
        legend4_rect = legend4.get_rect(topleft =(20,240))

        legend5 = pixel_font_thin.render(f"Press X to start next level", True, 'white')
        legend5_rect = legend5.get_rect(topleft =(20,300))

        legend6 = pixel_font_thin.render(f"Press B when on a shop to purchase uprade", True, 'white')
        legend6_rect = legend6.get_rect(topleft =(20,360))

        legend7 = pixel_font_thin.render(f"Press SPACE to atack", True, 'white')
        legend7_rect = legend7.get_rect(topleft =(20,420))

        legend8 = pixel_font2.render(f"Press G to start game", True, 'white')
        legend8_rect = legend8.get_rect(bottomleft =(20,700))
        legend8.set_alpha(alpha)

        if alpha >= 255:
            alpha_direction = False
        if alpha <=0:
            alpha_direction = True

        if alpha_direction:
            alpha += 10
        if alpha_direction == False:
            alpha -= 10

        best_score = pixel_font.render(f"Best score: {best_level} ", True, 'white')
        best_score_rect = best_score.get_rect(topleft =(20,500))

        hint = pixel_font_thin.render(f"Hint: Orks don't spawn in the middle of the map", True, 'white')
        hint_rect = hint.get_rect(bottomleft =(650,700))

        window.blit(background2, (0, 0))
        window.blit(legend1,legend1_rect)
        window.blit(legend2,legend2_rect)
        window.blit(legend3,legend3_rect)
        window.blit(legend4,legend4_rect)
        window.blit(legend5,legend5_rect)
        window.blit(legend6,legend6_rect)
        window.blit(legend7,legend7_rect)
        window.blit(legend8,legend8_rect)
        window.blit(game_title,game_title_rect)
        window.blit(ork_start, ork_start_rect)
        window.blit(best_score, best_score_rect)
        window.blit(hint,hint_rect)

        pygame.display.update()

def end_screen(window,level):
    run = True
    alpha = 0
    alpha_direction = bool
    while run:
        background1 = pygame.image.load("assets/background2.png")
        game_over1 = pixel_font.render(f"GAME OVER", True, 'white')
        game_over1_rect = game_over1.get_rect(center =(640,160))
        score = pixel_font.render(f"Your score: {level}", True, 'white')
        score_rect = score.get_rect(center =(640,370))
        legend9 = pixel_font2.render(f"Press G to move to start screen", True, 'white')
        legend9_rect = legend9.get_rect(center =(640,600))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    start_screen(window)

        legend9.set_alpha(alpha)

        if alpha >= 255:
            alpha_direction = False
        if alpha <= 0:
            alpha_direction = True

        if alpha_direction:
            alpha += 10
        if alpha_direction == False:
            alpha -= 10

        window.blit(background1, (0, 0))
        window.blit(game_over1,game_over1_rect)
        window.blit(legend9,legend9_rect)
        window.blit(score,score_rect)

        pygame.display.update()

start_screen(window)
