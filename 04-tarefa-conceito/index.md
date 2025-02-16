# Conceito de tarefas

## Informações gerais

- Capítulo: [Conceito de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-04.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Laura Beatriz Luna Maia
- matrícula: 20232014040018

## Respostas dos exercícios
questão 1

são um gênero de multiprogramação. A estratégia principal utilizada em sistemas com time-sharing é reduzir a ociosidade do processador, de forma com que ele sempre fique ocupado, aumentar a eficiência, e obtendo o máximo possível do hardware.

questão 2 
é o tempo máximo que um processo pode usar a CPU antes que ocorra uma interrupção para permitir que outro processo seja executado. 
A duração do quantum é definida com base no sistema operacional e de acordo com o tipo e prioridade da tarefa.


questão 3

Transição	Origem → Destino	Significado
t1	Novo → Pronto	Processo criado, pronto para execução
t2	Pronto → Executando	Processo escalonado para rodar
t3	Executando → Bloqueado	Processo aguarda um evento (I/O, recurso)
t4	Bloqueado → Pronto	Evento ocorreu, processo pode ser escalonado
t5	Novo → Terminado	Processo encerrado antes de ser executado
t6	Pronto → Terminado	Processo abortado antes de executar
Dessa forma, a transição faltante t6 vai de e3 (Pronto) para e2 (Terminado)


questão 4
Transição	Possível?	Justificativa
E → P	    ✅	      Fim do quantum do processador.
E → S   	✅	      Espera por entrada/saída ou recurso bloqueado.
S → E	    ❌	      Precisa passar por Pronta (P) antes.
P → N	    ❌	      Uma tarefa já carregada não volta para Nova.
S → T	    ❌	      Precisa executar antes de terminar.
E → T   	✅       	A tarefa termina sua execução.
N → S	    ❌       	Precisa estar em Pronta antes.
P → S	    ✅      	O sistema pode suspender uma tarefa para liberar recursos.

questão 5
[E] O código da tarefa está sendo carregado.
[P] As tarefas são ordenadas por prioridades.
[S] A tarefa sai deste estado ao solicitar uma operação de entrada/saída.
[T] Os recursos usados pela tarefa são devolvidos ao sistema.
[T] A tarefa vai a este estado ao terminar seu quantum.
[E] A tarefa só precisa do processador para poder executar.
[S] O acesso a um semáforo em uso pode levar a tarefa a este estado.
[N] A tarefa pode criar novas tarefas.
[E] Há uma tarefa neste estado para cada processador do sistema.
[S] A tarefa aguarda a ocorrência de um evento externo.
