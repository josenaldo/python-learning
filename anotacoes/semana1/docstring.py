import textwrap

# Exemplos de DocString
docstring1 = """
This is an example
of a multi-line string
in Python.
"""
print("docstring 1------------------------------")
print(docstring1)
print()

docstring2 = """\
    This is an example
                    of a multi-line string
            in Python.
"""
print ("docstring 2------------------------------")
print (docstring2)
print()

ident1 = """
    This is an example
    of a multi-line string
    in Python.
"""
print ("ident1------------------------------")
print(textwrap.dedent(ident1).strip())
print()

ident2 = """
    This is an example
        of a multi-line string
    in Python.
"""
print ("ident2------------------------------")
print(textwrap.dedent(ident2).strip())
print()

ident3 = """
    This is an example
        of a multi-line string
            in Python.
"""
print ("ident3-------------------3----------")
print(textwrap.dedent(ident3).strip())
print()

ident4 = """
            This is an example
        of a multi-line string
    in Python.
"""
print ("ident4------------------------------")
print(textwrap.dedent(ident4).strip())
print()

ident5 = """
            This is an example
    of a multi-line string
        in Python.
"""
print ("ident5------------------------------")
print(textwrap.dedent(ident5).strip())
print()

ident6 = """
                                                            This is an example
                                of a multi-line string
                                            in Python.
                                                                                    OK.
"""
print ("ident6-----------------------------")
print(textwrap.dedent(ident6).strip())
print()