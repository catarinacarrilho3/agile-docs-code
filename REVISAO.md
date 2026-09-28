# Revisão de código e documentação

Revisei o que produzi na sprint depois de terminar tudo. Aqui está o que achei.

## O que ficou bom

- Os 19 testes passam, entre cenários positivos e negativos.
- Usei `Decimal` com `ROUND_HALF_UP`, o que evita os erros de arredondamento que aparecem com `float`.
- Criei erros próprios (`MoedaNaoSuportadaError` e `ValorInvalidoError`), então as mensagens ficam claras para quem usa.
- A documentação cobre todas as seções que o enunciado pede.

## O que encontrei de problema

1. **(Corrigido)** **Entradas como `nan`, `inf` ou `1e400` quebram o conversor** com um erro genérico (`decimal.InvalidOperation`) em vez do meu `ValorInvalidoError`. Dá para resolver checando `valor_decimal.is_finite()` em `_validar_valor` e adicionando um teste para isso.
2. **(Corrigido)** **A interface de terminal não tinha teste.** A função `_entrada_interativa` só foi testada na mão. Poderia usar `unittest.mock.patch("builtins.input")` para simular a digitação.
3. **(Corrigido)** **O teste de arredondamento era fraco.** Ele converte USD para USD, e o comentário fala de BRL, o que confunde. Um caso melhor seria 1 EUR para BRL, que dá 5,8695... e arredonda para 5,87.
4. **(Corrigido)** **Não testei as taxas de câmbio.** Como são fixas, bastaria um teste garantindo que toda moeda suportada tem taxa maior que zero.
5. **A documentação é do login, e o foco da sprint é o conversor.** Segui o enunciado, mas uma seção curta sobre o conversor deixaria a documentação mais completa.

## Melhorias para uma próxima sprint

- Usar uma API pública de câmbio (por exemplo, exchangerate.host) para ter taxas em tempo real.
- Trocar o terminal por uma interface web simples.
- Incluir mais moedas, bastando acrescentar entradas em `TAXAS_PARA_USD`.
- Registrar a data em que as taxas fixas foram definidas.
