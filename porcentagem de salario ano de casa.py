sexo=input()
anocasa=int(input())
salario=float(input())

if sexo == 'h' or sexo == 'm':
    if sexo =='h' and anocasa > 15:
        print('%.2f'% (salario *1.20))
    else:
        if sexo =='m' and anocasa > 10:
            print('%.2f'%(salario *1.25))
        else:
            print('%.2f'%(salario+200))
