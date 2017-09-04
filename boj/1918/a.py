from storage import storage_ids

def main(s, input_char=None):
    pos = 'L0'
    while True:
        if 0: pass
        elif pos == 'L0':
            s.push(input_char())
            s.duplicate()
            s.push(48)
            s.compare()
            if not s.pop_is_nonzero(): pos = 'L7'; continue
            s.pop_print_char()
            if True: pos = 'L0'; continue
        elif pos == 'L7':
            s.duplicate()
            s.push(42)
            s.compare()
            if s.pop_is_nonzero():
                # *+-/
                while True:
                    # +-: push(1), */: push(2)
                    s.duplicate()
                    s.duplicate()
                    s.push(4)
                    s.mod()
                    s.add()
                    s.push(3)
                    s.mod()
                    s.activate(storage_ids[1])
                    if not s.duplicate_catch():
                        pos = 'L55'
                        break
                    if 1:
                        s.push(5)
                        s.add()
                        s.duplicate()
                        s.mul()
                        s.push(2)
                        s.mul()
                        s.push(3)
                        s.div()
                        s.push(5)
                        s.mod()
                    s.activate(storage_ids[0])
                    s.send_to(storage_ids[1])
                    s.activate(storage_ids[1])
                    s.compare()
                    if not s.pop_is_nonzero():
                        s.activate(storage_ids[0])
                        pos = 'L58'
                        break
                    s.pop_print_char()
                    s.activate(storage_ids[0])
            else:
                # ()\n
                s.duplicate()
                s.push(36)
                s.compare()
                if not s.pop_is_nonzero():
                    # \n
                    while s.activate(storage_ids[1]) and s.pop_print_char_catch():
                        pass
                    s.halt()
                s.duplicate()
                s.push(2)
                s.mod()
                if s.pop_is_nonzero():
                    # )
                    while True:
                        s.duplicate()
                        s.activate(storage_ids[1])
                        s.duplicate()
                        s.send_to(storage_ids[0])
                        s.activate(storage_ids[0])
                        s.compare()
                        if s.pop_is_nonzero():
                            break
                        s.activate(storage_ids[1])
                        s.pop_print_char()
                        s.activate(storage_ids[0])

                    s.pop()
                    s.activate(storage_ids[1])
                    s.pop()
                    s.activate(storage_ids[0])
                    pos = 'L777'
                else:
                    # (
                    pos = 'L55'

        elif pos == 'L55':
            s.activate(storage_ids[0])
            pos = 'L58'
        elif pos == 'L58':
            if s.swap_catch():
                pass
            s.send_to(storage_ids[1])
            pos = 'L777'
        elif pos == 'L777':
            while s.pop_catch():
                pass
            pos = 'L0'
