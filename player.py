import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Resources/HappyFace.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed = 0
        self.acceleration = 0.2

    def update(self, *args):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_d]:
        #     self.rect.x += 3

        # if keys[pygame.K_a]:
        #     self.rect.x -= 3

        if keys[pygame.K_w]:
            # self.rect.y -= 4
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            # self.rect.y += 4
            self.speed += self.acceleration
        else:
            self.speed *= 0.70

        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0

        if self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0
