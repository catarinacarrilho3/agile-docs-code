"""
Testes unitários para o módulo conversor_moedas, usando o framework unittest.

Cobre cenários positivos e negativos com base nos critérios de aceitação
definidos para a funcionalidade de conversão de moedas.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from conversor_moedas import (
    TAXAS_PARA_USD,
    _entrada_interativa,
    converter,
    MoedaNaoSuportadaError,
    ValorInvalidoError,
)


class TestConversorMoedas(unittest.TestCase):

    # --- Cenários positivos ---

    def test_conversao_usd_para_brl(self):
        resultado = converter(100, "USD", "BRL")
        self.assertEqual(resultado, 540.00)

    def test_conversao_brl_para_usd(self):
        resultado = converter(540, "BRL", "USD")
        self.assertEqual(resultado, 100.00)

    def test_conversao_eur_para_usd(self):
        resultado = converter(92, "EUR", "USD")
        self.assertEqual(resultado, 100.00)

    def test_conversao_mesma_moeda_retorna_valor_igual(self):
        resultado = converter(250, "BRL", "BRL")
        self.assertEqual(resultado, 250.00)

    def test_conversao_aceita_letras_minusculas(self):
        resultado = converter(100, "usd", "brl")
        self.assertEqual(resultado, 540.00)

    def test_resultado_tem_duas_casas_decimais(self):
        resultado = converter(10, "USD", "EUR")
        # 10 * 0.92 = 9.20
        self.assertEqual(resultado, 9.20)

    def test_arredondamento_correto(self):
        # 1 EUR -> BRL: 1 / 0.92 * 5.40 = 5.8695... -> 5.87
        resultado = converter(1, "EUR", "BRL")
        self.assertEqual(resultado, 5.87)

    def test_arredondamento_half_up(self):
        resultado = converter(1.005, "USD", "USD")
        self.assertEqual(resultado, 1.01)  

    def test_taxas_sao_maiores_que_zero(self):
        for moeda, taxa in TAXAS_PARA_USD.items():
            self.assertGreater(taxa, 0, moeda)

    def test_valor_zero_e_valido(self):
        resultado = converter(0, "USD", "BRL")
        self.assertEqual(resultado, 0.00)

    # --- Cenários negativos ---

    def test_moeda_origem_invalida_lanca_excecao(self):
        with self.assertRaises(MoedaNaoSuportadaError):
            converter(100, "XYZ", "BRL")

    def test_moeda_destino_invalida_lanca_excecao(self):
        with self.assertRaises(MoedaNaoSuportadaError):
            converter(100, "USD", "XYZ")

    def test_valor_negativo_lanca_excecao(self):
        with self.assertRaises(ValorInvalidoError):
            converter(-50, "USD", "BRL")

    def test_valor_nao_numerico_lanca_excecao(self):
        with self.assertRaises(ValorInvalidoError):
            converter("abc", "USD", "BRL")

    def test_valor_nan_lanca_excecao(self):
        with self.assertRaises(ValorInvalidoError):
            converter("nan", "USD", "BRL")

    def test_valor_infinito_lanca_excecao(self):
        with self.assertRaises(ValorInvalidoError):
            converter("inf", "USD", "BRL")

    def test_valor_gigante_lanca_excecao(self):
        with self.assertRaises(ValorInvalidoError):
            converter("1e400", "USD", "BRL")

    # --- Interface de terminal ---

    def _executar_interface(self, entradas):
        saida = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(saida):
            _entrada_interativa()
        return saida.getvalue()

    def test_interface_exibe_conversao(self):
        saida = self._executar_interface(["usd", "brl", "100"])
        self.assertIn("100 USD = 540.00 BRL", saida)

    def test_interface_exibe_erro_para_entrada_invalida(self):
        saida = self._executar_interface(["XYZ", "BRL", "100"])
        self.assertIn("Erro:", saida)


if __name__ == "__main__":
    unittest.main()
