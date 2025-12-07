from string_utils import StringUtils
import pytest

string_utils = StringUtils()

@pytest.mark.parametrize("input_str, expected", [
('winter', 'Winter'),('skypro', 'Skypro'), ('dog', 'Dog')])
def test_capitalize(input_str, expected):
   assert expected == string_utils.capitalize(input_str)


@pytest.mark.parametrize("input_str, expected", [
(' winter', 'winter'),(' skypro', 'skypro'), (' dog', 'dog')])
def test_trim(input_str, expected):
   assert expected == string_utils.trim(input_str)


@pytest.mark.parametrize(
    'string,symbol,expected',
    [
        ('winter', 'w', True),
        ('skype', 'c', False),
        ('skype', 'r', True),
        ('dog', 'b', False)
    ]
)
def test_contains(string, symbol, expected):
    assert expected == string_utils.contains(string, symbol)


@pytest.mark.parametrize(
    'string,symbol,expected',
   [
        ('winter', 'w', 'inter'),
        ('skypro', 'p', 'skyro'),
        ('dog', 'k', 'dog')
  ]
)
def test_delete_symbol(string, symbol, expected):
    assert expected == string_utils.delete_symbol(string, symbol)





