nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    print('Informe a primeira nota: ')
    print('Informe a segunda nota: ')
    print('Informe a terceira nota: ')
    print('Aprovado com media: %.1f ' % media)
elif media >= 5.0 and media < 7.0:
    print('Recuperacao com media: %f' % media)
elif media < 5.0:
    print('Reprovado com media: %.1f' % media)
