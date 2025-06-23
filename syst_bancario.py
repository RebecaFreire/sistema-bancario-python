CAMINHO_EXTRATO = "extrato.txt"

def salvar_extrato(movimento):
    with open(CAMINHO_EXTRATO, "a", encoding="utf-8") as f:
        f.write(movimento + "\n")

def depositar(saldo, extrato):
    entrada = input("Informe o valor do depósito: ").strip()
    if entrada.replace(',', '').replace('.', '').isdigit():
        valor = float(entrada.replace(',', '.'))
        if valor > 0:
            saldo += valor
            movimento = f"Depósito: R$ {valor:.2f}"
            extrato += movimento + "\n"
            salvar_extrato(movimento)
        else:
            print("A operação falhou! O valor informado deve ser positivo.")
    else:
        print("Operação falhou! Digite um valor numérico válido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    entrada = input("Informe o valor do saque: ").strip()
    if entrada.replace(',', '').replace('.', '').isdigit():
        valor = float(entrada.replace(',', '.'))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            movimento = f"Saque: R$ {valor:.2f}"
            extrato += movimento + "\n"
            numero_saques += 1
            salvar_extrato(movimento)
        else:
            print("Operação falhou! O valor informado deve ser positivo.")
    else:
        print("Operação falhou! Digite um valor numérico válido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========= EXTRATO =========")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===========================")

# ------------------------------
# Programa principal (main)
# ------------------------------
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, numero_saques, limite, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Saindo do sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
