tarefas = [
    "Estudar Python",
    "Fazer compras",
    "Ir à academia"
]

opcao = 0

while opcao != 4:
    print("====== MENU ======")
    print()
    print("1 - Adicionar uma tarefa")
    print("2 - Listar todas as tarefas cadastradas.")
    print("3 - Remover uma tarefa.")
    print("4 - Encerrar o programa.")
    print()

    opcao = int(input("Digite uma opção: "))
    print()

    if opcao == 1:
        tarefa = input("Digite a tarefa que você deseja adicionar: ")
        tarefas.append(tarefa)
        print("\nTarefa adicionada com sucesso!")
        print()

    elif opcao == 2:
        for i in range(len(tarefas)):
            print(f"{i + 1} - {tarefas[i]}")
        print()

    elif opcao == 3:
        if len(tarefas) == 0:
            print("Não há tarefas para remover.\n")
        else:
            contador = 1

            for tarefa in tarefas:
                print(f"{contador} - {tarefa}")
                contador += 1

            print()
            pergunta = int(input("Digite o número da tarefa que deseja remover: "))

            indice = pergunta - 1

            if 0 <= indice < len(tarefas):
                item_removido = tarefas.pop(indice)
                print(f'A tarefa "{item_removido}" foi removida com sucesso!\n')
            else:
                print("Número de tarefa inválido.\n")

    elif opcao == 4:
        print("Saindo do sistema...")
