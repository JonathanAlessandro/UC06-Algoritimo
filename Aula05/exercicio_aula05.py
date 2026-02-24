while True:
    print("O que deseja fazer:")
    print("Para par ou impar digite 1")
    print("Para tabuada digite 2")
    print("para Sair digite 3")

    opc_escolhida = input("Digite a opção da preferencia: ")

    if opc_escolhida == "2":
        while True:
            numero_usuario = input("Digite o numero que deseja saber a taboada: ")
            if numero_usuario.isdigit():
                for i in range(11):
                    numero_usuario = int(numero_usuario)
                    resultado= numero_usuario*i
                    print(f"{numero_usuario} x {i} = {resultado}")
                break
            elif not numero_usuario.isdigit():
                print("O valor digitado precisa ser um numero inteiro!")
            else:
                break
    elif opc_escolhida == "1":
        while True:
            impar_par = input("Digite o numero que deseja descobrir: ")
            if impar_par.isdigit:
                impar_par = int(impar_par)
            if impar_par%2 == 0:
                print(f"O numero digitado foi {impar_par} e ele e par!")
                break
            elif impar_par%2 != 0:
                print(f"O numero digitado foi {impar_par} e ele e impar!")
                break
            else:
                print("Numero digitado e invalido!")
    elif opc_escolhida == "3":
        break