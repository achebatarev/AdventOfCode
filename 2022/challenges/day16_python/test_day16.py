from main import read_data, parse_data, partA, partB
import pytest

testingA = [('test.in', 1651), ('linear_line.in', 2640), ('quadratic_line.in', 13468), ('circle.in', 1288), ('clusters.in', 2400)]
testingB = [('test.in', 1707), ('linear_line.in', 2670), ('quadratic_line.in', 12887), ('circle.in', 1484), ('clusters.in', 3680)]

@pytest.mark.parametrize('test_input,expected', testingA)
def test_partA(test_input, expected):
    data = read_data(test_input)
    parsed_data = parse_data(data)
    assert partA(parsed_data) == expected 

#@pytest.mark.skip(reason='too slow')
@pytest.mark.parametrize('test_input,expected', testingB)
def test_partB(test_input, expected):
    data = read_data(test_input)
    parsed_data = parse_data(data)
    assert partB(parsed_data) == expected 