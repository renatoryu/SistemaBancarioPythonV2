def menu():
    menu = '''
=============== SISTEMA BANCARIO ==================
[d] - Depositar
[s] - Sacar
[e] - Extrato
[u] - Novo usuário
[c] - Nova conta
[l] - Listar contas
[q] - Sair
===================================================
=> '''
    return input(menu)


def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("O valor informado é inválido, tente novamente!")
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
            
    else:
        if valor_saque >= limite:
            print("Saque não permitido, excedeu o limite!")
            
        elif valor_saque < limite:
                
            if valor_saque < saldo:
                print(f"Saldo restante: R${saldo-valor_saque:.2f}")
                saldo = saldo - valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1

            elif valor_saque > saldo:
                print("Não é possível sacar, saldo insuficiente!")

    return saldo, extrato, numero_saques

def exibirExtrato(saldo, /, *, extrato):
    print("\n------------------ EXTRATO -----------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("----------------------------------------------------")
           

def criarUsuario(usuarios):
    cpf = input("Digite seu CPF (somente número): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com o CPF informado!")
        return
    
    nome = input("Digite o nome completo: ")
    dataNascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, n° - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "dataNascimento": dataNascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

def criarContaCorrente(agencia, numeroConta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario}

    print("Usuário não encontrado, operação cancelada!")

def listarContas(contas):

    for conta in contas:
        linha = f'''
===================== CONTAS =======================
Agência: {conta['agencia']}
C/C: {conta['numeroConta']}
Titular: {conta['usuario']['nome']}
'''
        print(linha)
    print('''
====================================================
    ''')

def main():
    
    valor_saque = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
        print()

        if opcao == "d":
            valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Digite o valor que deseja sacar: R$"))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
                
        elif opcao == "e":
            exibirExtrato(saldo, extrato=extrato)

        elif opcao == "u":
            criarUsuario(usuarios)

        elif opcao == "c":
            numeroConta = len(contas) + 1
            conta = criarContaCorrente(AGENCIA, numeroConta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listarContas(contas)

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

main()
