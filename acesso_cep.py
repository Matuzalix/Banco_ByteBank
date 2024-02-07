from idlelib.multicall import r
import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP Inválido!')

    def __str__(self):
        return self.cep_format()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_format(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
