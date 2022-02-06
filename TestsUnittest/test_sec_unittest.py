import unittest
from secretary_func import *
from unittest import mock


class TestFunctions(unittest.TestCase):

    def setUp(self):
        print('SetUp')

    def tearDown(self):
        print('tearDown')

    @unittest.mock.patch('builtins.input', return_value='11-2')
    def test_get_name(self, mocked_input):
        # with unittest.mock.patch('builtins.input', return_value='11-2'):
        self.assertEqual(get_name(documents), 'Геннадий Покемонов')

    @unittest.mock.patch('builtins.input', return_value='11-2')
    def test_get_shelf(self, mocked_input):
        self.assertEqual(get_shelf(directories), 'Номер полки - 1.')

    def test_get_list(self):
        self.assertEqual(get_list(documents), 'passport "2207 876234" "Василий Гупкин"')

    @unittest.mock.patch('builtins.input', side_effects=['3', '777', 'passport', 'Jon Snow'])
    def test_add_doc(self, mocked_input):
        self.assertEqual(add_doc(documents, directories), 'Yes, doc added.')

    @unittest.mock.patch('builtins.input', side_effects=['3', '11-2'])
    def test_move_doc(self, mocked_input):
        self.assertEqual(move_doc(directories), 'Документ успешно перенесен на полку.')

    @unittest.mock.patch('builtins.input', return_value='10006')
    def test_delete_doc(self, mocked_input):
        self.assertEqual(delete_doc(documents, directories), 'Документ 10006 удалён.')

    @unittest.mock.patch('builtins.input', return_value='4')
    def test_add_shelf(self, mocked_input):
        self.assertEqual(add_shelf(directories), 'Полка 4 добавлена.')
        