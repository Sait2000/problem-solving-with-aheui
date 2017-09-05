# coding: utf-8
from __future__ import print_function
import collections
import os

OP_REQSIZE = [0, 0, 2, 2, 2, 2, 1, 0, 1, 0, 1, 0, 2, 0, 1, 0, 2, 2, 0, 1, 1, 0, 0, 2, 1, 0]
OP_STACKDEL = [0, 0, 2, 2, 2, 2, 1, 0, 1, 0, 1, 0, 2, 0, 1, 0, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0]
OP_STACKADD = [0, 0, 1, 1, 1, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 0, 0, 1, 1, 0, 0, 0]
#              ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ ln lc pn pc b2 b1 j
VAL_QUEUE = 21
VAL_PORT = 27
STORAGE_COUNT = 28

# ㄱ
# ㄲ
OP_DIV = 2  # ㄴ
OP_ADD = 3  # ㄷ
OP_MUL = 4  # ㄸ
OP_MOD = 5  # ㄹ
OP_POP = 6  # ㅁ
OP_PUSH= 7  # ㅂ
OP_DUP = 8  # ㅃ
OP_SEL = 9  # ㅅ
OP_MOV = 10  # ㅆ
OP_NONE= 11  # ㅇ
OP_CMP = 12  # ㅈ
# ㅉ
OP_BRZ = 14
# ㅋ
OP_SUB = 16  # ㅌ
OP_SWAP= 17  # ㅍ
OP_HALT= 18  # ㅎ

# end of primitive
OP_POPNUM = 19
OP_POPCHAR = 20
OP_PUSHNUM = 21
OP_PUSHCHAR = 22
OP_BRPOP2 = -3  # special
OP_BRPOP1 = -2  # special
OP_JMP = -1  # special

OP_BRANCHES = [OP_BRZ, OP_BRPOP1, OP_BRPOP2]
OP_JUMPS = OP_BRANCHES + [OP_JMP]
OP_BINARYOPS = [OP_DIV, OP_ADD, OP_MUL, OP_MOD, OP_CMP, OP_SUB]

OP_NAMES = [None, None, u'DIV', u'ADD', u'MUL', u'MOD', u'POP', u'PUSH', u'DUP', u'SEL', u'MOV', None, u'CMP', None, u'BRZ', None, u'SUB', u'SWAP', u'HALT', u'POPNUM', u'POPCHAR', u'PUSHNUM', u'PUSHCHAR', u'BRPOP2', u'BRPOP1', u'JMP']
OP_USEVAL = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

OPCODE_MAP = {}
for opcode, name in enumerate(OP_NAMES):
    if name is None:
        continue
    if name in [u'BRPOP1', u'BRPOP2', u'JMP']:
        opcode -= len(OP_NAMES)
    OPCODE_MAP[name] = opcode

label_name_map = {}
label_map = {}

lines = []

with open('1918.aheuis', 'rb') as fr:
    text = fr.read().decode('utf-8')

label_line_map = collections.defaultdict(list)

for row in text.split(u'\n'):
    if u';' in row:
        main, comment = row.split(u';', 1)
    else:
        main, comment = row, u''
    label = u''
    if u':' in main:
        label, main = main.split(u':')
        label = label.strip()
        label_name_map[label] = len(lines)
        label_line_map[len(lines)].append(label)
    main = main.strip()
    if not main:
        continue
    parts = main.split()
    opname = parts[0].encode('utf-8').upper().decode('utf-8')
    opcode = OPCODE_MAP[opname]
    val = parts[-1]
    try:
        if opcode in OP_JUMPS:
            if val in label_map:
                target = label_map[val]
            else:
                target = len(lines)
                label_map[val] = target
            lines.append((opcode, val))
        elif OP_USEVAL[opcode]:
            val = int(val)
            lines.append((opcode, int(val)))
        else:
            lines.append((opcode, -1))
    except Exception:
        os.write(2, b'parsing error: ln%d %s\n' % (len(lines), main.encode('utf-8')))
        raise
self_label_map = {}
for key in label_map.keys():
    self_label_map[label_map[key]] = label_name_map[key]


program_count_var = u'pos'
indent = u' ' * 4

if 0 not in label_line_map:
    label_line_map[0] = [None]


