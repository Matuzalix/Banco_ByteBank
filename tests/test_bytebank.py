import pytest

from funcionarios import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/3/2000" #Given - Contexto
        esperado = 23

        funcionario_test = Funcionario('Test', entrada, 1111)
        resultado = funcionario_test.idade() #When - Ação

        assert resultado == esperado #Then - Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "15/03/1985", entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario("Teste", "21/08/2000", entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exeption(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario("Teste", "21/08/2000", entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
