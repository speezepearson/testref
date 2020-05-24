from pandocfilters import toJSONFilter, Link, Image
import urllib.parse

def behead(key, value, format, meta):
    if key == 'Image':
        attr, content, (urlStr, title) = value
        url = urllib.parse.urlparse(urlStr)
        if url.scheme == "testinfo":
            img = Image(attr, content, (f"testinfo/{url.path}.png", title))
            return Link(attr, [img], (f"testinfo/{url.path}.html", title))

if __name__ == "__main__":
  toJSONFilter(behead)
