# import os
#
# import pygame
# import sys
# #
# sys.path.insert(0, 'pyglet_mockup1')
# import pyglet
#
# assert pyglet.mock_level == 1
# from cocos.director import director
#
# director.init()
#

#
# class Test_Director(object):
#
#     def test_default_windows_size(self):
#         vw, vh = 0, 0
#         viewportw, viewporth = 1200, 1440
#         if viewportw > director.window.width:
#             vw, vh = viewportw, viewporth
#         window = vw, vh
#         print(window)
#         assert director.window.width == 640
#         assert director.window.height == 480
#         assert director.scaled_resize_window(director.window.width, director.window.width) == window
#
#
# def test_pygame_version():
#     v = pygame.__version__
#     assert v == '1.9.6'
