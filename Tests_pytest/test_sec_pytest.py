import pytest
from secretary_func import *


class TestPytest:
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_get_list(self):
        assert get_list(documents) == 'passport "2207 876234" "Василий Гупкин"'

    def test_get_name(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '10006')
        assert get_name(documents) == 'Аристарх Павлов'

    def test_get_shelf(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '10006')
        assert get_shelf(directories) == 'Номер полки - 2.'

    def test_add_doc(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '3')
        monkeypatch.setattr('builtins.input', lambda _: '888')
        monkeypatch.setattr('builtins.input', lambda _: 'passport')
        monkeypatch.setattr('builtins.input', lambda _: 'Ivan')
        assert add_doc(documents, directories) == 'Yes, doc added.'

    def test_delete_doc(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '10006')
        assert delete_doc(documents, directories) == 'Документ 10006 удалён.'

    def test_move_doc(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '3')
        monkeypatch.setattr('builtins.input', lambda _: '10006')
        assert move_doc(directories) == 'Документ успешно перенесен на полку.'

    def test_add_shelf(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '5')
        assert add_shelf(directories) == 'Полка 5 добавлена.'
        