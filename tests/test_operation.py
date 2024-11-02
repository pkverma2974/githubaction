from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,3)==3

def test_sub():
    assert sub(5,2)==3
    assert sub(-2,2)==-4
