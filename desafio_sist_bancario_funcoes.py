import datetime
import textwrap

"""
Criar duas novas funções: usuário (cliente do banco) e criar conta corrente (vincular com usuário)
criar funções para as operações
"""
data_hora = datetime.datetime.now()

def menu():
    menu = """
    ------ Sistema Bancário ------
    Digite a opção desejada: 
    [d] depositar
    [s] sacar
    [e] ver extrato
    
    [u] criar usuário
    [c] criar conta
    [l] listar contas
    
    [sair] sair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato, /):
    if total_operacoes >= MAX_OPERACOES:
        print("Você não pode mais fazer depósitos e saques hoje.")
    else:
        val_deposito = float(input("Informe o valor do depósito: "))
        if val_deposito < 0:
            print("OPERAÇÃO NÃO CONCLUÍDA! Informe um valor positivo.")
        else:
            saldo += val_deposito
            total_operacoes += 1
            extrato += data_hora.strftime("%d/%m/%Y %H:%M - ") + f"Depósito: R$ {val_deposito:.2f}\n"
            print(f"Foi depositado o valor: R${val_deposito:.2f}")

    return saldo,extrato

def sacar(*, saldo,valor_saque,extrato,valor_max_saque,total_saques,max_saques):
    if total_saques >= MAX_SAQUES:
        print("Falha! Você não pode mais realizar saques hoje.")
    elif total_operacoes >= LIMITE_OPERACOES:
        print("Você não pode mais fazer depósitos e saques hoje.")
    else:
        valor_saque = float(input("O quanto deseja sacar? "))

        if valor_saque > saldo:
            print("Falha! O valor do saque é maior que o saldo.")
        elif valor_saque > valor_max_saque:
            print("Falha! O valor do saque é maior que o limite de R$500.00")
        else:
            saldo -= valor_saque
            total_saques += 1
            total_operacoes += 1
            extrato += data_hora.strftime("%d/%m/%Y %H:%M - ") + f"Saque: -R$ {valOR_saque:.2f}\n"
            print(f"Saldo atual: R$ {saldo:.2f}")
            print(f"Total saques restantes: {MAX_SAQUES - total_saques}")

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n------ Extrato ------")
    print("Não foram realizadas operações!" if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("---------------------")

def criar_usuario(usuarios):
    cpf = input("Informe seu cpf (somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
        print("\n FALHA!  Já existe um usuario com este cpf!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("*** Usuario cadastrado com sucesso! ***")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia,numero_conta,usuario):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    else:
        print("\n FALHA! Usuário não encontrado, fluxo de criação de conta encerrado!")
        return None
def listar_contas():
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print( "=" * 100)
        print(textwrap.dedent(linha))


def main():
    saldo = 0
    valor_max_saque = 500
    extrato = ""
    total_saques = 0
    total_operacoes = 0
    MAX_SAQUES = 3
    MAX_OPERACOES = 10
    AGENCIA = "0001"
    numero_conta = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor_deposito = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                valor_max_saque = valor_max_saque,
                total_saques = total_saques,
                max_saques = MAX_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "sair":
            break

        else:
            print("Informe uma opção válida.")

main()

