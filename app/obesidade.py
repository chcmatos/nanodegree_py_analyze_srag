from base_type import BaseType
from enum import unique

#Paciente possui obesidade
@unique
class Obesidade(BaseType):
    SIM = 1
    NAO = 2
    IGNORADO = 9

    def describe(self):
        return {
            1: 'Paciente possui obesidade',
            2: 'Paciente não possui obesidade',
            9: 'Não foi avaliado'
        }.get(self.value, 'Indefinido')
