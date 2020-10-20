from base_type import BaseType
from enum import unique

#Tipo de PCR. 
@unique
class TiposPCR(BaseType):
    CONVENCIONAL = 1
    TEMPO_REAL  = 2

    def describe(self):
        return {
            1: 'PCR Convencional',
            2: 'PCR Em tempo real',
        }.get(self.value, 'Indefinido')