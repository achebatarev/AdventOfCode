from main import first, second, parse_data, read_data

PART1_ANSWER = 6 
PART2_ANSWER = 6 

def test_part1():
    a = first(parse_data(read_data('test.in')))
    assert a == PART1_ANSWER 

def test_part2():
    a = second(parse_data(read_data('test2.in')))
    assert a == PART2_ANSWER 
