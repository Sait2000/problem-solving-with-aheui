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
    s.duplicate()
    s.send_to(stack1)
    s.push(input_num())
    s.sub()
    s.duplicate()
    s.duplicate()

    s.push_strict(2)
    s.mod()
    if True:
        # XXX: aheui div/mod fragmentation
        s.duplicate()
        s.mul()
    s.swap()
    s.push_strict(0)
    s.compare()
    s.compare()
    if s.pop_is_nonzero():
        # impossible
        s.push_strict(2)
        s.push_strict(3)
        s.sub()
    else:
        # possible

        # > stack0: m*2
        #   stack1: m+M
        s.push_strict(2)
        s.div()
        s.duplicate()
        s.send_to(stack1)
        s.activate(stack1)
        s.sub()
        s.pop_print_num()
        while s.push_strict(5) and not s.add_catch():
            pass
        s.pop_print_char()
        s.activate(stack0)

    s.pop_print_num()
    s.halt()


if __name__ == '__main__':
    storage = AheuiStorage()
    try:
        main(storage)
    except AheuiHalt:
        pass

    for t, v in storage.output_buffer:
        if t == 'num':
            s = str(v)
        elif t == 'char':
            s = unichr_(v)
        else:
            raise ValueError('Invalid output type: {!r}'.format(t))
        print(s, end='')
