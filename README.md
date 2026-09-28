# Agile Docs & Code Sprint

Este repositório reúne tudo que foi produzido na atividade **Agile Docs & Code**. A ideia era documentar, programar e testar um conversor de moedas simples, acompanhando tudo em um quadro no Trello.

**Autora**: Catarina Carrilho de Almeida
**Quadro Trello:** https://trello.com/b/vai2DT8R/meu-quadro-do-trello

## O que tem aqui

```
.
├── README.md
├── .gitignore
├── REVISAO.md                          # minha revisão de código e documentação
├── documentacao_tecnica_login.pdf      # documentação técnica 
└── conversor/
    ├── conversor_moedas.py             # o conversor
    └── test_conversor_moedas.py        # testes unitários (unittest)
```

## Como organizei a sprint

Logo após iniciar a sprint, criei o quadro no Trello com as listas Backlog, To Do, In Progress e Done. Fui movendo os cartões conforme avançava, e todos terminaram em Done:

1. Definir critérios de aceitação
2. Escrever a documentação técnica
3. Desenvolver o código do conversor de moedas
4. Desenvolver os testes unitários
5. Revisão de código e documentação

## O que o conversor faz

Os critérios de aceitação que defini foram:

- escolher a moeda de origem e a de destino;
- informar o valor na moeda de origem;
- ver o valor equivalente na moeda de destino;
- resultado com pelo menos duas casas decimais;
- arredondamento correto (ROUND_HALF_UP).

Nesta versão o conversor trabalha com **USD, EUR e BRL**, usando taxas fixas que ficam em `TAXAS_PARA_USD`. Foi optado por taxas fixas para manter o foco no que a atividade pede, sem depender de uma API externa. Integrar uma API de câmbio ficou como melhoria futura.

## Como rodar

Só precisa do Python 3, sem instalar nada extra.

```bash
cd conversor

# usar o conversor pelo terminal
python3 conversor_moedas.py

# rodar os testes
python3 -m unittest test_conversor_moedas -v
```

  Foram criados 19 testes, sendo 10 de cenários que devem funcionar, 7 de erros esperados (moeda inválida, valor negativo, valor não numérico, nan, inf, valor gigante) e 2 da interface de terminal. Todos passam.

## Sobre a documentação técnica

O enunciado pede a documentação da funcionalidade de **login**, então foi ela que documentei, com descrição, diagrama de fluxo, interfaces, armazenamento e serviços externos. No fim, deixei uma observação explicando como o login se conecta ao conversor de moedas, que é o foco da sprint.

## Revisão

Depois de terminar, revisei o código e a documentação. Anotei o que funcionou bem, o que encontrei de problema e o que melhoraria em [`REVISAO.md`](REVISAO.md).

## Reflexão sobre o Scrum

Fazer essa sprint sozinha ajudou a entender melhor como o Scrum funciona na prática. O Trello facilitou o acompanhamento das tarefas, mostrando o que ainda precisava ser feito, o que estava em andamento e o que já estava concluído, como uma agenda online. Os critérios de aceitação também ajudaram a orientar o desenvolvimento e os testes.

Ao mesmo tempo, ficou claro que o Scrum funciona ainda melhor quando se está em equipe. Sozinha, foi preciso assumir todos os papéis, desde definir prioridades até revisar o próprio trabalho. Em grupo, seria possível dividir melhor as tarefas, trocar ideias e ter outras pessoas revisando o código.

Depois da revisão, corrigi o tratamento de entradas como nan e inf, criei os testes da interface de terminal e das taxas de câmbio, e ajustei o fluxograma do login para tratar o bloqueio de conta. Numa próxima sprint, eu focaria em integrar uma API de câmbio para ter taxas em tempo real, evoluir a interface para algo mais amigável e incluir na documentação uma seção sobre o conversor. Esses pontos estão anotados no REVISAO.md e dariam bons cartões para o Backlog da sprint seguinte.

## Referências

- PRESSMAN, R. S.; MAXIM, B. R. *Engenharia de Software: uma abordagem profissional*. 9. ed. Porto Alegre: AMGH, 2021.
- SCHWABER, K.; SUTHERLAND, J. *Um guia definitivo para o Scrum: as regras do jogo*. Scrumguides, 2017.
