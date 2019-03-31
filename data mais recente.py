data = input()
data2 = input()
partes1 = data.split()
partes2 = data2.split()
num1 = int(partes1[0])
num2 = int(partes1[1])
num3 = int(partes1[2])
num4 = int(partes2[0])
num5 = int(partes2[1])
num6 = int(partes2[2])
if num3 > num6 or num2 > num5 or num1 > num4:
    print(data)
else:
    print(data2)
