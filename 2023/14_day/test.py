from main import first, second, parse_data, read_data, run_cycle

PART1_ANSWER = 136
PART2_ANSWER = 64 

def test_part1():
    a = first(parse_data(read_data('test.in')))
    assert a == PART1_ANSWER 

def test_part2_cycle1():
    a = run_cycle(tuple([tuple(e) for e in parse_data(read_data('test.in'))]))
    assert a == tuple(map(tuple, parse_data(read_data('cycle1.in'))))

def test_part2_cycle2():
    a = run_cycle(tuple([ tuple(e) for e in parse_data(read_data('test.in'))]))
    a = run_cycle(a)
    assert a == tuple(map(tuple, parse_data(read_data('cycle2.in'))))

def test_part2():
    a = second(parse_data(read_data('test.in')))
    assert a == PART2_ANSWER 
