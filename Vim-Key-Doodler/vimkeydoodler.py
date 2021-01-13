#!/usr/bin/env python3
# A very simple program for doodling with vim keybindings.
import pygame
import time
import sys


# This class controls what appears on the canvas at any given time and stores
# the coordinates of the pixels to be displayed onscreen.
class IntermediateGuiLayer:
    def __init__(self):
        pygame.init()
        self._pygame_display = pygame.display.set_mode([500, 500])
        pygame.display.set_caption("Vim Key Doodler")
        self._pixels = [ [] for i in range(51) ]
        for x in range(len(self._pixels)):
            self._pixels[x] = [ " " for y in range(51) ]

    def show_pixel(self, x, y, char):
        # char must be one of the following: " ", "0", "1"
        try:
            self._pixels[x][y] = char
        except IndexError:
            pass

    def refresh_display(self):
        # fill in the window with a single color
        self._pygame_display.fill(
            (20, 20, 20) # RGB color
        )

        for x in range(len(self._pixels)):
            for y in range(len(self._pixels[x])):
                if self._pixels[x][y] == " ":
                    pass
                elif self._pixels[x][y] == "0":
                    pygame.draw.rect(
                        self._pygame_display,
                        (0, 220, 60), # RGB color
                        pygame.Rect(
                            (x*10, y*10), # Cartesian coordinates of pixel's top-left corner
                            (10, 10) # Width and height of pixel
                        )
                    )
                elif self._pixels[x][y] == "1":
                    pygame.draw.rect(
                        self._pygame_display,
                        (0, 255, 80), # RGB color
                        pygame.Rect(
                            (x*10, y*10), # Cartesian coordinates of pixel's top-left corner
                            (10, 10) # Width and height of pixel
                        )
                    )
                else:
                    raise ValueError(f"Invalid character located at ({x}, {y})")
        pygame.display.flip()

    def clear_canvas(self):
        for x in range(len(self._pixels)):
            for y in range(len(self._pixels[x])):
                self._pixels[x][y] = " "


# This class owns and controls the DrawingPoint object. The methods are meant to be called
# according to whatever keys are currently being pressed; for example, if the user presses
# the "H" key, then KeyRelay.press_h() should be called.
class KeyRelay:
    def __init__(self, drawing_point = None):
        self._drawing_point = drawing_point

    def press_h(self):
        if self._drawing_point.x_position > -1:
            self._drawing_point.move_left()
        else:
            self._drawing_point.x_position = 50

    def press_j(self):
        if self._drawing_point.y_position < 50:
            self._drawing_point.move_down()
        else:
            self._drawing_point.y_position = 0

    def press_k(self):
        if self._drawing_point.y_position > -1:
            self._drawing_point.move_up()
        else:
            self._drawing_point.y_position = 50

    def press_l(self):
        if self._drawing_point.x_position < 50:
            self._drawing_point.move_right()
        else:
            self._drawing_point.x_position = 0


# This class represents the point being moved around on the canvas. It stores the x and y
# coordinates of that point.
class DrawingPoint:
    def __init__(self):
        if len(sys.argv) >= 3:
            self.x_position = int(sys.argv[1])
            self.y_position = int(sys.argv[2])
        else:
            self.x_position = 25
            self.y_position = 49

    def move_left(self):
        self.x_position -= 1

    def move_right(self):
        self.x_position += 1

    def move_up(self):
        self.y_position -= 1

    def move_down(self):
        self.y_position += 1


def main(game_object):

    while game_object["continuing"]:
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_object["continuing"] = False

        if pressed_keys[pygame.K_h]:
            game_object["key_relay"].press_h()
        if pressed_keys[pygame.K_j]:
            game_object["key_relay"].press_j()
        if pressed_keys[pygame.K_k]:
            game_object["key_relay"].press_k()
        if pressed_keys[pygame.K_l]:
            game_object["key_relay"].press_l()
        if pressed_keys[pygame.K_ESCAPE]:
            game_object["intermediate_gui_layer"].clear_canvas()
        if pressed_keys[pygame.K_q]:
            game_object["continuing"] = False

        time.sleep(0.05)

        game_object["intermediate_gui_layer"].show_pixel(
            game_object["drawing_point"].x_position,
            game_object["drawing_point"].y_position,
            "1"
        )
        game_object["intermediate_gui_layer"].show_pixel(
            game_object["drawing_point"].x_position - 1,
            game_object["drawing_point"].y_position,
            "0"
        )
        game_object["intermediate_gui_layer"].show_pixel(
            game_object["drawing_point"].x_position + 1,
            game_object["drawing_point"].y_position,
            "0"
        )
        game_object["intermediate_gui_layer"].show_pixel(
            game_object["drawing_point"].x_position,
            game_object["drawing_point"].y_position - 1,
            "0"
        )
        game_object["intermediate_gui_layer"].show_pixel(
            game_object["drawing_point"].x_position,
            game_object["drawing_point"].y_position + 1,
            "0"
        )

        game_object["intermediate_gui_layer"].refresh_display()

    pygame.quit()


if __name__ == "__main__":
    # This dict will contain all the objects, plus a boolean to tell if the game is continuing.
    game = {
        "continuing": True
    }

    game["drawing_point"] = DrawingPoint()

    game["key_relay"] = KeyRelay(game["drawing_point"]) # KeyRelay takes ownership of DrawingPoint

    game["intermediate_gui_layer"] = IntermediateGuiLayer()

    main(game)
