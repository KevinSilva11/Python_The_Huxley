a = int(input())
b = int(input())
c = int(input())

if a==b and b==c:
   print("nao")

if a>=b+c or b>=c+a or c>=a+b:
   print("nao")

if a<=0 or b<=0 or c<=0:
   print("nao")

elif a==b or b==c or c==a:
   print("nao")

else:
   print("sim")
