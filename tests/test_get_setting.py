"""Useage:
poetry run pytest -v -s
pytest -v -s
"""

from pathlib import Path

from get_setting import get_setting

SETTING_JSON = Path(__file__).parent / 'settings.json'


def test_setting_str():
    assert "a" == get_setting("test_str", SETTING_JSON)


def test_setting_int():
    assert 10 == get_setting("test_int", SETTING_JSON)


def test_setting_float():
    assert 0.0 == get_setting("test_float", SETTING_JSON)


def test_setting_dict():
    dic = get_setting("test_dict", SETTING_JSON)
    if isinstance(dic, dict):
        print(dic['file'])
        assert 10 == dic['aaa']


def test_setting_none():
    assert get_setting("test_abc", SETTING_JSON) is None
