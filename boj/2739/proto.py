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
    s.send_to(stack1)
    s.push_strict(9)

    while s.duplicate() and s.pop_is_nonzero():
        s.push_strict(3)
        s.push_strict(2)
        s.sub()
        s.sub()
        s.duplicate()
        s.push_strict(9)
        s.swap()
        s.sub()
        s.duplicate()

        s.activate(stack1)
        s.duplicate()
        s.duplicate()

        s.pop_print_num()

        s.push_strict(8)
        s.push_strict(4)
        s.mul()
        s.duplicate()
        s.pop_print_char()
        s.push_strict(6)
        s.push_strict(7)
        s.mul()
        s.pop_print_char()
        s.pop_print_char()

        s.activate(stack0)
        s.pop_print_num()

        s.push_strict(8)
        s.push_strict(4)
        s.mul()
        s.duplicate()
        s.pop_print_char()
        s.push_strict(8)
        s.push_strict(8)
        s.mul()
        s.push_strict(3)
        s.sub()
        s.pop_print_char()
        s.pop_print_char()

        s.send_to(stack1)
        s.activate(stack1)
        s.mul()
        s.pop_print_num()
        s.push_strict(5)
        s.push_strict(5)
        s.add()
        s.pop_print_char()

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
