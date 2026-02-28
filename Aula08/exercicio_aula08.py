lista_nomes= ["Alan","Samuel","Samira","Miriam"]
print(lista_nomes)

nome = input("Digite o nome que deseja excluir: ")

for i in lista_nomes:
    
    if  lista_nomes.count(nome)>= 1:
        lista_nomes.remove(nome)
        print(f"O nome desejado foi excluido {lista_nomes}")
        break
    else:
        print("Nome não encontrado!")
        break

