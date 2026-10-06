def busca_binaria(lista, valor):
  inicio = 0
  fim = len(lista)-1
  
  while inicio <= fim: 
    meio = (inicio+fim) // 2
    
    print("Inicio: ", inicio, "| Meio: ", meio, "| Fim: ", fim, "| Valor: ", lista[meio])
    
    if lista[meio] == valor:
      return meio
    elif valor < lista[meio]:
      fim = meio-1
    elif valor > lista[meio]:
      inicio = meio+1
  
  return -1


numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]


print("Buscando 70:")

resultado = busca_binaria(numeros, 70)

print("Posição:", resultado)


print("\nBuscando 35:")

resultado = busca_binaria(numeros, 35)

print("Posição:", resultado)