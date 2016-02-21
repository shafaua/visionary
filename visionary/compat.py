import sys

is_py2 = (sys.version_info[0] == 2)
is_py3 = (sys.version_info[0] == 3)

if is_py2:
    bytes = str
    str = unicode
    basestring = basestring
    file_ = file
elif is_py3:
    from io import IOBase
    str = str
    bytes = bytes
    basestring = (str, bytes)
    file_ = IOBase
