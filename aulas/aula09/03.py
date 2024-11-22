#TESTES UNITARIOS ERRO DE SEMANTICA  

def soma_2(numero):
     return numero * 2

test1 = soma_2(2) == 4
test2 = soma_2(5) == 7

msg1 = 'sucesso' if test1 else 'falha'
msg2 = 'sucesso' if test2 else 'falha'

print(f'Resultado do teste: {msg1}')
print(f'Resultado do teste: {msg2}')
