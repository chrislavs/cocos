from __future__ import division, print_function, unicode_literals

import os
# This code is so you can run the samples without installing the package
import sys

from pyglet.gl import glPushMatrix, glPopMatrix

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))


import sys
from cocos.layer import MultiplexLayer, pyglet, Layer
from cocos.scene import Scene
import cocos
from cocos.director import director
from pyglet.window import mouse


def on_new_game():
    print("Game started")


def on_quit():
    director.window.close()


def on_show_fps(show_fps):
    director.show_FPS = show_fps


class MainMenu(cocos.menu.Menu):
    is_event_handler = True

    def __init__(self):
        super(MainMenu, self).__init__("My Game")

        items = []

        items.append(cocos.menu.MenuItem("New Game", on_new_game))
        items[0].y = 0
        items.append(cocos.menu.ToggleMenuItem("show FPS ", on_show_fps, director.show_FPS))
        items[1].y = 0
        # items.pop(1)
        items.append(cocos.menu.MenuItem("Quit", on_quit))
        items[2].y = 0
        items.append(cocos.menu.MenuItem("open next layer", self.on_open))
        items[3].y = 0

        # self.not_visible = items[0]
        # action = Hide(self.not_visible)
        # self.not_visible.do(action)

        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())

    def on_open(self):
        self.parent.switch_to(1)

   # def on_mouse_press(self, x, y, button, modifiers):
   #     if button & mouse.LEFT:
   #         item_width = self.not_visible.get_item_width() + 50
   #         item_height = self.not_visible.get_item_height()
   #         item_x = self.not_visible.x + 480
   #         item_y = self.not_visible.y + 382 - (3 * item_height)
   #         print(x, y)
   #         if item_x + item_width > x > item_x and item_y + item_height > y > item_y:
   #             sys.exit(1)
   #             raise Exception('non visible menu item invalid ')


class optMenu(cocos.menu.Menu):
    def __init__(self):
        super(optMenu, self).__init__("Options Menu")

        items = []

        items.append(cocos.menu.MenuItem("New Game", on_new_game))
        items[0].y = 80
        items.append(cocos.menu.ToggleMenuItem("show FPS ", on_show_fps, director.show_FPS))
        items[1].y = 40
        items.append(cocos.menu.MenuItem("Quit", on_quit))
        items[2].y = -100

        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())


if __name__ == "__main__":
    director.init(resizable=True, width=1280, height=720, caption="Demo Menu")

    scene = Scene()
    scene.add(MultiplexLayer(
        MainMenu(),
        optMenu(),
         ),
        z=1)

    director.run(scene)
