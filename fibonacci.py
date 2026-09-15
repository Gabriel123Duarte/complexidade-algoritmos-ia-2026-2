# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
# fib(n) = fib(n-1) + fib(n-2)
# fib(0) = 0
# fib(1) = 1

chamadas = 0

def fibonacci(n):
  global chamadas
  
  chamadas += 1
  
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
  chamadas = 0
  resultado = fibonacci(n)
  
  print("n = ", n, " resultado = ", resultado, " chamadas = ", chamadas)

# 2^n