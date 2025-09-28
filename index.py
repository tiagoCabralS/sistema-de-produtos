# Sistema para guardar itens de supermercado/coisas assim
import json
from time import sleep
"""
itens = [
    ['ovo', 15]
]

with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sistema\\index.json', 'w', encoding='utf8') as arquivo:
    json.dump(itens, arquivo, indent=2, ensure_ascii=False)
"""


def guardar(item, preco=0):
    with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sistema\\index.json', 'r') as arquivo:
        itens = json.load(arquivo)

        itens.append([item, preco])
    
    with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sistema\\index.json', 'w', encoding='utf8') as arquivo:
        json.dump(itens, arquivo, indent=2)
        
        
def remover(indice):
    with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sistema\\index.json', 'r', encoding='utf8') as arquivo:
        itens = json.load(arquivo)
    
    del(itens[indice-1])
    
    with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sistema\\index.json', 'w', encoding='utf8') as arquivo:
        json.dump(itens, arquivo, indent=2)
    
    print('Item removido com sucesso!')
  
    
def listar():
    with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sistema\\index.json', 'r') as arquivo:
        itens = json.load(arquivo)
        
        contagem = 0
        for item, preco in itens:
            contagem += 1
            print(f'{contagem}: {item}-R${preco}')


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
    try:
        opcao = int(opcao)
        if opcao == 1:
            linha(25, '-')
            name = str(input('Nome do item a ser guardado: '))
            price = float(input('Preço: R$'))
            guardar(name, price)
            linha(25, '-')
            print(f'{name}, custando R${price:.2f}, foi adicionado(a) com sucesso!')
            sleep(1)
        elif opcao == 2:
            cabecalho('itens')
            listar()
            ind = int(input('Número do item a ser removido: '))
            remover(ind)
            sleep(1)
        elif opcao == 3:
            cabecalho('itens')
            listar()
            sleep(1)
        else:
            break
            
    except:
        break
    sleep(1)

linha(25, '-')
print('Fechando sistema. Até logo!')
sleep(1)
