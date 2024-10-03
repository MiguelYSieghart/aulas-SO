import random
import time

# Definindo os estados dos processos
ESTADOS = ['Novo', 'Pronto', 'Executando', 'Bloqueado', 'Finalizado']

class Processo:
    def __init__(self, pid):
        self.pid = pid
        self.estado = ESTADOS[0]  # Começa no estado 'Novo'

    def transicao(self):
        if self.estado == 'Novo':
            self.estado = 'Pronto'
        elif self.estado == 'Pronto':
            self.estado = random.choice(['Executando', 'Bloqueado'])
        elif self.estado == 'Executando':
            self.estado = random.choice(['Pronto', 'Bloqueado', 'Finalizado'])
        elif self.estado == 'Bloqueado':
            self.estado = 'Pronto'

    def __str__(self):
        return f"Processo {self.pid}: {self.estado}"

def simular_processos(n):
    processos = [Processo(i) for i in range(n)]

    while any(p.estado != 'Finalizado' for p in processos):
        for processo in processos:
            if processo.estado != 'Finalizado':
                processo.transicao()
                print(processo)
        time.sleep(1)  # Simula o tempo entre as transições
        print('-' * 30)

# Simula o ciclo de vida de 5 processos
simular_processos(5)
