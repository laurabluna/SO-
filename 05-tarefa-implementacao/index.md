# Implementação de tarefas

## Informações gerais

- Capítulo: [Implementação de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-05.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Laura Beatriz Luna Maia
- matrícula: 20232014040018

## Respostas dos exercícios

questão 1
O Task Control Block (TCB) é uma estrutura de dados mantida pelo sistema operacional para gerenciar informações sobre cada tarefa/processo. Ele é essencial para a troca de contexto e o gerenciamento eficiente de processos.

Para que serve?
O TCB é utilizado pelo escalonador e pelo gerenciador de processos do sistema operacional para:

Rastrear processos ativos.
Armazenar o estado de um processo durante a troca de contexto.
Garantir que a execução de processos seja retomada corretamente após interrupções.
O que contém um TCB?
O TCB normalmente inclui:

Identificador do processo (PID) – Número único do processo.
Estado do processo – Se está Pronto, Executando, Bloqueado, Terminado etc.
Contador de programa (PC) – Endereço da próxima instrução a ser executada.
Registradores da CPU – Valores salvos dos registradores durante a troca de contexto.
Informações de escalonamento – Prioridade, tempo de CPU, entre outros.
Informações de memória – Localização do código, pilha e heap do processo.
Informações sobre recursos – Arquivos abertos, uso de dispositivos, entre outros.
Lista de processos filhos – Processos criados por este processo


questão 2
Passo 1: Identificar os forks
fork() na linha 5: Cria um novo processo filho.
fork() na linha 9: Cria outro processo filho, mas depende de qual processo está executando.
Passo 2: Criar a árvore de processos
Após a primeira chamada de fork(), temos:

Processo Pai
Processo Filho (Criado na linha 5)
Após o segundo fork() na linha 9, se ambos os processos existentes executarem o fork(), teremos:

Processo Pai
Primeiro Filho (Criado na linha 5)
Segundo Filho (Criado na linha 9 pelo processo Pai)
Terceiro Filho (Criado na linha 9 pelo Primeiro Filho)
Passo 3: Comportamento do Código
x inicia como 0.
Após fork(), cada processo tem sua própria cópia de x.
Cada processo executa x++ (linha 6) e dorme por 5 segundos (sleep(5)).
O wait(0) na linha 8 faz o processo pai esperar seu filho terminar.
O segundo fork() (linha 9) cria mais processos.
Após outro wait(0), cada processo dorme mais 5 segundos.
O segundo x++ ocorre antes de imprimir x.
Passo 4: Saída esperada
Cada processo imprime x com base no número de execuções de x++. Como cada processo tem sua própria cópia de x, podemos ter saídas diferentes dependendo da ordem dos forks e waits.
Saída possível:

yaml
Copiar
Editar
Valor de x: 2
Valor de x: 2
Valor de x: 2
Valor de x: 2
Isso ocorre porque cada processo faz os dois incrementos separadamente.

Passo 5: Duração total do programa
Primeiro sleep(5)
Wait() pode causar pequeno atraso
Segundo sleep(5)
No pior caso, o programa pode levar ~10 segundos para terminar.
Diagrama de Tempo
O diagrama a seguir mostra os momentos principais da execução:

perl
Copiar
Editar
Tempo (s)   Processo Pai   Filho 1   Filho 2   Filho 3
-------------------------------------------------------
0           | fork() cria Filho 1    |            
1           | x++                   | x++       
5           | wait() (espera Filho)  | sleep(5)   
6           | fork() cria Filho 2    |            
7           | x++                    | x++       
10          | wait() (espera Filho)  | sleep(5)   
11          | printf x=2              | printf x=2     
Assim, temos 4 processos imprimindo x=2


questão 3

O primeiro fork() no laço é chamado 2 vezes, e cria 2 filhos. Então, temos:
Processo pai (PID inicial) = 1 "X".
Primeiro filho = 1 "X".
Segundo filho = 1 "X".
A condição pid[0] != 0 && pid[N-1] != 0 será verdadeira para o processo pai (porque pid[0] != 0 e pid[1] != 0). Como resultado, um novo processo será criado com fork() na linha 16, e ele também imprimirá a letra "X".
Número total de letras "X" imprimidas:

Pai: 1 "X"
Primeiro filho: 1 "X"
Segundo filho: 1 "X"
Processo adicional criado após o if: 1 "X"
Portanto, 4 letras "X" serão impressas

questão 4
Threads são unidades de execução dentro de um processo. Elas permitem que um único processo seja dividido em múltiplas tarefas que podem ser executadas simultaneamente ou de forma intercalada, compartilhando o mesmo espaço de memória do processo. Threads são usadas principalmente para:

- Melhorar o desempenho de programas, aproveitando a capacidade de processadores multi-core.
- Realizar várias operações ao mesmo tempo (como leitura de dados e processamento em paralelo).
- Melhorar a responsividade de aplicações, como em interfaces gráficas e servidores de alto desempenho.]


questão 5
Vantagens:

Eficiência: Threads compartilham o mesmo espaço de memória, o que torna a comunicação entre elas mais eficiente do que entre processos.
Desempenho: Em sistemas multi-core, múltiplas threads podem ser executadas em paralelo, aumentando o desempenho de programas que podem ser paralelizados.
Menor sobrecarga: Criar e gerenciar threads é menos custoso do que criar e gerenciar processos, pois elas compartilham recursos do processo pai.
Desvantagens:

Complexidade: A programação com threads é mais complexa, pois é necessário gerenciar sincronização e comunicação entre elas.
Condições de corrida e deadlocks: Quando várias threads acessam recursos compartilhados, podem ocorrer problemas de concorrência, como condições de corrida ou deadlocks.
Segurança: Como threads compartilham o mesmo espaço de memória, um erro em uma thread pode afetar outras threads no mesmo processo.

