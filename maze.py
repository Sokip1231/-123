#создай игру "Лабиринт"!
from pygame import *




window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(700, 500))
window.blit(background,(0, 0))
game = True
finish = False



clock = time.Clock()
speed = 5


class Gamesprite(sprite.Sprite):
    def __init__(self, jimage, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(jimage), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, widht, height, color, wall_x, wall_y):
        super().__init__()
        self.image = Surface((widht, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(Gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] :
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] : 
            self.rect.x += self.speed

class Enemy(Gamesprite):
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x < 410:
            self.direction = 'RIGHT'
        if self.rect.x > 560:
            self.direction = 'left'

    def __init__(self, jimage, speed, x, y):
        super().__init__(jimage, speed, x, y)
        self.direction = 'left'




heroes = Player('hero.png', 2, 10, 30)
cyborges = Enemy('cyborg.png', 4, 450, 345)
treasure = Gamesprite('treasure.png', 5, 550, 430)



wall1 = Wall(10, 360, (0, 255, 0), 100, 10)
wall2 = Wall(250, 10, (0, 0, 128), 100, 450)


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('pyshka.ogg')
treser = mixer.Sound('money.ogg')

gamenotover = True


font.init()
font = font.Font(None, 70)

win = font.render('ПОБЕДА', True, (255, 215, 0))
lose = font.render('ПОРАЖЕНИЕ', True, (255, 215, 0))


while gamenotover:

   
    if finish == False: 
        if sprite.collide_rect(heroes, treasure):
            finish = True
            treser.play()
        if sprite.collide_rect(heroes, wall1) or sprite.collide_rect(heroes, wall2):
            finish = True
            kick.play()
        
        window.blit(background,(0, 0))
        wall2.reset()
        wall1.reset()
        cyborges.reset()
        heroes.reset()
        heroes.update()
        cyborges.update()
        treasure.reset()
       
        

    



    for e in event.get():
        if e.type == QUIT:
            gamenotover = False
    clock.tick(60)
    display.update()