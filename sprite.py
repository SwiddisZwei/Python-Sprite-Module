#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
pygame.init()


class Sprite:

      # Constructor (Entering file location, x position, y position, screen surface)

    def __init__(
        self,
        img,
        x,
        y,
        screen,
        x_width=0,
        y_width=0,
        x_spam=0,
        y_spam=0,
        ):

        self.img = img
        self.x = x
        self.y = y

        self.sprite = pygame.image.load(self.img)
        self.screen = screen

            # Set Rect parameters to 0 by default

        if x_width is None or y_width is None or x_spam is None \
            or y_spam is None:
            pass
        else:
            self.x_width = x_width
            self.y_width = y_width
            self.x_spam = x_spam
            self.y_spam = y_spam

        self.x_num = 0
        self.y_num = 0

    def __init__(
        self,
        img,
        x,
        y,
        screen,
        x_spam=0,
        y_spam=0,
        ):
        self.img = img
        self.x = x
        self.y = y

        self.sprite = pygame.image.load(self.img)
        self.screen = screen

            # Set Rect parameters to 0 by default

        if x_width is None or y_width is None or x_spam is None \
            or y_spam is None:
            pass
        else:
            self.x_width = self.img.get_width() / x_spam
            self.y_width = self.img.get_height() / y_spam
            self.x_spam = x_spam
            self.y_spam = y_spam

      # Flip sprite, Enter True on x to flip horizontally; Enter True on y to flip vertically

    def flip(self, x_flip, y_flip):
        if x_flip:
            self.sprite = pygame.transform.flip(self.sprite, True,
                    False)
        elif y_flip:
            self.sprite = pygame.transform.flip(self.sprite, False,
                    True)
        else:
            self.sprite = pygame.transform.flip(self.sprite, True, True)

      # Change scale of the sprite, enter the width of x and width of y

    def scale(self, x_scale, y_scale):
        self.sprite = pygame.transform.scale(self.sprite, (x_scale,
                y_scale))

      # Draw function, draw sprite using blit function

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

      # Change image function, enter new image location

    def image(self, image):
        self.sprite = pygame.image.load(image)

      # Change x_position

    @property
    def x_position(self):
        return self.x

    @x_position.setter
    def x_position(self, new_x):
        self.x = new_x

      # Change y_position

    @property
    def y_position(self):
        return self.y

    @y_position.setter
    def y_position(self, new_y):
        self.y = new_y

      # Draw sprite sheet

    def draw_sheet(self):
        self.screen.blit(self.sprite, (self.x, self.y), (self.x_num
                         * self.x_width, self.y_num * self.y_width,
                         self.x_width, self.y_width))

      # Update position

    def update(self):
        if self.x_num < self.x_spam - 1:
            self.x_num += 1
        else:

            self.x_num = 0
            if self.y_num < self.y_spam - 1:
                self.y_num += 1
            else:
                self.y_num = 0



			
