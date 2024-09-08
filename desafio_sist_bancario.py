"""
3 operações: depósito, saque e extrato
# ------ Depósito ------
Deve ser possível depositar valores positivos 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
Nesta versão, v1, vamos trabalhar com apenas 1 usuário
Não precisa se preocupar com número da agência e conta

------- Saque -------
Deve permitir até 3 saques diários
com limite máximo de R$500,00 por saque.
Caso não tenha saldo em conta, 
deve ser exibida uma mensagem informando que não será possível sacar por falta de saldo
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

------- Extrato --------
Deve listar todos os depósitos e saques da conta
No fim da listagem deve ser exibido o saldo atual da conta.
Se o extrato estiver em branco, exibir a mensagem: não foram realizadas movimentações
Os valores devem ser exibidos utilizando o formato R$ xxx.xx
"""

menu = """
------ Sistema Bancário ------
Digite a opção desejada: 
[d] depositar
[s] sacar
[e] ver extrato
[sair] sair
"""
saldo = 0
limite_saque = 500
extrato = ""
total_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        val_deposito = float(input("Informe o valor do depósito: "))

        if val_deposito > 0:
            saldo += val_deposito
            extrato += f"Depósito: R$ {val_deposito:.2f}\n"
            print(f"Foi depositado o valor: R${val_deposito:.2f}")
        else:
            print("OPERAÇÃO NÃO CONCLUÍDA! Informe um valor positivo.")

    elif opcao == "s":
        if total_saques >= LIMITE_SAQUES:
            print("Falha! Você não pode mais realizar saques hoje.")

        else:
            val_saque = float(input("O quanto deseja sacar? "))

            if val_saque > saldo:
                    print("Falha! O valor do saque é maior que o saldo.")
            elif val_saque > limite_saque:
                print("Falha! O valor do saque é maior que o limite de R$500.00")
            else:
                saldo -= val_saque
                total_saques += 1
                extrato += f"Saque: -R$ {val_saque:.2f}\n"
                print(f"Saldo atual: R$ {saldo:.2f}")
                print(f"Total saques restantes: {LIMITE_SAQUES-total_saques}")


    elif opcao == "e":
        print("\n------ Extrato ------")
        print("Não foram realizadas operações!" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("---------------------")

    elif opcao == "sair":
        break

    else:
        print("Informe uma opção válida.")


