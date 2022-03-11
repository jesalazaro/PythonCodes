def prestamo(n, m=1000000):
  if n==0:
    return m
  else:
    return prestamo(n-1,m*1.05)

print(prestamo(12))
