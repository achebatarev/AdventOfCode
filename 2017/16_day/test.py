import pytest
from main import partA, partB, parse_data, read_data, execute_instruction

testingA = [('s1', 'eabcd'), ('x3/4', 'abced'), ('pe/b', 'aecdb'),
            ('s4', 'bcdea')]
testingB = [('test.in', 0)]


@pytest.mark.parametrize('test_input,expected', testingA)
def test_partA(test_input, expected):
    arr = list(map(chr, range(ord('a'), ord('e') + 1)))
    arr = execute_instruction(arr, test_input)
    assert ''.join(arr) == expected


@pytest.mark.xfail()
@pytest.mark.parametrize('test_input,expected', testingB)
def test_partB(test_input, expected):
    data = read_data(test_input)
    parsed_data = parse_data(data)
    a = partB(parsed_data)
    assert a == expected
