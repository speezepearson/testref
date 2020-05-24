A maximally simple usage of `testref`.

It has two test-cases:

-   `test_lower`, which passes
    [![](testinfo/test_str/test_lower.png)](testinfo/test_str/test_lower.html)
-   `test_upper`, which also passes
    [![](testinfo/test_str/test_upper.png)](testinfo/test_str/test_upper.html)

\^ The list above, which you can see in
[`README.src.markdown`](README.src.markdown), was written as:

``` {.markdown}
- `test_lower`, which passes ![](test:test_str/test_lower)
- `test_upper`, which also passes ![](test:test_str/test_upper)
```

To regenerate everything, just run:

``` {.bash}
    pytest --junit-xml=test-output.xml
    python -m testref.parse_pytest_xunit2 test-output.xml
    pandoc README.src.markdown --filter testref-pandoc -o README.markdown
```

or, equivalently, `make`.
