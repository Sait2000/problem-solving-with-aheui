from __future__ import print_function
from storage import AheuiStorage, AheuiHalt, storage_ids


try:
    unichr_ = unichr
except NameError:
    unichr_ = chr

stack0 = storage_ids[0]
stack1 = storage_ids[1]


def input_num():
    return int(input())


def main(s):
    s.push(input_num())
    while True:
        s.duplicate()
        s.push_strict(2)
        s.mod()
        if s.pop_is_nonzero():
            break
        s.push_strict(2)
        s.div()
    s.push_strict(2)
    s.swap()
    s.compare()
    s.pop_print_num()
    s.halt()


if __name__ == '__main__':
    s = AheuiStorage()
    try:
        main(s)
    except AheuiHalt:
        pass
    else:
        raise Exception

    for t, v in s.output_buffer:
        print({'char': unichr_(v), 'num': v}[t], end='')
