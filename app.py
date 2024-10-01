tarefas = []
# Loop 
while True:
    # tratamento de exceção
    try:
        # usuário cadastra nova tarefa
        nova_tarefa = input("Cadastre uma nova tarefa ou 'Enter' para exibir as tarefas cadastradas: ")

        if nova_tarefa:
            tarefas.append(nova_tarefa)
            print("Nova tarefa cadastrada com sucesso!")
        else:
            break

    except Exception as e:
        print(f"Não foi possível cadastrar nova tarefa. {e}.")

# Saindo do laço de repetição
for tarefa in tarefas:
    print(tarefa)
    
