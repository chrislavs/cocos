import pygame
import sys
import os

sys.path.insert(0, 'pyglet_mockup1')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pyglet

assert pyglet.mock_level == 1

from cocos.director import director

director.init()


class Test_Director(object):

    def test_default_windows_size(self):
        window = 0
        if sys.platform == 'darwin':
            viewportw, viewporth = 1200, 1440
            if viewportw > director._usable_width:
                vw, vh = viewportw, viewporth
                window = vw, vh
        else:
            window = director._usable_width, director._usable_height
        print(window)
        assert director._usable_width == 640
        assert director._usable_height == 480
        assert director.scaled_resize_window(director._usable_width, director._usable_height) == window


def test_pygame_version():
    v = pygame.__version__
    assert v == '1.9.6'
