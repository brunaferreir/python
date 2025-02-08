def adicionarCarrinho(carrinho, produto):
    if produto not in carrinho:
        carrinho.append(produto)

carrinho = []

r = "S"
while r == 'S':
    try:
        produto = str(input('Adicione o produto no carrinho: '))
        adicionarCarrinho(carrinho, produto)
    except ValueError:  
         print("Entrada inválida. Digite um produto valido.")  

    r = str(input('Quer continuar? [S/N]')).upper()

print(f'Seus produtos adicionados: {carrinho}')
print('FIM')
    
