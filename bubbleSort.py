def bubble_sort(lista):
  n = len(lista)
  
  for i in range(n): 
    trocou = False
    for j in range(n-1): 
      if lista[j] > lista[j+1]:
        
        antigo = lista[j]
        lista[j] = lista[j+1]         
        lista[j+1] = antigo
        # swap
        # lista[j], lista[j+1] = lista[j+1], lista[j]
        trocou = True
      
    print("Passada", i+1, ":", lista)
    if not trocou: 
      break



numeros = [5, 3, 8, 4, 2]
print("Lista desordenada:", numeros)
bubble_sort(numeros)
print("Lista ordenada:", numeros)

