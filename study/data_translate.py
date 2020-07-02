import sys
import prettytable as pt



mydict = {
    '1': 1,
    '0b1': 0b1,
    '0o1': 0o1,
    '0x1': 0x1,
    'int(\'f\',16)': int('f',16),
    'hex(int(\'17\',8))': hex(int('17',8)),
    '0xe7': 0xe7,
    '\'\\xe7\'': '\xe7',
    'b\'xe7\'': b'xe7'
}




if __name__ == "__main__":
    tb = pt.PrettyTable()
    tb.field_names= ["Expression","Value","Type","Memort address","Memory size"]
    for i in mydict:
        tb.add_row([i, mydict[i], type(mydict[i]), id(mydict[i]), sys.getsizeof(mydict[i])])

    print(tb)