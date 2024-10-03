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
        self.tempo_espera = 0  # Novo atributo para controlar tempo de espera

    def gerar_pid_aleatorio(self):
        return str(random.randint(1000, 9999))

    def mostrar(self):
        print(f"PID: {self.pid}, Estado: {self.estado.value}, Tempo de Espera: {self.tempo_espera}")

    def incrementar_tempo_espera(self):
        if self.estado == Estados.Pronto or self.estado == Estados.Bloqueado:
            self.tempo_espera += 1

def inicializar_processos(n):
    return [Processo() for _ in range(n)]

# Mapeando transições de estados com base em probabilidades
transicoes = {
    Estados.Novo: Estados.Pronto,
    Estados.Pronto: lambda: Estados.Executando if random.random() < 0.6 else Estados.Bloqueado,
    Estados.Executando: lambda: random.choices([Estados.Pronto, Estados.Bloqueado, Estados.Terminado], weights=[0.4, 0.3, 0.3])[0],
    Estados.Bloqueado: Estados.Pronto,
}

def proximo_estado(processo):
    estado_atual = processo.estado
    if estado_atual in transicoes:
        transicao = transicoes[estado_atual]
        processo.estado = transicao() if callable(transicao) else transicao

def todos_processos_terminaram(processos):
    return all(processo.estado == Estados.Terminado for processo in processos)

# Simulação de processos
NUMERO_DE_PROCESSOS = 5
processos = inicializar_processos(NUMERO_DE_PROCESSOS)

iteracoes = 0
while not todos_processos_terminaram(processos):
    for processo in processos:
        if processo.estado != Estados.Terminado:
            processo.incrementar_tempo_espera()
            if random.random() < 0.7:  # Ajustando a chance de mudar o estado para 70%
                proximo_estado(processo)
    iteracoes += 1

    print(f"\n-- Iteração {iteracoes} --")
    for processo in processos:
        processo.mostrar()

print(f"\nTodos os processos foram finalizados! Total de {iteracoes} iterações.")
