def producto(n):
  if n == 0:
    return 1
  else:
    return n*producto(n-1)

print(producto(4))
