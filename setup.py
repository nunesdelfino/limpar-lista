import csv

ARQUIVO1 = "Arquivo1"
ARQUIVO2 = "Arquivos2"

NOMEARQUIVO = "Lista"


def lerArquivo(arquivo):
    lista = []
    with open(arquivo + ".csv", 'r') as conteudo:
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

def main():

    listaPrincipal = lerArquivo(ARQUIVO1)
    listaSecundaria = lerArquivo(ARQUIVO2)

    listaLimpa = removeItens(listaPrincipal, listaSecundaria)

    listaLimpa.sort()

    criaLista(listaLimpa, NOMEARQUIVO)

    

if __name__ == "__main__":
    main()