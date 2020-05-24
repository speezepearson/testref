.PHONY: parse-testinfo

all: examples/basic/README.markdown examples/fibonacci/README.markdown README.markdown README.html

README.html: README.src.markdown parse-testinfo
	pandoc README.src.markdown -o README.html --filter=testref-pandoc

README.markdown: README.src.markdown parse-testinfo
	pandoc README.src.markdown -o README.markdown --filter=testref-pandoc

parse-testinfo: pytest-output.xml
	python -m testref.parse_pytest_xunit2 "$<"

pytest-output.xml: pytest.ini $(shell find  . -name "*.py")
	pytest . --junit-xml="$@"; true

examples/%/README.markdown:
	cd $(shell dirname "$@") && $(MAKE) README.markdown
