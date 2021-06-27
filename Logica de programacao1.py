# Fundamentos de Lógica de Programação com Python

## Tipo Inteiro
"""

type(1)

a=input('')
a

1 + 2

5 - 3

6 * 7

43 % 6

43 // 6

43 / 6

2 ** 63 -1

9_223_372_036_854_775_807

2 ** 1000

"""## Tipo Ponto Flutuante"""

type(7.166666666666667)

7.5 + 5, 5.5 - 7, 7.2 * 2, 2.1 ** 2, 7.3 / 2

"""## Variáveis"""

pi = 3.1415
raio = 2
pi * (raio ** 2)

raio = 1
pi * (raio ** 2)

nao_existe

"""## Cadeia de Caracteres (String)"""

print('Olá Mundo')

type('Renzo'), type("Renzo"), type("""Renzo"""), type('''Renzo''')

nome = """Renzo's "name" """
nome

nome = '''Renzo 
 Nuccitelli'''
print(nome)

"""## Tipos Booleanos"""

True, False, type(True), type(False)

not True, not False

True and True, True and False, False and True, False and False

True or True, True or False, False or True, False or False

5 < 6, 5 >= 6, 5 == 4, 5 == 5, 5 != 4,  5 != 5, 'Renzo' == 'Renzo'

renzo = 'Renzo'
renzo == 'renzo'

"""## Desvios Lógicos"""

idade = 65

if idade < 18:
  print(f'menor de idade: {idade}')
  print('Acabou o if')
elif idade >= 65:
  print(f'pessoa idosa: {idade}')
else:
  print(f'maior de idade: {idade}')

"""## Funções

"""

def classificar(idade, nome):
  if idade < 18:
    return f'{nome} é menor de idade: {idade}'
  elif idade >= 65:
    return f'{nome} é um isodo(a): {idade}'
  else:
    return f'{nome} é maior de idade: {idade}'

classificar(38, 'Renzo'), classificar(150, 'Matusalem')

"""## Sequencias

"""

lista = [1, 4.5, True, []]
type(lista), lista

"""### Acesso a elementos"""

lista[0], lista[1]

len(lista)

lista[-1], lista[-2]

"""### Fatiamento"""

lista

lista[1:3], lista[0:3], lista[:3], lista[2: len(lista)], lista[2: ]

lista[:]

numeros = list(range(1, 11))
numeros, numeros[1: 7: 2]

list(range(1, 32, 2))

renzo= 'Renzo Nuccitelli'
renzo[0], renzo[:6]

"""## Adição e Remoção"""

dir(numeros)

help(numeros.pop)

numeros

numeros.pop()

numeros

numeros.append(10)

numeros

numeros.extend([11, 12])

numeros

[1, 3] + [2, 4]

[1, 3] * 3

'Renzo ' + 'Nuccitelli'

'bla ' * 3

"""## Laços de Repetição"""

idades = [17, 38, 70, 80]
classificar(idades[0], 'Renzo'), classificar(idades[1], 'Renzo'), classificar(idades[2], 'Renzo')

for idade in idades:
  print(classificar(idade, 'Pessoa'))

"""## Dicionário"""

linguas = {'pt': 'Portugues', 'en': 'Inglês'}
linguas['pt'], linguas['en']

linguas['es'] = 'Espanhol'
linguas

for chave in linguas.keys():
  print(chave)

for valor in linguas.values():
  print(valor)

for chave, valor in linguas.items():
  print(chave, valor)

# Commented out IPython magic to ensure Python compatibility.
# %ls

with open('sample_data/ips.txt', 'r') as ips:
  for ip in ips:
    print(ip.strip())

with open('sample_data/saida.txt', 'w') as out:
  out.write('x')