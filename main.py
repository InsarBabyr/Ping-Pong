from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')

font.init()
font = font.SysFont('Arial', 30)
clock = time.Clock()

FPS = 60
win_height = 500
win_width = 700
speed_x = 3
speed_y = 3
finish = False
run = True

bgcolor = (200, 255, 255)
background = transform.scale(image.load('bg.jpg'), (win_width, win_height))
background.fill(bgcolor)
lose_l = font.render("PLayer_1 lose!", 1, (255,0,0))
lose_r = font.render("PLayer_2 lose!", 1, (255,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

rocket_l = Player('roket.png', 30, 180, 2, 20, 100)
rocket_r = Player('roket.png', 640, 180, 2, 20, 100)
ball = Player('ball1.png',350, 250, 3,30,30)


while run != False:
    for e in event.get():
        if e.type == QUIT:
            run = False
                
    if finish != True:
        window.blit(background, (0,0))
        rocket_l.reset()
        rocket_l.update_l()
        rocket_r.reset()
        rocket_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(rocket_l,ball) or sprite.collide_rect(rocket_r,ball):
            speed_x *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_l, (200,200))

        if ball.rect.x > 700:
            finish = True
            window.blit(lose_r, (260,210))
        ball.reset()
    display.update()
    clock.tick(FPS)

