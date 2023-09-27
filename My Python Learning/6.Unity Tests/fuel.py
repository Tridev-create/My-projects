from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_guage()

def test_convert():
    assert convert('1/2') == 50
    assert convert('1/4') == 25
    assert convert('1/100') == 1
    assert convert('99/100') == 99
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_guage():
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'