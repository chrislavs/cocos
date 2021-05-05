"""
Testing load_tmx() behavior with a tileset.
Ensure code works when given a tileset that does not contain a picture element.

Tests being run with pytest.
"""

#from __future__ import division, print_function, unicode_literals
# os.environ['LANG'] = 'en_US'
# sys.path.insert(0, 'pyglet_mockup1')
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#assert pyglet.mock_level == 1
# import os
# import sys
# sys.path.insert(0, '/cocos/tiles.py')
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from cocos.tiles import load_tmx
from cocos import tiles


class Test_Tmx_Load_Tileset(object):

    # Test contains multiple tilesets
    def test_load_tmx_file_one(self):
        load_tmx("../clavallee_tests/testOne.tmx")
        print()
        # print(tileset_tiles)
        assert tiles.tileset_tiles[1] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[2] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[3] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[4] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[5] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[6] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[7] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[8] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[9] == '../clavallee_tests\\../utest/white4x3.png'
        assert tiles.tileset_tiles[10] == '../clavallee_tests\\../utest/white4x3.png'

    # Test obtaining image sources from different locations, ensuring they load properly
    def test_load_tmx_file_two(self):
        load_tmx("../clavallee_tests/TestTwo.tmx")
        print()
        # print(tileset_tiles)
        assert tiles.tileset_tiles[1] == '../clavallee_tests\\../test/car.png'
        assert tiles.tileset_tiles[2] == '../clavallee_tests\\../test/fire.png'
        assert tiles.tileset_tiles[3] == '../clavallee_tests\\../test/dinosaur.gif'
        assert tiles.tileset_tiles[4] == '../clavallee_tests\\../samples/flag.png'
        assert tiles.tileset_tiles[5] == '../clavallee_tests\\../samples/fire.jpg'

