.PHONY: parse-testinfo

README.markdown: README.src.markdown parse-testinfo
	pandoc README.src.markdown -o README.markdown --filter=testref-pandoc

parse-testinfo: pytest-output.xml
	python -m testref.parse_pytest_xunit2 "$<"

pytest-output.xml: $(shell find  . -name "*.py")
	pytest . --junit-xml="$@"; true
