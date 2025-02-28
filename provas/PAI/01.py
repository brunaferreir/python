preco_unitario = int(input("Digite o preco unitario:"))
qtd = int(input("Digite a quanntidade:"))
total = preco_unitario * qtd
if total > 100:
    desconto = total * 0.10
    print(f"O total com desconto é {total - desconto}")  

print(f"O total é {total}")  


