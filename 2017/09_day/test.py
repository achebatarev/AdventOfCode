import pytest
from main import parse_data, partA, partB

testingA = [('{}', 1), ('{<a>,<a>,<a>,<a>}', 1), ('{{{},{},{{}}}}', 16),
            ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
            ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
            ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)]


@pytest.mark.parametrize('test_input,expected', testingA)
def test_partA(test_input, expected):
    ans = partA(parse_data(test_input))
    assert ans == expected
