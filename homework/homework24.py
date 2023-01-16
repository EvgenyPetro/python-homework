# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def rle_encode(data):
    count = 0
    pointer = data[0]
    new_str = []
    for i in range(len(data)):
        if pointer == data[i]:
            count += 1
        else:
            new_str.append(str(count))
            new_str.append(pointer)
            count = 1
            pointer = data[i]
    new_str.append(str(count))
    new_str.append(pointer)
    return "".join(new_str)


def rle_decode(data):
    int_arr = []
    str_arr = []
    new_str = []
    for i in range(len(data)):
        if i % 2 == 0:
            int_arr.append(int(data[i]))
        else:
            str_arr.append(data[i])

    for i in range(len(int_arr)):
        new_str.append(str_arr[i] * int_arr[i])
    return "".join(new_str)


with  open("decode.txt") as decode:
    decode_str = decode.read().strip()
    print(rle_encode(decode_str))

with  open("encode.txt") as encode:
    encode_str = encode.read().strip()
    print(rle_decode(encode_str))


