"""

>>> div.render()
'<div></div>'

>>> div[div].render()
'<div><div></div></div>'

>>> ul[li["hello"], li["world"]].render()
'<ul><li>hello</li><li>world</li></ul>'

>>> li["<script>firenukes()</script>"].render()
'<li>&lt;script&gt;firenukes()&lt;/script&gt;</li>'

>>> div(_class="\\"...").render()
'<div class="&quot;..."></div>'

>>> html(lang="en")[
...   head,
...   body[
...     h1["Hello, World!"],
...     p["this is a cool edsl"]
...   ]
... ].render()
'<html lang="en"><head></head><body><h1>Hello, World!</h1><p>this is a cool edsl</p></body></html>'

"""
from html import escape
from collections import namedtuple

class Tag(namedtuple("Tag", "name attr children")):

    def render(self):
        attr = ''.join(f' {n.lstrip("_")}="{escape(str(v))}"' 
                for n, v in sorted(self.attr.items()))
        children = ''.join(render(c) for c in self.children)
        return f'<{self.name}{attr}>{children}</{self.name}>'

    def __getitem__(self, index):
        if not isinstance(index, tuple) or isinstance(index, Tag):
            index = tuple([index])
        return self._replace(children=index)
    
    def __call__(self, *args, **kwargs):
        return self._replace(attr=dict(kwargs))


a[1, 2] === a.__getitem__((1,2))
a(1, 2) === a.__call__(1, 2)

namedtuple("Point", "x y")

def render(obj):
    if isinstance(obj, Tag):
        return obj.render()
    else:
        return escape(str(obj))

tagnames = ["div", "html", "body", "head", "div", "ul", "li",
    "h1", "p"]

for name in tagnames:
    globals()[name] = Tag(name, {}, [])

if __name__ == "__main__":
    import doctest
    doctest.testmod()


