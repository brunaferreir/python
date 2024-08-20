# Exercício 02
# Preencha um dicionário com os dados de 5 alunos
# - Utilize o ra do aluno como chave e uma lista de três notas como valor.
# - Solicite os dados do usuário
# - Percorra o dicionário e exiba a média de cada aluno.
# Exemplo:
# Veja um exemplo da estrutura do dicionário.
# {19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]}

dados = {}

while len(dados) < 5:
    notas = []
    ra = float(input("Insira o RA: "))
    for i in range(3):
        nota = float(input("Insira a nota: "))
        notas.append(nota)
        dados[ra] = notas

for chave, valor in dados.items():
    print(f'RA: {chave}')
    print(f'Notas: {valor}')
    print(f'Média: {(sum(valor))/len(valor):.2f}')