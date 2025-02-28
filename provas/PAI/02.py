n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

m = n1
if n2 > m:
    m = n2

if n3 > m:
    m = n3

print(f"O maior numero é {m}")