import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("вера", "Вера"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!Внимание", "!Внимание"),
    (" test", " test")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" test", "test"),
    ("  Некая фраза", "Некая фраза"),
    ("   10 шт.", "10 шт.")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ",""),
    (None, None),
    (" ! Ahtung", "! Ahtung"),
    ("Text", "Text")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_ch, expected", [
    ("String", "t", True),
    ("My life", " ", True),
    ("12 chairs", "2", True),
    ("cat's", "'", True)
])
def test_contains_positive(input_str, input_ch, expected):
    assert string_utils.contains(input_str, input_ch) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_ch, expected", [
    ("String", "T", False),
    ("", "", True)
])
def test_contains_negative(input_str, input_ch, expected):
    assert string_utils.contains(input_str, input_ch) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("String", "tri", "Sng"),
    ("Ma  rokko", " ", "Marokko"),
    ("List of symbols", "List of", " symbols"),
    ("123 sun", "23", "1 sun"),
    ("t@x", "@", "tx")
])
def test_delete_symbol_positive(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("String", "", "String"),
    ("Marokko", " ", "Marokko"),
    ("   ", " ", ""),
    ("   ", "  ", " ")
])
def test_delete_symbol_negative(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected