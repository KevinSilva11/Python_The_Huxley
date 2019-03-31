escolha = int(input())
num2 = float(input())
num3 = float(input())

mul = num2 * num3
div = num2 / num3
sub = num2 - num3
adi = num2 + num3

if escolha == 3:
    print('1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao')
    print('A multiplicacao eh: %.2f' % mul)
elif escolha == 4:
    print('1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao')
    print('A divisao eh: %.2f' % div)
elif escolha == 2:
    print('1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao')
    print('A subtracao eh: %.2f' % sub)
else:
    if escolha == 1:
        print('1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao')
        print('A adicao eh: %.2f' % adi)
