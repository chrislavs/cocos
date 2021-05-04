"""
Testing load_tmx() behavior with a tileset.
Ensure code works when given a tileset that does not contain a picture element.

Tests being run with pytest.
"""

from __future__ import division, print_function, unicode_literals

import sys
import os

import pyglet
#assert pyglet.mock_level == 1
sys.path.insert(0, 'pyglet_mockup1')
import cocos.layer
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from cocos.tiles import load_tmx, tileset_tiles

class Test_Tmx_Load_Tileset(object):

    # Test contains multiple tilesets
    def test_load_tmx_file_one(self):
        load_tmx("TestOne.tmx")
        print()
        print(tileset_tiles)
        assert tileset_tiles[1] == 'white4x3.png'
        assert tileset_tiles[2] == 'white4x3.png'
        assert tileset_tiles[3] == 'white4x3.png'
        assert tileset_tiles[4] == 'white4x3.png'
        assert tileset_tiles[5] == 'white4x3.png'
        assert tileset_tiles[6] == 'white4x3.png'
        assert tileset_tiles[7] == 'white4x3.png'
        assert tileset_tiles[8] == 'white4x3.png'
        assert tileset_tiles[9] == 'white4x3.png'
        assert tileset_tiles[10] == 'white4x3.png'

    # Test obtaining image sources from different locations, ensuring they load properly
    def test_load_tmx_file_two(self):
        load_tmx("TestTwo.tmx")
        print()
        print(tileset_tiles)
        assert tileset_tiles[1] == '../test/car.png'
        assert tileset_tiles[2] == '../test/fire.png'
        assert tileset_tiles[3] == '../test/dinosaur.gif'
        assert tileset_tiles[4] == '../samples/flag.png'
        assert tileset_tiles[5] == '../samples/fire.jpg'

