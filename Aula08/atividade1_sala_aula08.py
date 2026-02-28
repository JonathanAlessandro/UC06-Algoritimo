"""
crie uma lista vazia chamada compras
peça ao usuário para digitar 3 itens
Adicione cada item na lista
mostre todos os itens da lista ao final
"""

lista_compra= []
for i in range(3):
    lista_compra.append(input("Digite o item que deseja adicionar a sua lista de compras: "))
    
print(f"Sua lista de compras: {lista_compra}")


for compra in lista_compra:
    print("-",compra)