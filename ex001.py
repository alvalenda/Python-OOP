from uteis.dado import leia_str, leia_float


class Empregado:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome.lower() + '.' + sobrenome.lower() + '@empresa.com'

    def imprime_dados(self):
        return f'''Nome Completo: {self.nome[:15]} {self.sobrenome[:15]}
    E-mail.......: {self.email[:30]}
    Salário......: R$ {self.salario:.2f}'''


empregados = []

for index, empregado in enumerate(range(3), start=1):
    print(f"{f' {index}º FUNCIONÁRIO ':#^60}")
    nome_ = leia_str(f'NOME: ', 2)
    sobrenome_ = leia_str(f'SOBRENOME: ', 2)
    salario_ = leia_float(f'SALÁRIO R$: ')
    empregados.append(Empregado(nome_, sobrenome_, salario_))

# for index, empregado in enumerate(empregados, start=1):
#     print(f'{f" {index}º FUNCIONÁRIO CADASTRADO ":#^50}')
#     print(f'{empregado.imprime_dados()}')
#     print(f'#'*50)

meta = dict()
lista = [meta, empregados]
lista[0]['Metadados'] = 'Lista de Funcionários da empresaX'
lista[0]['Itens'] = len(lista[1])
print(lista[0])

for index, empregado in enumerate(lista[1], start=1):
    print(f'{f" {index}º FUNCIONÁRIO CADASTRADO ":#^60}')
    print(f'\t{empregado.imprime_dados()}')
print(f'#' * 60)
print(f'FIM!!!')
