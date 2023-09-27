from bank import value

def main():
    test_value()
    test_value1()
    test_value2()


def test_value():
    assert value('hello') == 0
    assert value('Hello') == 0

def test_value1():
    assert value('hi') == 20

def test_value2():
    assert value('cs50') == 100
    assert value('50') == 100
    assert value("what's up?") == 100



if __name__ == "__main__":
    main()