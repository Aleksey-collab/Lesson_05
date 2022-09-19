# 4. ДОП
# ШИФР ЮЛИЯ
# Юлий Цезарь использовал свой способ шифрования. Каждая буква заменялась на следующую по алфовиту через К позиций по кругу.
# Необходимо по заданой шифровке определить исходный текст. 
# Пример:
# XPSE
# 1
# Выход
# WORD


def decod_cesar_code(string, step):
    res = []
    for i in range(len(string)):
        if ord(string[i].lower()) - step < 97:
            x = (122 - (97 - (ord(string[i].lower()) - step))) + 1
            res.append(chr(x))
        else:
            x = ord(string[i].lower()) - step
            res.append(chr(x))
            print(res)
    return res

decod_cesar_code('XPSE', 1)