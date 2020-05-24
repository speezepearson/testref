\[OOC: this directory is pretending to be a Python package that provides
Fibonacci-related functions. But it's really an example of what a simple
`testref`-using project might look like. Some of its documentation is
broken -- as an exercise, you might consider fixing the documentation,
which is not *quite* dead-simple, for reasons you might discover.\]

------------------------------------------------------------------------

Utilities for Fibonacci-related stuff.

(A note on indexing: the `fib` function, starting at `n=0`, goes
`1, 1, 2, 3, ...`
[![](testinfo/examples.fibonacci.fibonacci.test_fib/test_zero_indexed_goes_1_1_2_3.png)](testinfo/examples.fibonacci.fibonacci.test_fib/test_zero_indexed_goes_1_1_2_3.html))

It also exposes the `approx_fib` function, which *quickly* calculates a
number within 1% of any Fibonacci number.
[![](testinfo/examples.fibonacci.fibonacci.test_fib/test_approx_fib_always_within_1_percent.png)](testinfo/examples.fibonacci.fibonacci.test_fib/test_approx_fib_always_within_1_percent.html)
