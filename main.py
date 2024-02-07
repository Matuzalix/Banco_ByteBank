from funcionarios import Funcionario

#lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')
    
teste_idade()
