from uteis.dado import leia_str


def arabico_romano(nume):
    lista = []
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabico = [1000, 900,  500, 400, 100,  90,  50,   40,   10,   9,   5,   4,    1]
    for numero, romano in zip(arabico, romanos):
        while nume - numero >= 0:
            lista.append(romano)
            nume -= numero
    return ''.join(lista)


def romano_arabico(nume):
    romanos = ['CM', 'M', 'CD', 'D', 'XC', 'C', 'XL', 'L', 'IX', 'X', 'IV', 'V', 'I']
    arabico = [900, 1000,  400, 500,  90,  100,  40,   50,   9,  10,    4,   5,   1]
    acumula_num = int(0)
    for romano, numero in zip(romanos, arabico):
        while romano in nume:
            acumula_num += numero
            doidera = nume.split(romano, 1)
            nume = ''.join(doidera)
    if num_b in arabico_romano(acumula_num):
        return acumula_num
    else:
        return False


num = leia_str('Número Arábico ou Romano: ', 1)
num_b = num
if num.isnumeric():
    num = int(num)
    print(f'{num_b} --> {(arabico_romano(num))}')
elif num.isalpha():
    if romano_arabico(num):
        print(f'{num_b} --> {(romano_arabico(num))}')
    else:
        print(f'--> {num_b} <-- NÃO É COMPOSTO APENAS POR ALGARISMOS ROMANOS')
else:
    print(f'--> {num_b} <-- NÃO É UM VALOR VÁLIDO')
