from Unit_Test import square

def main():
    test_positive()
    test_negative()
    test_zero()

def test_positive():
    assert square(2) == 4, "2 squared should be 4"
    assert square(3) == 9, "3 squared should be 9"

def test_negative():
    assert square(-2) == 4, "2 squared should be -4"
    assert square(-3) == 9, "3 squared should be -4"

def test_zero():
    assert square(0) == 0, "0 squared should be 0"


if __name__ == "__main__":
    main()