# Escalonamento de tarefas

## Informações gerais

- Capítulo: [Escalonamento de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-06.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: 
- matrícula: 

## Respostas dos exercícios

questão 1
Escalonamento Round-Robin:
O escalonamento Round-Robin (RR) é um algoritmo de escalonamento de processos no qual cada processo recebe um "quantum" de tempo fixo para execução. Quando o processo esgota esse tempo, ele é interrompido e colocado novamente na fila de pronto. O próximo processo da fila é então selecionado e o ciclo se repete.

Exemplo: Considere três processos (P1, P2, P3) com tempos de execução de 4, 3 e 5 unidades de tempo, respectivamente, e um quantum de tempo de 2 unidades. O escalonamento seria o seguinte:

Tempo 0-2: P1 executa por 2 unidades de tempo (restam 2 unidades para P1).
Tempo 2-4: P2 executa por 2 unidades de tempo (resta 1 unidade para P2).
Tempo 4-6: P3 executa por 2 unidades de tempo (restam 3 unidades para P3).
Tempo 6-8: P1 executa por mais 2 unidades (já terminou).
Tempo 8-9: P2 executa sua última unidade de tempo (já terminou).
Tempo 9-12: P3 executa por mais 2 unidades de tempo (resta 1 unidade).
Tempo 12-13: P3 executa sua última unidade de tempo (já terminou).
Esse ciclo continua até todos os processos serem finalizados.

questão 2

A eficiência de um sistema de escalonamento pode ser definida como a proporção de tempo em que o processador está ocupado realizando trabalho útil, em vez de estar aguardando ou realizando troca de contexto.

Seja:

tq: quantum de tempo,
ttc: tempo de troca de contexto,
p: porcentagem do quantum em que o processo realiza I/O (Entrada/Saída).

Quanto maior for 𝑡𝑞 tq e menor for 𝑡𝑡𝑐 ttc, maior será a eficiência do sistema

questão 3

A técnica de aging (envelhecimento) é um método utilizado em sistemas operacionais para evitar a fome de processos (starvation). A fome ocorre quando um processo nunca tem chance de ser executado porque sempre existe um processo de maior prioridade.

O aging aumenta a prioridade de processos que estão esperando na fila por muito tempo, garantindo que processos mais antigos recebam mais atenção. À medida que o tempo passa, os processos com maior tempo de espera têm sua prioridade aumentada.

Como funciona:

Cada vez que um processo não é selecionado para execução, sua prioridade é aumentada gradualmente até atingir um valor que o torne apto para ser escalonado.
Isso pode ser implementado de forma periódica, por exemplo, a cada ciclo de escalonamento.
Essa técnica é importante em algoritmos de escalonamento por prioridade, onde os processos de baixa prioridade podem ser "esquecidos" sem envelhecimento

questão 4
No algoritmo de envelhecimento, caso seja necessário suportar prioridades negativas, as modificações principais seriam:

Permitir que a prioridade de um processo possa ser diminuída (em vez de apenas aumentada) após um certo tempo de espera.
Em vez de apenas aumentar as prioridades de processos com tempo de espera elevado, também permitir que a prioridade de um processo possa ser reduzida, se ele exceder uma certa idade, desde que ainda tenha uma prioridade acima de um limite mínimo (para evitar starvation).
Isso permitiria que a técnica de aging fosse mais flexível, lidando com a possibilidade de valores negativos nas prioridades, onde as tarefas poderiam "envelhecer" para uma maior prioridade, ou eventualmente diminuir sua prioridade para retornar ao ciclo.

questão 5
Tarefa	Ingresso	Duração	Prioridade
t1	     0	         5	     2
t2	     0	         4	     3
t3	     3	         5       5
t4	     5	         6	     9
t5	     7	         4	     6

Considerações:

Tempo de espera (Waiting Time): O tempo que o processo espera na fila de prontos antes de ser executado.
Tempo de vida (Turnaround Time): O tempo desde que o processo é admitido até sua conclusão, ou seja, turnaround time = tempo de término - tempo de ingresso.

questão 6
 FCFS (First-Come, First-Served) cooperativo
A política FCFS executa as tarefas na ordem em que chegam, sem preempção.

Execução:

t1 começa em 0 e termina em 5 (duração 5).
t2 começa em 5 e termina em 11 (duração 6).
t3 começa em 11 e termina em 13 (duração 2).
t4 começa em 13 e termina em 19 (duração 6).
t5 começa em 19 e termina em 23 (duração 4).
Tempos:

Turnaround time (tempo de vida): tempo de término - tempo de ingresso

t1: 5 − 0=55−0=5
t2: 11−0=1111−0=11
t3: 13−1=1213−1=12
t4: 19−7=129−7=12
t5: 23−11=1223−11=12
Waiting time (tempo de espera): tempo de espera = turnaround time - duração

t1: 5−5=05−5=0
t2: 11−6=511−6=5
t3: 12−2=1012−2=10
t4: 12−6=612−6=6
t5: 12−4=812−4=8

2. SJF (Shortest Job First) cooperativo
O algoritmo SJF executa primeiro o processo com o menor tempo de duração.

Execução:

t1 começa em 0 e termina em 5 (duração 5).
t3 começa em 5 e termina em 7 (duração 2).
t2 começa em 7 e termina em 13 (duração 6).
t4 começa em 13 e termina em 19 (duração 6).
t5 começa em 19 e termina em 23 (duração 4).
Tempos:

Turnaround time:

t1: 5−0=55−0=5
t2: 13−0=1313−0=13
t3: 7−1=67−1=6
t4: 19−7=1219−7=12
t5: 23−11=1223−11=12
Waiting time:

t1: 5−5=05−5=0
t2: 13−6=713−6=7
t3: 6−2=46−2=4
t4: 12−6=612−6=6
t5: 12−4=812−4=8


3. SJF preemptiva (SRTF - Shortest Remaining Time First)
Neste algoritmo, o processo com o menor tempo restante é sempre executado, com preempção.

Execução (sequência de execução baseada em tempo restante):

t1 começa em 0 e termina em 5.
t3 começa em 1 e termina em 3 (duração 2).
t2 começa em 3 e termina em 9 (duração 6).
t1 recomeça em 9 e termina em 11 (restante 1).
t4 começa em 11 e termina em 17 (duração 6).
t5 começa em 17 e termina em 21 (duração 4).
Tempos:

Turnaround time:

t1: 11−0=1111−0=11
t2: 9−0=99−0=9
t3: 3−1=23−1=2
t4: 17−7=1017−7=10
t5: 21−11=1021−11=10
Waiting time:

t1: 11−=611−5=6
t2: 9−6=39−6=3
t3: 2−2=02−2=0
t4: 10−6=410−6=4t5: 10−4=610−4=6

4. PRIO (Prioridade) cooperativa
O algoritmo PRIO executa os processos com maior prioridade primeiro.

Execução:

t1 começa em 0 e termina em 5 (prioridade 2).
t2 começa em 5 e termina em 11 (prioridade 3).
t3 começa em 11 e termina em 13 (prioridade 4).
t4 começa em 13 e termina em 19 (prioridade 7).
t5 começa em 19 e termina em 23 (prioridade 9).
Tempos:

Turnaround time:

t1: 5−0=55−0=5
t2: 11−0=1111−0=11
t3: 13−1=1213−1=12
t4: 19−7=1219−7=12
t5: 23−11=1223−11=12
Waiting time:

t1: 5−=05−5=t2: 11−6=511−6=5
t3: 12−=1012−2=10
t4: 12−6=612−6=6
t5: =12−4=812−4=8


5. PRIO preemptiva
Neste caso, o processo de maior prioridade é executado, podendo ser interrompido caso outro de maior prioridade chegue.

Execução:

t1 começa em 0 e termina em 5 (prioridade 2).
t2 começa em 5 e termina em 11 (prioridade 3).
t3 começa em 11 e termina em 13 (prioridade 4).
t4 começa em 13 e termina em 19 (prioridade 7).
t5 começa em 19 e termina em 23 (prioridade 9).
Tempos:

Turnaround time:

t1: 5−0=55−0=5
t2: 11−0=1111−0=11
t3: 13−1=1213−1=12
t4: 19−7=1219−7=12
t5: 23−11=1223−11=12
Waiting time:

t1: 5−5=05−5=0
t2: 11−6=511−6=5
t3: 12−2=1012−2=10
t4: 12−6=612−6=6
t5: 12−4=812−4=8


6. RR (Round-Robin) com tq = 2, sem envelhecimento
No RR, cada tarefa recebe um quantum de 2 unidades de tempo.

Execução:

t1 executa de 0 a 2, depois t2 de 2 a 4, t3 de 4 a 6, e assim por diante.
Tempos (para RR, é necessário calcular o tempo de execução em ciclos e interações, o que resultaria em valores aproximados):

Turnaround time e Waiting time seriam calculados a partir da sequência de execução e o ciclo de troca.
