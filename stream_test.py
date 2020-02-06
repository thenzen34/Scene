from random import random

from core.stream_io import StreamIO

in_file = 'test.double'

val = random()
def save():
    handle = open(in_file, 'wb')

    rw = StreamIO(handle, True)

    rw.write_double(val)
    print('write', val)


def load():
    handle = open(in_file, 'rb')

    rw = StreamIO(handle, True)

    result = rw.read_double()

    if result == val:
        print('load cool', val)
    else:
        print('load wrong', val, result)


save()
load()
