from fibonacci import fib, approx_fib

def test_zero_indexed_goes_1_1_2_3():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3

def test_approx_fib():
    assert abs(1 - approx_fib(10)/fib(10)) < 0.001
    assert abs(1 - approx_fib(100)/fib(100)) < 0.001
