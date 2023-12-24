from main import first, second, parse_data, read_data

PART1_ANSWER = 405 
PART2_ANSWER = 400 

def test_part1_horizontal():
    a = first(parse_data(read_data('horizontal.in')))
    assert a == 400

def test_part1_vertical():
    a = first(parse_data(read_data('vertical.in')))
    assert a == 5 

def test_part1():
    a = first(parse_data(read_data('test.in')))
    assert a == PART1_ANSWER

def test_part2_horizontal():
    a = second(parse_data(read_data('horizontal.in')))
    assert a == 100

def test_part2_vertical():
    a = second(parse_data(read_data('vertical.in')))
    assert a == 300

def test_part2():
    a = second(parse_data(read_data('test.in')))
    assert a == PART2_ANSWER