print(u'from storage import storage_ids')
print()
print(u'def main(s, input_char=None):')

print(u'{indent}{} = {!r}'.format(
    program_count_var,
    label_line_map[0][0],
    indent=indent,
))
print(u'{indent}while True:'.format(indent=indent))
print(u'{indent}{indent}if 0: pass'.format(indent=indent))

jumped = False

for line_no, (opcode, val) in enumerate(lines):
    if line_no in label_line_map:
        if not jumped and line_no > 0:
            print(u'{indent}{indent}{indent}{} = {!r}'.format(
                program_count_var,
                label_line_map[line_no][0],
                indent=indent,
            ))
        if len(label_line_map[line_no]) == 1:
            print(u'{indent}{indent}elif {} == {!r}:'.format(
                program_count_var,
                label_line_map[line_no][0],
                indent=indent,
            ))
        else:
            print(u'{indent}{indent}elif {} in {!r}:'.format(
                program_count_var,
                tuple(label_line_map[line_no]),
                indent=indent,
            ))

    jumped = False

    if opcode == OP_DIV:
        print(u'{indent}{indent}{indent}s.div()'.format(indent=indent))
    elif opcode == OP_ADD:
        print(u'{indent}{indent}{indent}s.add()'.format(indent=indent))
    elif opcode == OP_MUL:
        print(u'{indent}{indent}{indent}s.mul()'.format(indent=indent))
    elif opcode == OP_MOD:
        print(u'{indent}{indent}{indent}s.mod()'.format(indent=indent))
    elif opcode == OP_POP:
        print(u'{indent}{indent}{indent}s.pop()'.format(indent=indent))
    elif opcode == OP_PUSH:
        print(u'{indent}{indent}{indent}s.push({})'.format(val, indent=indent))
    elif opcode == OP_DUP:
        print(u'{indent}{indent}{indent}s.duplicate()'.format(indent=indent))
    elif opcode == OP_SEL:
        print(u'{indent}{indent}{indent}s.activate(storage_ids[{}])'.format(val, indent=indent))
    elif opcode == OP_MOV:
        print(u'{indent}{indent}{indent}s.send_to(storage_ids[{}])'.format(val, indent=indent))
    elif opcode == OP_CMP:
        print(u'{indent}{indent}{indent}s.compare()'.format(indent=indent))
    elif opcode == OP_BRZ:
        print(u'{indent}{indent}{indent}if not s.pop_is_nonzero(): {} = {!r}; continue'.format(
            program_count_var,
            val,
            indent=indent,
        ))
    elif opcode == OP_SUB:
        print(u'{indent}{indent}{indent}s.sub()'.format(indent=indent))
    elif opcode == OP_SWAP:
        print(u'{indent}{indent}{indent}s.swap()'.format(indent=indent))
    elif opcode == OP_HALT:
        print(u'{indent}{indent}{indent}s.halt()'.format(indent=indent))
    elif opcode == OP_POPNUM:
        print(u'{indent}{indent}{indent}s.pop_print_num()'.format(indent=indent))
    elif opcode == OP_POPCHAR:
        print(u'{indent}{indent}{indent}s.pop_print_char()'.format(indent=indent))
    elif opcode == OP_PUSHNUM:
        print(u'{indent}{indent}{indent}s.push(input_num())'.format(indent=indent))
    elif opcode == OP_PUSHCHAR:
        print(u'{indent}{indent}{indent}s.push(input_char())'.format(indent=indent))
    elif opcode == OP_BRPOP2:
        print(u'{indent}{indent}{indent}if not (s.swap_catch() and s.swap()): {} = {!r}; continue'.format(
            program_count_var,
            val,
            indent=indent,
        ))
    elif opcode == OP_BRPOP1:
        print(u'{indent}{indent}{indent}if not (s.duplicate_catch() and s.pop()): {} = {!r}; continue'.format(
            program_count_var,
            val,
            indent=indent,
        ))
    elif opcode == OP_JMP:
        jumped = True
        print(u'{indent}{indent}{indent}if True: {} = {!r}; continue'.format(
            program_count_var,
            val,
            indent=indent,
        ))
    else:
        raise ValueError('Invalid opcode')
