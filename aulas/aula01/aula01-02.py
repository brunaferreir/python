# 2. Determinar se um ano fornecido pelo usuário é bissexto ou não
# Lembre-se que um ano é bissexto se for divisível por 4 e, se for divisível por 100, deve ser também divisível #por 400.

ano = int(input("Digite o ano: "))
if ano %4 == 0 or ano %100 == 0 and ano %400 == 0:
    print(f'{ano} é um ano biissexto.')
else:
    print(f'{ano} não é um ano bissexto.')    



