# Revisão de código e documentação
Revisei o que produzi na sprint depois de terminar tudo, com isso foi possível observar o que ficou bom e alguns problemas encontrados pelo caminho

## O que ficou bom

- Os 12 testes passam, entre cenários positivos e negativos.
- Usei `Decimal` com `ROUND_HALF_UP`, o que evita os erros de arredondamento que aparecem com `float`.
- Criei erros próprios (`MoedaNaoSuportadaError` e `ValorInvalidoError`), então as mensagens ficam claras para quem usa.
- A documentação cobre todas as seções que o enunciado pede.

## O que encontrei de problema

1. **Entradas como `nan`, `inf` e `1e400` quebram o conversor** com um erro genérico (`decimal.InvalidOperation`) em vez do meu `ValorInvalidoError`. Para `nan` e `inf`, dá para resolver checando `valor_decimal.is_finite()` em `_validar_valor`, antes da comparação com zero. O `1e400` é um número finito e só falha depois, no `quantize`, então exigiria também capturar o `InvalidOperation` no arredondamento. Em ambos os casos, seria preciso adicionar um teste.
2. **A interface de terminal não tem teste.** A função `_entrada_interativa` só foi testada na mão. Poderia usar `unittest.mock.patch("builtins.input")` para simular a digitação.
3. **O teste de arredondamento é fraco.** Ele converte USD para USD, e o comentário fala de BRL, o que confunde. Um caso melhor seria 1 EUR para BRL, que dá 5,8695... e arredonda para 5,87.
4. **Não testei as taxas de câmbio.** Como são fixas, bastaria um teste garantindo que toda moeda suportada tem taxa maior que zero.
5. **A documentação é do login, e o foco da sprint é o conversor.** Segui o enunciado, mas uma seção curta sobre o conversor deixaria a documentação mais completa.
6. **O fluxograma do login não verifica se a conta já está bloqueada.** Pelo desenho, quem tenta entrar durante o bloqueio segue direto para a comparação da senha, sendo que o campo `bloqueado_ate` existe justamente para barrar isso. Também falta indicar que o contador de tentativas volta a zero depois de um login bem-sucedido.

## Melhorias para uma próxima sprint

- Usar uma API pública de câmbio (por exemplo, exchangerate.host) para ter taxas em tempo real.
- Trocar o terminal por uma interface web simples.
- Incluir mais moedas, bastando acrescentar entradas em `TAXAS_PARA_USD`.
- Registrar a data em que as taxas fixas foram definidas.