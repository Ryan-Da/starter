#!/usr/bin/env python
import pygame

pygame.init()
bg_size = (50, 50)
screen = pygame.display.set_mode((50, 50))
pygame.display.set_caption("222")
image1 = pygame.image.load("image/1.png")
screen.blit(image1, (0, 0))

print("fee")