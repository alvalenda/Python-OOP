from random import sample

correto = perfeito = tentativas = 0
numero = sample(range(10), 4)
# print(numero)
while True:
    palpite = str(input('Dê um palpite: ')).strip()
    tentativas += 1

    for i, pal in enumerate(palpite):
        if int(pal) in numero:
            if int(pal) == numero[i]:
                perfeito += 1
            else:
                correto += 1

    print(f'Corretos:  {correto}\nPerfeitos: {perfeito}')
    if perfeito == 4:
        print(f'=' * 40 + '\n' + f'PARABÉNS!!!'.center(40) + '\n' + f'=' * 40)
        break
    else:
        print(f'=' * 40)
        perfeito = correto = 0
print(f'Você venceu após {tentativas} palpites!'.center(40))
