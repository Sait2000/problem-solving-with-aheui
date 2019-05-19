from __future__ import print_function
from storage import AheuiStorage, AheuiHalt, storage_ids


try:
    unichr_ = unichr
except NameError:
    unichr_ = chr

# current
stack0 = storage_ids[0]
# original
stack1 = storage_ids[1]
# res
stack2 = storage_ids[2]


def input_num():
    return int(input())


def main(s):
    s.push(input_num())
    s.duplicate()
    s.send_to(stack1)

    while True:
        s.duplicate()
        s.duplicate()
        s.push_strict(5); s.push_strict(5); s.add()
        s.div()
        s.add()
        s.push_strict(5); s.push_strict(5); s.add()
        s.mod()

        s.swap()
        s.push_strict(5); s.push_strict(5); s.add()
        s.mod()
        s.push_strict(5); s.push_strict(5); s.add()
        s.mul()
        s.add()

        s.push_strict(2)
        s.send_to(stack2)

        s.duplicate()
        s.activate(stack1)
        s.duplicate()
        s.send_to(stack0)
        s.activate(stack0)
        s.sub()
        if not s.pop_is_nonzero():
            break

    while s.activate(stack2) and s.add_catch():
        pass
    s.push_strict(2)
    s.div()
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
