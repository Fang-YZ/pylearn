import pytest
from calculator import square

def main():
    test_square()
    test_negative()
    test_zero()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():    
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

    """
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
    """
    """
    try:
        assert square(-2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    try:
        assert square(-3) == 9 
    except AssertionError:
        print("3 squared was not 9")"""
        
def test_str():
    with pytest.raises(TypeError):
        square("cat")
if __name__ == "__main__":
    main()
        