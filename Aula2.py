from collections import deque

# Definindo a classe para um processo
class Process:
    def __init__(self, id, burst_time):
        self.id = id  # Identificador do processo
        self.burst_time = burst_time  # Tempo necessário para concluir o processo
        self.remaining_time = burst_time  # Tempo restante para completar o processo
        self.wait_time = 0  # Tempo de espera do processo
        self.turnaround_time = 0  # Tempo de turnaround (tempo total que o processo levou)

# Função para simular o algoritmo
def round_robin(processes, quantum):
    queue = deque(processes)  # Fila de processos
    time = 0  # Relógio da simulação

    while queue:
        process = queue.popleft()  # Pegando o processo da fila

        # Se o tempo restante for maior que o quantum, processa por um quantum e reenvia para a fila
        if process.remaining_time > quantum:
            print(f"Processo {process.id} executando por {quantum} unidades de tempo.")
            time += quantum
            process.remaining_time -= quantum
            queue.append(process)
        else:  # Se o tempo restante for menor ou igual ao quantum, o processo finaliza
            print(f"Processo {process.id} executando por {process.remaining_time} unidades de tempo e finalizando.")
            time += process.remaining_time
            process.remaining_time = 0
            process.turnaround_time = time
            process.wait_time = process.turnaround_time - process.burst_time

    # Exibir estatísticas
    print("\nEstatísticas dos processos:")
    total_wait_time = 0
    total_turnaround_time = 0
    for process in processes:
        print(f"Processo {process.id}: Tempo de espera = {process.wait_time}, Tempo de turnaround = {process.turnaround_time}")
        total_wait_time += process.wait_time
        total_turnaround_time += process.turnaround_time

    # Média dos tempos de espera e turnaround
    print(f"\nTempo médio de espera: {total_wait_time / len(processes):.2f}")
    print(f"Tempo médio de turnaround: {total_turnaround_time / len(processes):.2f}")

# Lista de processos (id, tempo de execução)
process_list = [
    Process(1, 10),
    Process(2, 5),
    Process(3, 8)
]

# Definindo o quantum
time_quantum = 3

# Chamando a simulação
round_robin(process_list, time_quantum)
