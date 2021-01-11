#!/usr/bin/env python3
import pygame


class IntermediateGuiLayer:
    def __init__(self):
        pygame.init()
        self._pygame_display = pygame.display.set_mode([500, 500])
        self._continuing_main_loop = True

    def quit_game(self):
        self._continuing_main_loop = False
        pygame.quit()

    def start_main_loop(self):
        while self._continuing_main_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            # fill in the window with a single color
            self._pygame_display.fill(
                (20, 20, 20) # RGB color
            )

            pygame.draw.circle(
                self._pygame_display,
                (0, 255, 80), # RGB color
                (250, 250), # coordinates of the center of the circle (pixels)
                75 # radius of the circle (pixels)
            )
            pygame.display.flip()


class KeyRelay:
    # TODO
    pass


class Ship:
    # TODO
    pass


class Battlefield:
    # TODO
    pass


class Displayer:
    # TODO
    pass


if __name__ == "__main__":
    intermediate_gui_layer = IntermediateGuiLayer()
    intermediate_gui_layer.start_main_loop()
