from main import first, second, parse_data, read_data

PART1_ANSWER = 8
PART2_ANSWER = 10


def test_part1():
    a = first(parse_data(read_data("test.in")))
    assert a == PART1_ANSWER



def test_part2_small():
    a = second(parse_data(read_data("test1.in")))
    assert a == 4 

def test_part2_big():
    a = second(parse_data(read_data("test2.in")))
    assert a == 8 

def test_part2_junk():
    a = second(parse_data(read_data("test3.in")))
    assert a == 10 

def test_part2_enclosed_out():
    a = second(parse_data(read_data("test4.in")))
    assert a == 4 


