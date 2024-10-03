<?php

// Definindo os estados dos processos
class Estados
{
    const Novo = "Novo";
    const Pronto = "Pronto";
    const Executando = "Executando";
    const Bloqueado = "Bloqueado";
    const Terminado = "Terminado";
}

class Processo
{
    public $pid;
    public $estado;

    public function __construct()
    {
        $this->pid = $this->gerarPidAleatorio();
        $this->estado = Estados::Novo;
    }

    private function gerarPidAleatorio()
    {
        return rand(1000, 9999);
    }

    public function mostrar()
    {
        echo "PID: {$this->pid}, Estado: {$this->estado}\n";
    }
}

// Inicializa um número definido de processos
function inicializarProcessos($n)
{
    $processos = [];
    for ($i = 0; $i < $n; $i++) {
        $processos[] = new Processo();
    }
    return $processos;
}

// Define o próximo estado de um processo
function proximoEstado($processo)
{
    if ($processo->estado === Estados::Novo) {
        $processo->estado = Estados::Pronto;
    } elseif ($processo->estado === Estados::Pronto) {
        if (mt_rand() / mt_getrandmax() < 0.5) {
            $processo->estado = Estados::Executando;
        } else {
            $processo->estado = Estados::Bloqueado;
        }
    } elseif ($processo->estado === Estados::Executando) {
        $probabilidade = mt_rand() / mt_getrandmax();
        if ($probabilidade < 0.3) {
            $processo->estado = Estados::Pronto;
        } elseif ($probabilidade < 0.6) {
            $processo->estado = Estados::Bloqueado;
        } else {
            $processo->estado = Estados::Terminado;
        }
    } elseif ($processo->estado === Estados::Bloqueado) {
        $processo->estado = Estados::Pronto;
    }
}

// Verifica se todos os processos estão terminados
function todosProcessosTerminaram($processos)
{
    foreach ($processos as $processo) {
        if ($processo->estado !== Estados::Terminado) {
            return false;
        }
    }
    return true;
}

// Simulação de processos
$NUMERO_DE_PROCESSOS = 5;
$processos = inicializarProcessos($NUMERO_DE_PROCESSOS);

$iteracoes = 0;
while (!todosProcessosTerminaram($processos)) {
    foreach ($processos as $processo) {
        if (mt_rand() / mt_getrandmax() < 0.5) {
            proximoEstado($processo);
        }
    }
    $iteracoes++;

    echo "\n-- Iteração $iteracoes --\n";
    foreach ($processos as $processo) {
        $processo->mostrar();
    }
}

echo "\nTodos os processos foram finalizados! Total de $iteracoes iterações.\n";