'''
rpu - The stupid realtime Python updater
Copyright @raspiduino 2021
Date created 27/1/2021
----------------------------------------
This is the test file for rpu. You can
modify any of this and try.
Usage: rpu.py pygametest.py
Require pygame

This test file show you how to edit a
pygame script and see the change.
'''

import pygame
import sys

pygame.init()

test = pygame.display.set_mode((500, 500))

test.fill([255,255,255])

pygame.draw.rect(test, (15,49,86), (50, 70, 200, 100))

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

pygame.display.update()
