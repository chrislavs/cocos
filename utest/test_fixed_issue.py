import pygame
import sys
import os
from os import getenv
sys.path.insert(0, 'pyglet_mockup1')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pyglet

assert pyglet.mock_level == 1

from cocos.director import director

director.init()


class Test_Director(object):

    def test_scaled_resize_window(self):
        window = 0
        assert director.window.width == 640
        assert director.window.height == 480
        if sys.platform == 'darwin':
            viewportw, viewporth = director.window.get_viewport_size()
            if viewportw > director.window.width:
                vw, vh = viewportw, viewporth
                window = vw, vh
        else:
            window = director.window.width, director.window.height
        print(window)

        assert director.scaled_resize_window(director.window.width, director.window.width) == window

    def test_get_window_size(self):
        default_size = director.window.width, director.window.height
        assert director.get_window_size() == default_size


def test_pygame_version():
    v = pygame.__version__
    assert v == '1.9.6'