questão 6

Problema de I/O com latência alta: Quando o programa é limitado por operações de entrada/saída (como leitura de arquivos ou comunicação de rede), a criação de múltiplas threads pode não resultar em um ganho de desempenho, pois o tempo de espera nas operações de I/O não é reduzido com paralelismo.

Problemas com alto custo de sincronização: Quando várias threads precisam de sincronização constante para acessar dados compartilhados (como em um banco de dados ou em uma aplicação com acesso concorrente a recursos), a sobrecarga de gerenciar o bloqueio de recursos pode superar os benefícios do paralelismo, tornando a versão sequencial mais eficiente.


questão 7
a) many-to-one (N:1):

(a) Tem a implementação mais simples, leve e eficiente.
(h) Se um thread bloquear, todos os demais têm de esperar por ele.
(d) Não permite explorar a presença de várias CPUs pelo mesmo processo.
(f) Geralmente implementado por bibliotecas.

b) one-to-one (1:1):

(g) É o modelo implementado no Windows NT e seus sucessores.
(i) Cada thread no nível do usuário tem sua correspondente dentro do núcleo.
(c) Pode impor uma carga muito pesada ao núcleo.

c) many-to-many (N:M):

(e) Permite uma maior concorrência sem impor muita carga ao núcleo.
(b) Multiplexa os threads de usuário em um pool de threads de núcleo.
(j) É o modelo com implementação mais complexa.

questão 8
a) Diagramas de Execução
1. Modelo Many-to-One (N:1)
No modelo many-to-one, as threads de usuário são mapeadas para um único thread de núcleo. Isso significa que, mesmo que você crie várias threads, o núcleo só pode executar uma de cada vez, e isso pode causar bloqueios se uma thread bloquear (como no caso do sleep(10)).

Execução: O thread principal (main) cria tA e tB, mas devido à natureza do modelo N:1, o núcleo alterna entre essas threads, de modo que quando uma thread bloqueia com sleep(10), as outras ficam na fila esperando.
Comportamento:
tA e tB são criadas, mas o núcleo executa apenas uma delas por vez.
tA e tB chamam sleep(10), o que faz com que o núcleo "pause" essas threads por 10 segundos.
O main aguarda o término de tA e tB usando thread_join().
tC é criada após um segundo de espera e executa com o mesmo comportamento.
Diagrama de Execução (many-to-one):
rust
Copiar
Editar
main()        tA          tB         tC
 |             |           |          |
 |---->create-->|           |          |
 |             |--->sleep-->|          |
 |             |           |--->sleep--|
 |---->sleep(1)--|           |          |
 |             |<----print---|          |
 |<---join---->|<----print---|          |
 |<---join---->|<----print---|          |
 |             |           |          |
 |---->create-->|           |<----print-|
 |             |           |          |
 |<---join---->|           |          |
 
2. Modelo One-to-One (1:1)
No modelo one-to-one, cada thread de usuário é mapeada para um thread de núcleo. Isso significa que cada thread pode ser executada simultaneamente em um sistema com múltiplos núcleos (caso haja recursos disponíveis). Neste modelo, enquanto uma thread está executando, outras podem estar bloqueadas devido ao sleep() ou outras operações.

Execução: tA, tB, e tC podem ser executadas simultaneamente (ou de maneira intercalada em sistemas com um único núcleo), e o main aguardará suas finalizações com thread_join().
Comportamento:
O main cria as threads tA, tB e tC.
As threads podem executar simultaneamente, e o bloqueio de uma thread com sleep(10) não afeta as outras threads.
As threads completam a execução e o main aguarda as threads com thread_join().
Diagrama de Execução (one-to-one):
rust
Copiar
Editar
main()        tA          tB         tC
 |             |           |          |
 |---->create-->|           |          |
 |             |--->sleep-->|          |
 |             |           |--->sleep--|
 |---->sleep(1)--|           |          |
 |             |<----print---|          |
 |<---join---->|<----print---|<----print-|
 |<---join---->|           |          |
 |             |           |          |
 |---->create-->|           |          |
 |             |           |<----print-|
 |<---join---->|           |          |


b) Duração Aproximada de Execução
Many-to-One (N:1):
O main cria as threads tA e tB, mas o sistema alterna entre essas threads, esperando que cada uma termine seu sleep(10). Isso resulta em uma execução de aproximadamente 11 segundos (1 segundo de sleep(1) no main, seguido pelos 10 segundos de bloqueio das threads).
Após o término de tA e tB, o main cria a thread tC e aguarda sua execução, resultando em mais 1 segundo de execução.
Duração aproximada: 12 segundos.

One-to-One (1:1):
O main cria as threads tA e tB, mas as threads podem ser executadas simultaneamente. O tempo de bloqueio de sleep(10) é distribuído entre as threads, e elas podem terminar antes que o main crie a thread tC.
Após o término de tA e tB, o main cria tC, que também faz o sleep(10).
Duração aproximada: 12 segundos (semelhante ao modelo N:1, pois o tempo de execução ainda depende do bloqueio das threads)

c) Saída do Programa na Tela
Para ambos os modelos (N:1 e 1:1), as saídas serão semelhantes, mas a ordem pode variar dependendo da execução simultânea das threads.

As threads tA, tB, e tC podem imprimir a linha x: 1, y: 1 (ou valores incrementados dependendo da ordem de execução). O valor de x será sempre 1 (pois é inicializado dentro da thread e incrementado), mas o valor de y será incrementado por cada thread executada.
A saída será algo assim:

yaml
Copiar
Editar
x: 1, y: 1
x: 1, y: 2
x: 1, y: 3
 
