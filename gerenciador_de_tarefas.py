# Gerenciador de Tarefas

# Função para adicionar tarefa
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return


# Função para consultar tarefas
def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["completada"] == True else " "
        nome_tarefa = tarefa['tarefa']
        print(f"{idx}. [{status}] {nome_tarefa}")


# Função para atualizar tarefa
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}!")
    return


# Função para finalizar as tarefas
def completar_tarefas(tarefas, indice_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    return


# Função para deletar tarefas finalizadas
def deletar_tarefas_finalizadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas finalizadas deletadas com sucesso!")
    return


# main
tarefas = []
while True:
    print("\n Menu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefas")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
        if indice_tarefa - 1 >= 0 and indice_tarefa - 1 < len(tarefas):
            novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
            atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
        else:
            print("Insira um índice válido!")

    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
        if indice_tarefa - 1 >= 0 and indice_tarefa - 1 < len(tarefas):
            completar_tarefas(tarefas, indice_tarefa)
        else:
            print("Insira um índice válido!")

    elif escolha == "5":
        deletar_tarefas_finalizadas(tarefas)

    elif escolha == "6":
        print("Programa finalizado!")
        break
