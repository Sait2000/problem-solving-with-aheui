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
    while s.push_strict(5) and not s.add_check():
        pass

    s.push_strict(0)

    while True:
        s.swap()
        s.duplicate()

        if s.pop_is_nonzero():
            s.push_strict(2)
            s.sub()
            s.swap()

            s.push(input_num())
            s.push_strict(5)
            s.div()
            s.push_strict(8)
            s.sub()
            s.duplicate()
            s.push(0)
            s.compare()
            s.mul()
            s.push_strict(8)
            s.add()
            s.add()

        else:
            s.pop()
            s.pop_print_num()
            s.halt()


if __name__ == '__main__':
    s = AheuiStorage()
    try:
        main(s)
    except AheuiHalt:
        pass

    for t, v in s.output_buffer:
        print({'char': unichr_(v), 'num': v}[t], end='')
