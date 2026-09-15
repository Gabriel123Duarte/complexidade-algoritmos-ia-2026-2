def fatorial_recursivo(n):
  print("Entrando:", n)
  if n <= 1:
    print("Caso-base:", n)
    return 1
  
  resposta = n * fatorial_recursivo(n-1)
  print("Retornando:", n, "->", resposta);
  
  
  return resposta

print(fatorial_recursivo(6))


