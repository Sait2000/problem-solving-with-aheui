# coding: utf-8

from __future__ import print_function
from storage import AheuiStorage, AheuiHalt, storage_ids


try:
    unichr_ = unichr
except NameError:
    unichr_ = chr

stack0 = storage_ids[0]
stack1 = storage_ids[1]
stack2 = storage_ids[4]
stack3 = storage_ids[7]


def input_num():
    return int(input())


def main(s):
    # s.push(2500)
    while s.push_strict(5) and not s.mul_catch():
        pass
    s.duplicate()
    s.mul()
    s.push_strict(4)
    s.mul()

    s.send_to(stack2)

    for n in [2, 5, 5, 4, 2, 6, 6, 4, 2, 7, 2, 5, 6, 6, 6]:
        s.push(n)

    s.activate(stack1)
    for n in [6, 6, 0, 4, 4, 10, 0, 4, 4, 10, 6, 6, 0, 0, 8]:
        s.push(n)

    s.activate(stack0)

    while s.send_to_catch(stack2):
        s.activate(stack2)

        # update
        s.aheui_eval(u'밞밝따밤따')  # s.push(252)
        s.sub()
        s.duplicate()
        s.add()
        s.sub()

        s.duplicate()
        s.send_to(stack1)
        s.activate(stack1)
        s.swap()

        while s.duplicate() and s.pop_is_nonzero():
            s.push_strict(0)
            s.push_strict(0)
            s.compare()
            s.sub()

            s.swap()

            s.duplicate()
            s.pop_print_num()

            s.push_strict(5)
            s.push_strict(5)
            s.add()
            s.pop_print_char()

            s.push_strict(0)
            s.push_strict(0)
            s.compare()
            s.add()

            s.swap()

        s.pop()
        s.pop()

        s.activate(stack0)

    s.halt()


if __name__ == '__main__':
    s = AheuiStorage()
    try:
        main(s)
    except AheuiHalt:
        pass

    for t, v in s.output_buffer:
        print({'char': unichr_(v), 'num': v}[t], end='')
