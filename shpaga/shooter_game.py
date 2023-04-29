from pygame import *

window = display.set_mode((700,500))
display.set_caption('наверное круто')
background = transform.scale(image.load('city_2.png'),(700,500))

sprite1 = transform.scale(image.load('princess_1.png'),(100,100))
sprite2 = transform.scale(image.load('Asset 7@4x.png'),(100,100))
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65))     
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 700 - 80: 
            self.rect.x += self.speed
    def fire(self): 
        bullet = Bullet('bomb-4.png', self.rect.centerx, self.rect.top, 5) 
        bullets.add(bullet) 
class Bullet(GameSprite): 
    def update(self): 
        self.rect.y -= self.speed 
        if self.rect.y < 0: 
            self.kill() 
bullets = sprite.Group() 
x1 = 200
y1 = 200
x2 = 150
y2 = 100
speed = 10

clock = time.Clock()




game = True
while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite1,(x2,y2))

    keys_najali = key.get_pressed()


    if keys_najali[K_a] and x1 > 0:
        x1 -= speed

    if keys_najali[K_d] and x1 < 690:
        x1 += speed


    if keys_najali[K_LEFT] and x2 > 0:
        x2 -= speed

    if keys_najali[K_RIGHT] and x2 < 690:
        x2 += speed
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(75)
    display.update()






