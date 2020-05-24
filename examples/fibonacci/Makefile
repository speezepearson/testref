README.markdown:
	pytest --junit-xml=test-output.xml; true
	python -m testref.parse_pytest_xunit2 test-output.xml
	pandoc README.src.markdown --filter testref-pandoc -o README.markdown
