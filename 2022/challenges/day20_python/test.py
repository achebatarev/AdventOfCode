import pytest
from main import partA, partB, parse_data, read_data

testingA = [('test.in', 3)]
testingB = [('test.in', 0)]


@pytest.mark.parametrize('test_input,expected', testingA)
def test_partA(test_input, expected):
    data = read_data(test_input)
    parsed_data = parse_data(data)
    a = partA(parsed_data)
    assert a == expected


@pytest.mark.parametrize('test_input,expected', testingB)
def test_partB(test_input, expected):
    data = read_data(test_input)
    parsed_data = parse_data(data)
    a = partB(parsed_data)
    assert a == expected
