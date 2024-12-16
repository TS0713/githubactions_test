from src.math_operations import add,minus

def test_add():
    assert add(2,3)==5
    assert add(1,-1)==0

def test_minuns():
    assert minus(5,3)==2
    assert minus(1,1)==0 # added comment

