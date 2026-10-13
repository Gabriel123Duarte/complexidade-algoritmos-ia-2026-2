def insertion_sort(lista):
  n = len(lista)
  
  for i in range(1, n): 
    atual = lista[i]
    j = i-1
    
    while j >= 0 and lista[j] > atual:
      lista[j+1] = lista[j]
      j -= 1
    
    lista[j+1] = atual
    print("Passada", i+1, ":", lista)
  



numeros = [5, 3, 8, 4, 2]
print("Lista desordenada:", numeros)
insertion_sort(numeros)
print("Lista ordenada:", numeros)