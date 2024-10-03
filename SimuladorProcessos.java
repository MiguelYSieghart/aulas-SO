import java.util.ArrayList;
import java.util.List;
import java.util.Random;

// Definindo os estados dos processos
enum Estados {
    NOVO, PRONTO, EXECUTANDO, BLOQUEADO, TERMINADO
}

// Classe que representa um processo
class Processo {
    private String processoid;
    private Estados estado;

    public Processo() {
        this.processoid = gerarProcessoidAleatorio();
        this.estado = Estados.NOVO;
    }

    private String gerarProcessoidAleatorio() {
        Random random = new Random();
        return Integer.toString(1000 + random.nextInt(9000));
    }

    public void mostrar() {
        System.out.println("ProcessoID: " + processoid + ", Estado: " + estado);
    }

    public Estados getEstado() {
        return estado;
    }

    public void setEstado(Estados estado) {
        this.estado = estado;
    }
}

// Classe que simula o funcionamento de um escalonador de processos
public class SimuladorProcessos {

    private static List<Processo> inicializarProcessos(int n) {
        List<Processo> processos = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            processos.add(new Processo());
        }
        return processos;
    }

    // Define o próximo estado de um processo
    private static void proximoEstado(Processo processo) {
        Random random = new Random();

        switch (processo.getEstado()) {
            case NOVO:
                processo.setEstado(Estados.PRONTO);
                break;
            case PRONTO:
                if (random.nextDouble() < 0.5) {
                    processo.setEstado(Estados.EXECUTANDO);
                } else {
                    processo.setEstado(Estados.BLOQUEADO);
                }
                break;
            case EXECUTANDO:
                double probabilidade = random.nextDouble();
                if (probabilidade < 0.3) {
                    processo.setEstado(Estados.PRONTO);
                } else if (probabilidade < 0.6) {
                    processo.setEstado(Estados.BLOQUEADO);
                } else {
                    processo.setEstado(Estados.TERMINADO);
                }
                break;
            case BLOQUEADO:
                processo.setEstado(Estados.PRONTO);
                break;
            default:
                break;
        }
    }

    // Verifica se todos os processos terminaram
    private static boolean todosProcessosTerminaram(List<Processo> processos) {
        for (Processo processo : processos) {
            if (processo.getEstado() != Estados.TERMINADO) {
                return false;
            }
        }
        return true;
    }

    // Método principal
    public static void main(String[] args) {
        final int NUMERO_DE_PROCESSOS = 5;
        List<Processo> processos = inicializarProcessos(NUMERO_DE_PROCESSOS);

        int iteracoes = 0;
        Random random = new Random();

        while (!todosProcessosTerminaram(processos)) {
            for (Processo processo : processos) {
                if (random.nextDouble() < 0.5) { // Probabilidade de alterar o estado
                    proximoEstado(processo);
                }
            }
            iteracoes++;

            System.out.println("\n-- Iteração " + iteracoes + " --");
            for (Processo processo : processos) {
                processo.mostrar();
            }
        }

        System.out.println("\nTodos os processos foram finalizados! Total de " + iteracoes + " iterações.");
    }
}
