from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).parent

def test_testref_exists_on_pypi():
    assert requests.get('https://pypi.org/project/testref/').status_code == 200

def test_this_project_dogfoods():
    readme = (PROJECT_ROOT/'README.markdown').read_text()
    assert '![](testinfo/test_readme/test_testref_exists_on_pypi.png)](testinfo/test_readme/test_testref_exists_on_pypi.html)' in readme
