from main import first, second, parse_data, read_data, hash_

PART1_ANSWER = 1320
PART2_ANSWER = 145

def test_part1():
    a = first(parse_data(read_data('test.in')))
    assert a == PART1_ANSWER 

def test_hash_():
    assert hash_('HASH') == 52 
    assert hash_('cm-') == 253
    assert hash_('ot=7') == 231

def test_part2():
    a = second(parse_data(read_data('test.in')))
    assert a == PART2_ANSWER 

