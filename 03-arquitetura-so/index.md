# Arquiteturas de Sistemas Operacionais

## Informações gerais

- Capítulo: [Arquitetura de SO](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-03.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Laura Beatriz Luna Maia 
- matrícula: 20232014040018

## Respostas dos exercícios
questão 1

Arquitetura	

Monolítica	- Alto desempenho devido à comunicação direta entre os componentes.
- Implementação relativamente simples.
- Uso eficiente dos recursos do sistema.	- Dificuldade na manutenção e atualização, pois qualquer modificação exige a recompilação do kernel.
- Maior risco de falhas catastróficas devido à falta de isolamento entre os módulos.


Micronúcleo (Microkernel)	- Maior modularidade e facilidade de manutenção.
- Melhor segurança e estabilidade devido ao isolamento de processos.
- Possibilidade de extensão sem impactar o núcleo.	- Desempenho inferior em comparação ao modelo monolítico devido ao aumento de troca de mensagens entre processos.
- Maior complexidade de implementação.


Híbrida	- Combina vantagens do monolítico e do micronúcleo, equilibrando desempenho e modularidade.
- Melhor adaptabilidade a diferentes sistemas e necessidades.
- Facilidade na adição de novos recursos.	- Pode herdar complexidade de ambas as arquiteturas.
- Potencial para problemas de desempenho dependendo da implementação.


Máquina Virtual	- Excelente portabilidade, permitindo a execução em diferentes plataformas.
- Melhor isolamento e segurança entre processos e sistemas.
- Facilidade de teste e desenvolvimento de novos sistemas operacionais.	- Pode ter desempenho inferior devido à sobrecarga da virtualização.
- Maior consumo de recursos, como memória e processamento.


Exonúcleo (Exokernel)	- Maior controle e flexibilidade para aplicações especializadas.
- Melhor desempenho, pois elimina abstrações desnecessárias do kernel.	- Maior complexidade no desenvolvimento de aplicações, pois o SO não fornece muitas abstrações.
- Baixa compatibilidade com software legado.

questão 2

O Linux possui um núcleo monolítico modular, pois os principais serviços do sistema operam no modo kernel, garantindo alto desempenho. No entanto, ele permite carregar e descarregar módulos dinamicamente, tornando-o mais flexível. Diferente de um micronúcleo, ele não separa rigidamente os serviços do sistema no modo usuário, evitando a sobrecarga da troca de mensagens.

questão 3

a) incorreta
máquina virtual emula um hardware para suportar qualquer SO. A máquina virtual é projetada para executar aplicações escritas em uma linguagem específica

b) correta
o hipervisor roda sob um sistema operacional hospedeiro, enquanto o 1 roda no hardware, sem precisar de algo intermediando eles. 

c) incorreta
Em um micronúcleo, a maioria dos componentes do sistema (como drivers e gerenciadores de arquivos) roda no espaço do usuário, fora do núcleo. Apenas um pequeno conjunto de funções essenciais (como comunicação entre processos e gerenciamento de memória) executa dentro do núcleo.

d) incorreta
monolíticos são populares devido ao alto desempenho, pois os componentes do sistema rodam diretamente no kernel sem precisar de troca de mensagens. No entanto, eles não são fáceis de manter, pois qualquer modificação exige a recompilação do núcleo, e erros podem afetar todo o sistema.

e) correta
Em um micronúcleo, serviços como gerenciamento de arquivos e drivers rodam no espaço do usuário e precisam se comunicar com o núcleo