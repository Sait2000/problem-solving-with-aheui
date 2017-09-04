from __future__ import print_function
from storage import AheuiStorage, AheuiHalt
from a import main


try:
    unichr_ = unichr
except NameError:
    unichr_ = chr


if __name__ == '__main__':
    import io

    for in_data, out_data in [
        (u'A*(B+C)', u'ABC+*'),
        (u'A+(B*C)*D*E+F', u'ABC*D*E*+F+'),
        (u'A+(B/C)*D/E+F', u'ABC/D*E/+F+'),
        (u'A+(B+C)*D', u'ABC+D*+'),
        (u'A+(((B+C))*D)', u'ABC+D*+'),
        (u'A*B*C*D', u'AB*C*D*'),
        (u'(A+(B/C))*D/E+F-G+(((H+I))*J)', u'ABC/+D*E/F+G-HI+J*+'),
    ]:
        s = AheuiStorage()

        in_file = io.StringIO(in_data + '\n')

        def input_char():
            c = in_file.read(1)
            if not c:
                return -1
            return ord(c)

        try:
            main(s, input_char=input_char)
        except AheuiHalt:
            pass
        else:
            raise Exception

        out_file = io.StringIO()
        for t, v in s.output_buffer:
            out_file.write({
                'char': unichr_(v),
                'num': u'{}'.format(v),
            }[t])
        out_file.seek(0)
        out_res = out_file.read()
        success = out_data.rstrip(u'\n') == out_res.rstrip(u'\n')
        print(u'-' * 50)
        print(u'[{}] input: {!r}'.format(
            u'O' if success else u'X',
            in_data,
        ))
        print(u'expected output: {!r}'.format(out_data))
        print(u'  actual output: {!r}'.format(out_res))
