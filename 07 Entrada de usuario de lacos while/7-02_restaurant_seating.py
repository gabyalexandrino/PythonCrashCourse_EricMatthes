qtd_pessoas = input("Boa noite, quantas pessoas estão no seu grupo para jantar? ")
qtd_pessoas = int(qtd_pessoas)
if qtd_pessoas > 8:
    print(f"Quantidade de pessoas igual a {qtd_pessoas}, aguarde mais um pouco por uma mesa.")
else:
    print(f"Quantidade de pessoas igual a {qtd_pessoas}, sua mesa está pronta. Por favor, me acompanhe.")