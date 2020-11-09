"""
>>> div.render()
'<div></div>'

>>> div[div].render()
'<div><div></div></div>'
"""
from html import escape
from collections import namedtuple

class Tag(namedtuple("Tag", "name attr children")):
    def render(self):
        children = ''.join(c.render() for c in self.children)
        return f'<{self.name}>{children}</{self.name}>'

    # overwrites item[]
    def _getitem__(self, index):
        if isinstance(index, Tag):
            index = tuple([index])
        return self._replace(children=index)
    
    def __call__(self, *args, **kwargs):
        return self._replace(attr=dict(kwargs))

def render():
    if isinstance(index, Tag):
        index = tuple([index])
    return self._replace(children=index)

div = Tag('div', {}, [])

if __name__ == "__main__":
    import doctest
    doctest.testmod()