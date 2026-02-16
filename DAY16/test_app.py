from app import add, sub, multipuly, division
def test_add():
    result = add(2,3)
    assert result == 5

def test_sub():
    result = sub(2,3)
    assert result == -1

def test_mul():
    result = multipuly(2,3)
    assert result == 6

def test_dev():
    result = division(10,5)
    assert result == 2