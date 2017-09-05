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
    while True:
        if not s.duplicate_catch():
            s.push_strict(3)
            s.push_strict(2)
            s.sub()
            s.push_strict(0)
            s.send_to(stack1)
            s.push(input_num())
            continue

        if s.pop_is_nonzero():
            s.push_strict(3)
            s.push_strict(2)
            s.sub()
            s.sub()
            s.swap()
            s.duplicate()
            s.send_to(stack1)
            s.activate(stack1)
            s.swap()
            s.send_to(stack0)
            s.activate(stack0)
            s.add()
            s.aheui_eval(u'발발따밤따빠따밝다')  # s.push(10007)
            s.mod()
            s.swap()
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
