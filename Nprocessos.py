import random
from enum import Enum

# Definindo os estados dos processos
class Estados(Enum):
    Novo = "Novo"
    Pronto = "Pronto"
    Executando = "Executando"
    Bloqueado = "Bloqueado"
    Terminado = "Terminado"

class Processo:
    def __init__(self):
        self.pid = self.gerar_pid_aleatorio()
        self.estado = Estados.Novo

    def gerar_pid_aleatorio(self):
        return str(random.randint(1000, 9999))

    def mostrar(self):
        print(f"PID: {self.pid}, Estado: {self.estado.value}")

def inicializar_processos(n):
    return [Processo() for _ in range(n)]

# Define o próximo estado de um processo
def proximo_estado(processo):
    if processo.estado == Estados.Novo:
        processo.estado = Estados.Pronto
    elif processo.estado == Estados.Pronto:
        if random.random() < 0.5:
            processo.estado = Estados.Executando
        else:
            processo.estado = Estados.Bloqueado
    elif processo.estado == Estados.Executando:
        probabilidade = random.random()
        if probabilidade < 0.3:
            processo.estado = Estados.Pronto
        elif probabilidade < 0.6:
            processo.estado = Estados.Bloqueado
        else:
            processo.estado = Estados.Terminado
    elif processo.estado == Estados.Bloqueado:
        processo.estado = Estados.Pronto

def todos_processos_terminaram(processos):
    return all(processo.estado == Estados.Terminado for processo in processos)

# Simulação de processos
NUMERO_DE_PROCESSOS = 5
processos = inicializar_processos(NUMERO_DE_PROCESSOS)

iteracoes = 0
while not todos_processos_terminaram(processos):
    for processo in processos:
        if random.random() < 0.5:  # Probabilidade de alterar o estado
            proximo_estado(processo)
    iteracoes += 1

    print(f"\n-- Iteração {iteracoes} --")
    for processo in processos:
        processo.mostrar()

print(f"\nTodos os processos foram finalizados! Total de {iteracoes} iterações.")
