def adicionar_tarefa(tarefas, id_tarefa, descricao, prazo_final, urgencia):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Parâmetros:
    - tarefas (list): Lista que armazena as tarefas.
    - id_tarefa (int): ID único da tarefa.
    - descricao (str): Descrição da tarefa.
    - prazo_final (str): Data limite para conclusão da tarefa.
    - urgencia (str): Nível de urgência da tarefa (Baixa, Média, Alta).

    Retorno:
    - Nenhum
    """
    tarefa = {
        'ID': id_tarefa,
        'Descrição': descricao,
        'Data de Criação': "02/09/2024",
        'Status': 'Pendente',
        'Prazo Final': prazo_final,
        'Urgência': urgencia
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):
    """
    Lista todas as tarefas pendentes.

    Parâmetros:
    - tarefas (list): Lista que armazena as tarefas.

    Retorno:
    - Nenhum
    """
    if not tarefas:
        print("Nenhuma tarefa pendente.")
        return

    print("Lista de Tarefas Pendentes:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. ID: {tarefa['ID']}, Descrição: {tarefa['Descrição']}, Prazo Final: {tarefa['Prazo Final']}, Urgência: {tarefa['Urgência']}, Status: {tarefa['Status']}")


def marcar_como_concluida(tarefas, id_tarefa):
    """
    Marca uma tarefa específica como concluída.

    Parâmetros:
    - tarefas (list): Lista que armazena as tarefas.
    - id_tarefa (int): ID da tarefa a ser marcada como concluída.

    Retorno:
    - Nenhum
    """
    for tarefa in tarefas:
        if tarefa['ID'] == id_tarefa:
            tarefa['Status'] = 'Concluída'
            print("Tarefa marcada como concluída!")
            return
    print("Tarefa não encontrada.")


def remover_tarefa(tarefas, id_tarefa):
    """
    Remove uma tarefa específica da lista.

    Parâmetros:
    - tarefas (list): Lista que armazena as tarefas.
    - id_tarefa (int): ID da tarefa a ser removida.

    Retorno:
    - Nenhum
    """
    for tarefa in tarefas:
        if tarefa['ID'] == id_tarefa:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
            return
    print("Tarefa não encontrada.")


def menu():
    """
    Exibe o menu de opções e realiza as operações solicitadas pelo usuário.

    Parâmetros:
    - Nenhum

    Retorno:
    - Nenhum
    """
    tarefas = []
    id_contador = 1

    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            descricao = input("Digite a descrição da tarefa: ")
            prazo_final = input("Digite o prazo final da tarefa (DD/MM/AAAA): ")
            urgencia = input("Digite o nível de urgência (Baixa, Média, Alta): ")
            adicionar_tarefa(tarefas, id_contador, descricao, prazo_final, urgencia)
            id_contador += 1
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            id_tarefa = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
            marcar_como_concluida(tarefas, id_tarefa)
        elif opcao == '4':
            id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
            remover_tarefa(tarefas, id_tarefa)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
