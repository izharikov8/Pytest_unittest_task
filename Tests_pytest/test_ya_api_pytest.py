import pytest
from ya_api import *


class TestFunctions:

    def test_create_folder(self):
        assert create_folder('TestFolder') == 201

    def test_get_folder(self):
        assert get_folder('TestFolder') == 200

    def test_delete_folder(self):
        assert delete_folder('TestFolder') == 204
