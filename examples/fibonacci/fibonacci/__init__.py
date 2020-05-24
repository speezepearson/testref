def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b


_PHI = (1 + 5**.5) / 2
_FIB_VS_PHIN_CORRECTION_FACTOR = fib(100) / _PHI**100

def approx_fib(n: int) -> float:
    return _PHI**n * _FIB_VS_PHIN_CORRECTION_FACTOR
