a, b = 0, 1
while b < 100:
  print(b, end=',')
  a, b = b, a+b
  print("\na = ",a)
  print("\nb = ",b)
  print("\na+b = ",a+b)