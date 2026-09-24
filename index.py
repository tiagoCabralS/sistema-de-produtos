import json
import os
from time import sleep

caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.json')

if not os.path.exists(caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump([], arquivo)


def guardar(item, preco=0):
    with open(caminho, 'r', encoding='utf8') as arquivo:
        itens = json.load(arquivo)

    itens.append([item, preco])

    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(itens, arquivo, indent=2, ensure_ascii=False)


def remover(indice):
    with open(caminho, 'r', encoding='utf8') as arquivo:
        itens = json.load(arquivo)

    if indice < 1 or indice > len(itens):
        print('Número inválido!')
        return

    del itens[indice - 1]

    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(itens, arquivo, indent=2, ensure_ascii=False)

    print('Item removido com sucesso!')


def listar():
    with open(caminho, 'r', encoding='utf8') as arquivo:
        itens = json.load(arquivo)

    if not itens:
        print('Nenhum item guardado.')
        return

    for contagem, (item, preco) in enumerate(itens, start=1):
        preco = f'R${preco:.2f}'
        print(f'{contagem}: {item:-<12}{preco:->10}')


def linha(tamanho, caracter):
    print(f'{caracter}' * tamanho)


def cabecalho(palavra):
    linha(25, '-')
    print(f'{palavra.upper():^25}')
    linha(25, '-')


while True:
    cabecalho('sistema')
    print('1 - Guardar\n2 - Remover\n3 - Listar')
    opcao = input('Selecionar opção (digite qualquer tecla para sair): ')
    if opcao == '1':
        linha(25, '-')
        name = input('Nome do item a ser guardado: ')
        try:
            price = float(input('Preço: R$').replace(',', '.'))
        except ValueError:
            print('Preço inválido!')
            sleep(1)
            continue
        guardar(name, price)
        linha(25, '-')
        print(f'{name}, custando R${price:.2f}, foi adicionado(a) com sucesso!')
        sleep(1)
    elif opcao == '2':
        cabecalho('itens')
        listar()
        try:
            ind = int(input('Número do item a ser removido: '))
        except ValueError:
            print('Número inválido!')
            sleep(1)
            continue
        remover(ind)
        sleep(1)
    elif opcao == '3':
        cabecalho('itens')
        listar()
        sleep(1)
    else:
        break

    sleep(1)

linha(25, '-')
print('Fechando sistema. Até logo!')
sleep(1)