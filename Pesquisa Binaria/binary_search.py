# 'cut' a list in half every guess you make...
def pesquisa_binaria(lista, item):
    lowerL = 0
    upperL = len(lista)-1
    i = 0
    
    while lowerL <= upperL:
        i += 1
        meio = int((lowerL + upperL) / 2)
        chute = lista[meio]
        if chute == item:
            print('int:',i)
            return meio
        if chute > item:
            upperL = meio - 1
        else:
            lowerL = meio + 1
    print('int:',i)
    return None


numeros = [k*k for k in range(1,10001)]

ind = pesquisa_binaria(numeros, 93779856)

try:
    print(numeros[ind], 'in', ind)
except TypeError:
    print(numeros[ind], "not found")
