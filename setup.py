import csv

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

def main():

    arquivo1 = "Lista 01.csv"
    arquivo2 = "Lista 02.csv"

    nomeArquivo = "Lista"

    listaPrincipal = lerArquivo(arquivo1)
    listaSecundaria = lerArquivo(arquivo2)

    listaLimpa = removeItens(listaPrincipal, listaSecundaria)

    listaLimpa.sort()

    criaLista(listaLimpa, nomeArquivo)

    

if __name__ == "__main__":
    main()