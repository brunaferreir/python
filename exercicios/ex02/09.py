'''9. Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato de “D de mesPorExtenso de AAAA”.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.'''

def dada(data):
    dias = data.split('/')[0]
    mes = data.split('/')[1]
    ano = data.split('/')[2]
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    if int(dias) > 31 or int(dias) < 1 or int(mes) > 12 or int(mes) < 1:
        return 'NULL'
    else:
        return f'{dias} de {meses[int(mes)-1]} de {ano}'
    
data = "25/12/2023"
data_formatada = dada(data)
print(data_formatada)   