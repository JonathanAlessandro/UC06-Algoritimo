numero_01 = int(input("Digite um numero: "))
numero_02 = int(input("Digite um outro numero: "))
mes = int(input("Digite o mes que estamos lembrando que os meses vao de 1 a 12: "))
impar_par = int(input("Digite um numero inteiro agora para descobrirmos se ele e impar ou par: "))

if numero_01>numero_02:
    print(f"O maior numero e o {numero_01}")
elif numero_02> numero_01:
    print(f"O maior numero e o {numero_02}")
else:
    print("Os numeros são iguais")


if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Marco")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("O numero digitadoe e invalido por favor digite um numero de 1 a 12")

if impar_par%2 == 0:
    print(f"O numero digitado foi {impar_par} e ele e par")
else:
    print(f"O numero digitado foi {impar_par} e ele e impar")

