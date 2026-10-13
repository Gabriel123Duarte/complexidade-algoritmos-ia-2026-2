def selection_sort(lista):
  n = len(lista)
  
  for i in range(n-1):
    indice_menor = i 
    
    for j in range(i+1, n):
      if lista[j] < lista[indice_menor]:
        indice_menor = j
        
    antigo = lista[i]
    lista[i] = lista[indice_menor]         
    lista[indice_menor] = antigo
  
    print("Passada", i+1, ":", lista)


numeros = [5, 3, 8, 4, 2]
print("Lista desordenada:", numeros)
selection_sort(numeros)
print("Lista ordenada:", numeros)