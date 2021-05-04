import pygame
import sys
import os
os.environ['LANG'] = 'en_US'
sys.path.insert(0, 'pyglet_mockup1')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pyglet

assert pyglet.mock_level == 1

from cocos.director import director
from cocos.audio.SDL import dll


director.init()


class Test_Director(object):

    def test_scaled_resize_window(self):
        # window = 0
        assert director.window.width == 640
        assert director.window.height == 480
        # if sys.platform == 'darwin':
        #     window = director.window.get_viewport_size()
        # else:
        #     window = director.get_window_size()
        # print(window)
        if sys.platform == 'darwin':
            window = (director.window.width*2),(director.window.height*2)
        else:
            window = director.get_window_size()
        print(window)

        assert director.scaled_resize_window\
                   (director.window.width, director.window.height) == window

    def test_get_window_size(self):
        default_size = director.window.width, director.window.height
        assert director.get_window_size() == default_size


class Test_SDL_DLL:

    def test_SDL_package(self):
        v = pygame.__version__
        assert v == '1.9.6'
        assert dll.private_function == dll._dll.private_function
