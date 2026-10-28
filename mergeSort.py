# [5, 6] -  []
# [1, 2, 3, ]

def combinar(esquerda, direita):
  resposta = []
  
  i = 0
  j = 0
  
  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      resposta.append(esquerda[i])
      i += 1
    else:
      resposta.append(direita[j])
      j += 1
  
  resposta.extend(esquerda[i:])
  # for x in range(i, len(esquerda)):
  #   resposta.append(esquerda[x])
    
  resposta.extend(direita[j:])
  
  return resposta

def mergeSort(lista):
  if len(lista) <= 1:
    return lista 
  
  meio = len(lista) // 2
  
  esquerda = lista[:meio]
  direita = lista[meio:]
  
  esquerda = mergeSort(esquerda)
  direita = mergeSort(direita)
  
  resposta = combinar(esquerda, direita)
  
  return resposta

# Testando o algoritmo
numeros = [8, 3, 5, 1, 7, 2]

print("Lista original:", numeros)

ordenada = mergeSort(numeros)

print("Lista ordenada:", ordenada)