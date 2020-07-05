#!/usr/bin/env python3
import sys
try:
    import prettytable as pt
except Exception as e:
    print("Failed to import prettytable,try to install with pip3.",e)
    sys.exit(1)

def error(msg,errormsg):
    print(msg,errormsg)
    sys.exit(1)

mydict = {
    # '1': 1,
    # '0b1': 0b1,
    # '0o1': 0o1,
    # '0x1': 0x1,
    # 'int(\'f\',16)': int('f',16),
    # 'hex(int(\'17\',8))': hex(int('17',8)),
    # '231': 231,
    '0xe7': 0xe7,
    'b\'\\xe7\'': b'\xe7',
    '\'\\xe7\'': '\xe7',
    'b\'\\xc3\\xa7\'': b'\xc3\xa7',
    'xe7': 'xe7',
    'b\'xe7\'': b'xe7',
    
}




if __name__ == "__main__":
    tb = pt.PrettyTable()
    tb.field_names= ["Expression", "Value", "Bytes_value", "Bytes_hex()", "Binary_value","Type", "Memort address", "Memory size"]
    bytes_value = {}
    for i in mydict:
        if isinstance(mydict[i], bytes):
            bytes_value[i] = mydict[i]
        elif isinstance(mydict[i], str):
            bytes_value[i] = bytes(mydict[i], encoding='utf-8')
        else:
            # note：  bytes(int) -> bytes object of size given by the parameter initialized with null bytes
            # convert int to bytes, use bytes([int])
            bytes_value[i] = bytes([mydict[i]]) 


    binary_value = {}
    for i in mydict:
        binary_value[i] = "{:08b}".format(int(bytes_value[i].hex(),16))

    for i in mydict:
        tb.add_row([i, mydict[i], bytes_value[i], bytes_value[i].hex(),binary_value[i], type(mydict[i]), id(mydict[i]), sys.getsizeof(mydict[i])])

    print(tb)