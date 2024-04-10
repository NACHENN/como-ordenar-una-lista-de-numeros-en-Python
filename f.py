def partList(list, n):
    print("Lista de números:")
    lower = []  
    upper = []  
    
    for numeros in list:
        if numeros < n:  
            lower.append(numeros)  
        else:
            upper.append(numeros)  
    
    return lower + upper  

lista = [3, 1, 4, 2, 5, 7, 6]
n = 3
resultado = partList(lista, n)
print(resultado)
print("Lista de números", n, ":")