import pytest

from main import partA, parse_data

testingA = [('ne,ne,ne', 3), ('ne,ne,sw,sw', 0), ('ne,ne,s,s', 2),
            ('se,sw,se,sw,sw', 3)]


@pytest.mark.parametrize('test_input,expected', testingA)
def test_partA(test_input, expected):
    data = parse_data(test_input)
    ans1 = partA(data)
    assert ans1 == expected