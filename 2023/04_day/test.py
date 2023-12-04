from main import first, second, parse_data, read_data

PART1_ANSWER = 13 
PART2_ANSWER = 30

def test_part1():
    a = first(parse_data(read_data('test.in')))
    assert a == PART1_ANSWER 

def test_part2():
    a = second(parse_data(read_data('test.in')))
    assert a == PART2_ANSWER 
