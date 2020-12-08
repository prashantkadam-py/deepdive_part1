from functools import singledispatch
from collections.abc import Sequence
from numbers import Integral
from html import escape

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def htmlize_integral_number(a):
    return f"{a}(<i>{str(hex(a))}</i>)"

@htmlize.register(Sequence)
def html_squence(l):
    items = (f"<li>{htmlize(item)}</li>"
                for item in l
            )

    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def html_escape(arg):
    return escape(str(arg))

@htmlize.register(str)
def html_str(s):
    return html_escape(s).replace("\n", "<br/>\n")




if __name__ == "__main__":
    print(htmlize("Python"))
    print(htmlize([1,2,3]))
