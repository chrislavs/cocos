import pygame
import os
# from __future__ import division, print_function, unicode_literals
# set the desired pyglet mockup
import sys

from pyglet.window.cocoa import CocoaWindow

sys.path.insert(0, 'pyglet_mockup1')

from cocos.director import director

director.init()

rec = []


class Test_Director(object):

    def test_default_windows_size(self):
        assert director.window.width == 640
        assert director.window.height == 480
        assert director.scaled_resize_window(director.window.width, director.window.width) == True


def test_pygame_version():
    v = pygame.__version__
    assert v == '1.9.6'
