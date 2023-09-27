from plates import is_valid

def main():
    test_valid()

def test_valid():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False
    assert is_valid("cs50p") == False
    assert is_valid("23") == False
    assert is_valid("cs") == True
    assert is_valid("cs.,32") == False
    assert is_valid("cs32") == True