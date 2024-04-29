import pygame as pg
from random import randrange as rnd

# game size and refresh rate
WIDTH, HEIGHT = 800, 600
fps = 60


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.rect.right - rect.left
    else:
        delta_x = rect.right - ball.rect.left
    if dy > 0:
        delta_y = ball.rect.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.rect.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 20
        self.frame = 0

        # Define player's size and position
        self.width = WIDTH / 2
        self.height = HEIGHT / 2
        self.rect = pg.Rect(400, 500, 300, 50)


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.frame = 0

        self.radius = 20
        self.rect = int(self.radius * 2 ** 0.5)

        self.rect = pg.rect.Rect(rnd(self.rect, WIDTH - self.rect), HEIGHT // 2, self.rect, self.rect)
        self.dx, self.dy = 1, -1


class Object(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.list = [pg.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
        self.colorList = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]


class Game:
    def __init__(self):
        # initialize game
        pg.init()
        self.fps = fps

        # Create player object
        self.player = Player()
        self.ball = Ball()
        self.objects = Object()

        # set screen size and time + background
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.background = pg.image.load('images/a041213ba395a6bd46dea73b71d8a2e5.jpg').convert()
        self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))

        self.run()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.screen.blit(self.background, (0, 0))

            # Draw the objects
            [pg.draw.rect(self.screen, self.objects.colorList[color], block) for color, block in
             enumerate(self.objects.list)]
            pg.draw.rect(self.screen, pg.Color('white'), self.player.rect)
            pg.draw.circle(self.screen, pg.Color('white'), self.ball.rect.center, self.ball.radius)

            # use random movement for the ball
            self.ball.rect.x += self.ball.speed * self.ball.dx
            self.ball.rect.y += self.ball.speed * self.ball.dy

            # check for ball collision
            if self.ball.rect.centerx < self.ball.radius or self.ball.rect.centerx > WIDTH - self.ball.radius:
                self.ball.dx = -self.ball.dx
            if self.ball.rect.centery < self.ball.radius:
                self.ball.dy = -self.ball.dy

            # collision with player
            if self.ball.rect.colliderect(self.player.rect) and self.ball.dy > 0:
                self.ball.dy, self.ball.dx = detect_collision(self.ball.dx, self.ball.dy, self.ball, self.player.rect)

            # collision with block
            hit_index = self.ball.rect.collidelist(self.objects.list)
            if hit_index != -1:
                hit_rect = self.objects.list.pop(hit_index)
                hit_color = self.objects.colorList.pop(hit_index)
                self.ball.dx, self.ball.dy = detect_collision(self.ball.dx, self.ball.dy, self.ball, hit_rect)

                hit_rect.inflate_ip(self.ball.rect.width * 3, self.ball.rect.height * 3)
                pg.draw.rect(self.screen, hit_color, hit_rect)
                self.fps += 2

            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] and self.player.rect.left > 0:
                self.player.rect.left -= self.player.speed
            if keys[pg.K_RIGHT] and self.player.rect.left < WIDTH:
                self.player.rect.right += self.player.speed

            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    game = Game()