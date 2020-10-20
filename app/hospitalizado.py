from base_type import BaseType
from enum import unique

#Paciente foi hospitalizado
@unique
class Hospitalizado(BaseType):
    SIM = 1
    NAO = 2
    IGNORADO = 9

    def describe(self):
        return {
            1: 'Paciente foi hospitalizado',
            2: 'Paciente não foi hospitalizado',
            9: 'Indefinido'
        }.get(self.value, 'Indefinido')
