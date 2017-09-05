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
    while not s.duplicate_catch():
        s.push(input_num())
        s.duplicate()
        s.add()
    s.send_to(stack1)
    while s.duplicate() and s.pop_is_nonzero():
        s.activate(stack1)
        s.duplicate()

        while s.duplicate() and s.pop_is_nonzero():
            s.activate(stack0)
            s.duplicate()
            s.activate(stack1)
            s.duplicate()
            s.send_to(stack0)
            s.activate(stack0)
            s.compare()
            s.push_strict(5)
            s.push_strict(5)
            s.add()
            s.mul()
            s.push_strict(8)
            s.push_strict(4)
            s.mul()
            s.add()
            s.pop_print_char()

            s.activate(stack1)

            s.push_strict(2)
            s.sub()

        s.pop()

        s.activate(stack0)
        s.push_strict(2)
        s.sub()

        s.push_strict(5)
        s.push_strict(5)
        s.add()
        s.pop_print_char()

    s.halt()


if __name__ == '__main__':
    s = AheuiStorage()
    try:
        main(s)
    except AheuiHalt:
        pass

    for t, v in s.output_buffer:
        print({'char': unichr_(v), 'num': v}[t], end='')
