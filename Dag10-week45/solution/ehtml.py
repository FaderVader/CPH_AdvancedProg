"""
A Html eDSL


>>> html.render()
'<html/>'

>>> div(_class="hello").render()
'<div class="hello"/>'

>>> a(href="#")["This is a link"].render()
'<a href="#">This is a link</a>'

>>> ul[li["item 1"], li["item 2"]].render()
'<ul><li>item 1</li><li>item 2</li></ul>'

>>> a(_class="navbar-brand", href="#")["Navbar"].render()
'<a class="navbar-brand" href="#">Navbar</a>'
 
>>> nav(_class="")[a(_class="navbar-brand", href="#")["Navbar"]].render()
'<nav class=""><a class="navbar-brand" href="#">Navbar</a></nav>'

"""
from html import escape
from enum import Enum
from collections import namedtuple, abc

class End(Enum):
    FULL = 0
    HALF = 1
    NEVER = 2

class Tag(namedtuple("Tag", "name attr children end")):

    def __new__(self, name, attr = None, children = None, end = End.HALF):
        return super().__new__(self, name, attr or {}, children or [], end)

    def __call__(self, *args, **kwargs):
        attr = dict(self.attr)
        attr.update(kwargs)
        return self._replace(attr=attr)

    def __getitem__(self, args):
        if not isinstance(args, tuple) or isinstance(args, Tag):
            args = tuple([args])
        return self._replace(children=args)

    def render(self):
        attrs = ''.join(f' {k.lstrip("_")}="{escape(str(v))}"'
                for k, v in sorted(self.attr.items())
                )

        children = render(c for c in self.children)
        if children:
            return f"<{self.name}{attrs}>{children}</{self.name}>"
        elif self.end == End.FULL:
            return f"<{self.name}{attrs}></{self.name}"
        elif self.end == End.HALF:
            return f"<{self.name}{attrs}/>"
        else:
            return f"<{self.name}{attrs}>"

def render(item):
    if isinstance(item, str):
        return escape(item)
    if isinstance(item, abc.Generator):
        return ''.join(render(c) for c in item)
    if isinstance(item, Tag):
        return item.render()
    else:
        return escape(str(item))


# Tags
tagnames = [ "div", "a", "ul", "li", "nav",
        "body", "head", "h1", "h2", "html",
        "p"]

for tagname in tagnames:
    globals()[tagname] = Tag(tagname)

noendtagnames = [ "meta", "link" ]

for tagname in noendtagnames:
    globals()[tagname] = Tag(tagname, end=End.NEVER)

fullendtagnames = [ "script", "title"]

for tagname in fullendtagnames:
    globals()[tagname] = Tag(tagname, end=End.FULL)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
