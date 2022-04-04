import csv
import sys


def lerArquivo(arquivo):
    lista = []
    with open(arquivo, 'r') as conteudo:
        leitor = csv.reader(conteudo)
        for item in leitor:
            lista.append(item)
    return lista

def removeItens(listaP, listaS):
    for item in listaS:
        for item2 in listaP:
            if(item == item2):
                listaP.remove(item)
    return listaP

def criaLista(lista, nome):
    with open(nome + ".csv", 'w', newline='', encoding="utf8") as csvfile:
        escrever = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        for x in lista:
            escrever.writerow(x)
    
    print("Arquivo " + nome + ".csv criado com sucesso")

def mensagemAjuda():
    print("Por favor, informe o nome dos arquivos:")
    print("Exemplo: setup.py NomeArquivo01.csv NomeArquivo02.csv ArquivoFinal")
    print("Arquivo 01 - Lista completa a ser limpa")
    print("Arquivo 02 - Lista dos itens a serem removidos da lista completa 'Arquivo 01'")
    print("Arquivo Final - Nome do arquivo de saída")

def validaParametros():
    if(len(sys.argv) != 4):
        mensagemAjuda()
        exit()

def obtemNomeDoArquivo(Index):
    return sys.argv[Index]

def main():

    validaParametros()

    Arquivo01 = obtemNomeDoArquivo(1)
    Arquivo02 = obtemNomeDoArquivo(2)
    NomeArquivo = obtemNomeDoArquivo(3)

    listaPrincipal = lerArquivo(Arquivo01)
    listaSecundaria = lerArquivo(Arquivo02)

    listaLimpa = removeItens(listaPrincipal, listaSecundaria)

    listaLimpa.sort()

    criaLista(listaLimpa, NomeArquivo)

    

if __name__ == "__main__":
    main()
