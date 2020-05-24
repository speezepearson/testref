import logging
from pathlib import Path
import re
import urllib.parse

from pandocfilters import toJSONFilter, Link, Image, Strong, Str

from testref import TestName

CWD = Path.cwd()
TESTINFO_DIR = CWD / 'testinfo'
TEST_NAMES = {
    TestName(str(path.relative_to(TESTINFO_DIR).with_suffix("")))
    for path in TESTINFO_DIR.glob("**/*.png")
}

def linkify_tests(key, value, format, meta):
    if key == 'Image':
        attr, content, (urlStr, title) = value
        url = urllib.parse.urlparse(urlStr)
        if url.scheme != "test":
            return

        name = None
        if url.path.startswith("~"):
            pattern = url.path[1:]
            matches = list(sorted({n for n in TEST_NAMES if re.search(pattern, n)}))
            if len(matches) == 1:
                [name] = matches
            else:
                logging.error(f"pattern {pattern!r} does not uniquely identify a test; matches = {matches}")
        else:
            name = TestName(url.path)
            if name not in TEST_NAMES:
                name = None
                logging.error(f"test name {name!r} does not seem to exist!")

        if name is None:
            return Strong([Str("[???]")])

        img = Image(attr, content, (f"testinfo/{name}.png", title))
        return Link(attr, [img], (f"testinfo/{name}.html", title))

def main():
  toJSONFilter(linkify_tests)

if __name__ == "__main__":
    main()
