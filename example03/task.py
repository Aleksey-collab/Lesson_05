# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
def encode(string):
    count = 1
    word = string[0]
    res = []
    for i in range(len(string) - 1):
        if word == string[i + 1]:
            count += 1
        else:
            res.append(f'{string[i]}{count}')
            word = string[i + 1]
            count = 1
    res.append(f'{word}{count}')
    return ''.join(res)


def decode(string):
    res = []
    tmp = ''
    for i in range(len(string)-2):
        d = 0
        tmp = ''
        if string[i].isalpha():

            if string[i+1].isdigit() and string[i+2].isdigit():
                tmp += (string[i+1] + string[i+2])
            elif string[i+1].isdigit():
                tmp += string[i+1]

            d = int(tmp)
            res.append(string[i]*d)

        elif string[-2].isalpha() and len(string)-1 == i+2:
            if string[i+2].isdigit():
                tmp += (string[i+2])

            d = int(tmp)
            res.append(string[i+1]*d)

    return ''.join(res)

with open('new1.txt', 'r')as file:
    s = file.readline()

print(s)
encode_file = encode(s)

print(encode_file)
with open('decode.txt', 'w')as file:
    file.write(decode(encode_file))

with open('decode.txt', 'r')as file:
    s = file.readline()
print(s)