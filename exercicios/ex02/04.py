'''4. Faça um programa para a leitura de duas notas parciais de um aluno. O
programa deve calcular a média alcançada por aluno e apresentar:

A mensagem &quot;Aprovado&quot;, se a média alcançada for maior ou igual a
sete;
A mensagem &quot;Reprovado&quot;, se a média for menor do que sete;
A mensagem &quot;Aprovado com Distinção&quot;, se a média for igual a dez.'''

nota1 = float(input("Digite a primera nota:"))
nota2 = float(input("Digite a seginda nota:"))
media = (nota1 + nota2) / 2

if media == 10:
    print(f"Sua media foi: {media} Aprovado com Distincao!")
elif media >= 7:
    print(f"Sua media foi: {media}, Aprovado!") 
else:
    print(f"Sua media foi: {media}, Reprovado!")

       