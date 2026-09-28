"""

Implementa a funcionalidade de conversão entre moedas pré-definidas
(USD, EUR, BRL) usando taxas de câmbio fixas, conforme os critérios
de aceitação definidos na Sprint "Agile Docs & Code".

Critérios de aceitação cobertos:
- Seleção de moeda de origem e de destino;
- Entrada da quantidade na moeda de origem;
- Exibição do valor equivalente na moeda de destino;
- Resultado com precisão de, no mínimo, duas casas decimais;
- Arredondamento correto do resultado.
"""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


# Taxas de câmbio fixas, usando o Dólar (USD) como moeda base.
# Cada valor representa quantas unidades da moeda equivalem a 1 USD.
TAXAS_PARA_USD = {
    "USD": Decimal("1"),
    "EUR": Decimal("0.92"),
    "BRL": Decimal("5.40"),
}

MOEDAS_SUPORTADAS = tuple(TAXAS_PARA_USD.keys())


class MoedaNaoSuportadaError(ValueError):
    """Lançada quando a moeda de origem ou destino não está cadastrada."""


class ValorInvalidoError(ValueError):
    """Lançada quando o valor a ser convertido é inválido (negativo ou não numérico)."""


def _validar_moeda(codigo_moeda):
    if codigo_moeda not in TAXAS_PARA_USD:
        raise MoedaNaoSuportadaError(
            f"Moeda '{codigo_moeda}' não é suportada. "
            f"Moedas disponíveis: {', '.join(MOEDAS_SUPORTADAS)}"
        )


def _validar_valor(valor):
    try:
        valor_decimal = Decimal(str(valor))
    except Exception:
        raise ValorInvalidoError(f"Valor '{valor}' não é um número válido.")

    if not valor_decimal.is_finite():
        raise ValorInvalidoError(f"Valor '{valor}' não é um número finito.")

    if valor_decimal < 0:
        raise ValorInvalidoError("O valor a ser convertido não pode ser negativo.")

    return valor_decimal


def converter(valor, moeda_origem, moeda_destino):
    """
    Converte um valor de uma moeda de origem para uma moeda de destino.

    Parâmetros:
        valor (int, float, str ou Decimal): quantidade na moeda de origem.
        moeda_origem (str): código da moeda de origem (ex.: "USD").
        moeda_destino (str): código da moeda de destino (ex.: "BRL").

    Retorna:
        float: valor convertido, arredondado para duas casas decimais.

    Lança:
        MoedaNaoSuportadaError: se a moeda de origem ou destino não existir.
        ValorInvalidoError: se o valor informado for negativo ou não numérico.
    """
    moeda_origem = moeda_origem.upper()
    moeda_destino = moeda_destino.upper()

    _validar_moeda(moeda_origem)
    _validar_moeda(moeda_destino)
    valor_decimal = _validar_valor(valor)

    valor_em_usd = valor_decimal / TAXAS_PARA_USD[moeda_origem]
    valor_convertido = valor_em_usd * TAXAS_PARA_USD[moeda_destino]

    try:
        valor_arredondado = valor_convertido.quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
    except InvalidOperation:
        raise ValorInvalidoError(f"Valor '{valor}' é grande demais para ser convertido.")

    return float(valor_arredondado)


def _entrada_interativa():
    """Interface simples de linha de comando para uso manual do conversor."""
    print("=== Conversor de Moedas ===")
    print(f"Moedas disponíveis: {', '.join(MOEDAS_SUPORTADAS)}")

    origem = input("Moeda de origem: ").strip().upper()
    destino = input("Moeda de destino: ").strip().upper()
    valor = input("Valor a converter: ").strip()

    try:
        resultado = converter(valor, origem, destino)
        print(f"{valor} {origem} = {resultado:.2f} {destino}")
    except (MoedaNaoSuportadaError, ValorInvalidoError) as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    _entrada_interativa()
