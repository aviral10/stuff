def decimal_to_hexadecimal(dec):
    decimal = int(dec)
    return hex(decimal)


def hexadecimal_to_decimal(val):
    res = int(val, 16)
    return res


def find(arr):
    str_conv = ""
    if arr[0] < 4:
        if arr[0] == 0:
            str_conv += "H"
        else:
            str_conv += lower_bits[arr[0]]
    else:
        str_conv += upper_bits[arr[0]]
    if arr[1] == 0:
        str_conv += "O"
    else:
        str_conv += lower_bits[arr[1]]
    return str_conv


lower_bits = {0: 'O', 1 : 'A', 2: 'E', 3 : 'I'}
upper_bits = {0 : 'H', 4: 'B', 8: 'K', 12: 'D'}


def find_equi(num):
    arr = []
    final = ""
    hexa = decimal_to_hexadecimal(num)
    hexa = str(hexa)
    print("Hexa: ", hexa)
    for ele in hexa[2:]:
        arr = []
        conv = hexadecimal_to_decimal(ele)
        if conv % 4 == 0:
            arr.append(conv)
            arr.append(0)
        else:
            arr.append((conv//4)*4)
            arr.append(conv % 4)
        print(f"Conversion of {ele}: {arr}")
        final += find(arr)
    return final


aa = ["156", "16", "17"]
for ele in aa:
    print(f"Num: {ele}")
    print("bi-bi-binary: ",find_equi(ele))
