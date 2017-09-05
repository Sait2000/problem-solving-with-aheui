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

def input_char():
    import sys
    c = sys.stdin.read(1)
    if c:
        return ord(c)
    return -1


def main(s):
    s.activate(stack3)
    s.push(0)
    s.push(0)
    s.push(0)
    while s.pop_catch():
        s.activate(stack0)
        s.push(input_num())
        while True:
            s.duplicate()
            s.activate(stack1)
            if s.duplicate_catch():
                s.send_to(stack2)
                s.send_to(stack0)
                s.activate(stack0)
                s.compare()
                if not s.pop_is_nonzero():
                    s.send_to(stack2)
                    s.activate(stack2)
                    s.swap()
                    break
            else:
                s.activate(stack0)
                s.send_to(stack1)
                break
        while s.activate(stack2) and s.send_to_catch(stack1):
            pass
        s.activate(stack3)
    s.activate(stack1)
    s.pop()
    s.pop_print_num()

    s.halt()


def main_oneliner(s):
    s.push(input_num())
    s.duplicate()
    s.push(input_num())
    s.duplicate()
    s.send_to(stack1)
    s.compare()
    s.activate(stack1)
    s.send_to(stack0)
    s.activate(stack0)
    s.swap()

    if not s.pop_is_nonzero():
        s.swap()

    s.duplicate()
    s.push(input_num())
    s.duplicate()
    s.send_to(stack1)
    s.compare()
    s.activate(stack1)
    s.send_to(stack0)
    s.activate(stack0)
    s.swap()

    if not s.pop_is_nonzero():
        s.swap()
    s.pop()

    s.duplicate()
    s.send_to(stack1)
    s.swap()
    s.duplicate()
    s.send_to(stack1)
    s.compare()
    s.send_to(stack1)
    s.activate(stack1)

    if not s.pop_is_nonzero():
        s.swap()
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
