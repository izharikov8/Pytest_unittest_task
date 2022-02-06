import unittest
from ya_api import *


class TestFunction(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_create_folder(self):
        self.assertEqual(create_folder('TestFolder'), 201)

    def test_delete_folder(self):
        self.assertEqual(delete_folder('TestFolder'), 204)

    def test_get_folder(self):
        self.assertEqual(get_folder('TestFolder'), 404)
        