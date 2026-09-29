def buscaLinear(lista, alvo):
  comparacoes = 0
  
  for i in range(len(lista)):
    comparacoes += 1
    if lista[i] == alvo:
      return i, comparacoes
  
  return -1, comparacoes


numeros = [17, 8, 25, 3, 41, 12, 30]

posicao, comparacoes = buscaLinear(numeros, 41)

print("Posição:", posicao)
print("Comparações:", comparacoes)

# melhor caso
posicao, comparacoes = buscaLinear(numeros, 17)

print("\nPosição melhor caso:", posicao)
print("Comparações melhor caso:", comparacoes)

# elemento no meio
posicao, comparacoes = buscaLinear(numeros, 3)

print("\nPosição elemento meio:", posicao)
print("Comparações elemento meio:", comparacoes)

# pior caso - ultima
posicao, comparacoes = buscaLinear(numeros, 30)

print("\nPosição pior caso:", posicao)
print("Comparações pior caso:", comparacoes)


# pior caso - inexistente
posicao, comparacoes = buscaLinear(numeros, 1)

print("\nPosição pior caso inexistente:", posicao)
print("Comparações pior caso inexistente:", comparacoes)

print("\nEscalando")
for n in [10, 100, 1000, 10000]:
  numeros = list(range(n))
  posicao, comparacoes = buscaLinear(numeros, -1)
  
  print("n =", n, "| comparações =", comparacoes)
  