# Revisão de código e documentação
Revisei o que produzi na sprint depois de terminar tudo, com isso foi possível observar o que ficou bom e alguns problemas encontrados pelo caminho

## O que ficou bom

- Os 19 testes passam, entre cenários positivos e negativos.
- Usei `Decimal` com `ROUND_HALF_UP`, o que evita os erros de arredondamento que aparecem com `float`.
- Criei erros próprios (`MoedaNaoSuportadaError` e `ValorInvalidoError`), então as mensagens ficam claras para quem usa.
- A documentação cobre todas as seções que o enunciado pede.

##  problemas encontrados

1. **(Corrigido)** **Entradas como `nan`, `inf` e `1e400` quebravam o conversor** com um erro genérico (`decimal.InvalidOperation`) em vez do meu `ValorInvalidoError`. Para `nan` e `inf`, resolvi checando `valor_decimal.is_finite()` em `_validar_valor`, antes da comparação com zero. O `1e400` é um número finito e só falhava depois, no `quantize`, então também passei a capturar o `InvalidOperation` no arredondamento. Adicionei testes para os três casos.
2. **(Corrigido)** **A interface de terminal não tinha teste.** A função `_entrada_interativa` só tinha sido testada na mão. Usei `unittest.mock.patch("builtins.input")` para simular a digitação e criei testes para a conversão e para o erro exibido.
3. **(Corrigido)** **O teste de arredondamento era fraco.** Ele convertia USD para USD, e o comentário falava de BRL, o que confundia. Troquei pelo caso 1 EUR para BRL, que dá 5,8695... e arredonda para 5,87, e mantive o caso original (1,005) como teste separado do arredondamento exato pela metade.
4. **(Corrigido)** **Não testei as taxas de câmbio.** Como são fixas, adicionei um teste garantindo que toda moeda suportada tem taxa maior que zero.
5.  **(Resolvido)** A documentação inicial era do login, mas o enunciado pede a documentação do conversor na etapa de entrega. Troquei para documentar o conversor de moedas, que é o foco da sprint.
6. **(Corrigido)** **O fluxograma do login não verificava se a conta já estava bloqueada.** Pelo desenho antigo, quem tentasse entrar durante o bloqueio seguia direto para a comparação da senha, sendo que o campo `bloqueado_ate` existe justamente para barrar isso. Também faltava indicar que o contador de tentativas volta a zero depois de um login bem-sucedido. Refiz o diagrama incluindo a verificação de bloqueio antes da comparação de credenciais e a etapa de zerar o contador após o sucesso.

## Melhorias para uma próxima sprint

- Usar uma API pública de câmbio (por exemplo, exchangerate.host) para ter taxas em tempo real.
- Trocar o terminal por uma interface web simples.
- Incluir mais moedas, bastando acrescentar entradas em `TAXAS_PARA_USD`.
- Registrar a data em que as taxas fixas foram definidas.