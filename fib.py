def fibonaci(n):
  
  f= [0, 1]

  for i in range (2, n+1):
    f.append(f[i-1]+f[i-2])
  return f[n]
x=0
y= input("how many numbers?")
y = int(y)
while x < y:
  print(fibonaci(x))
  x+=1