from enum import Enum, unique

#Tipo de PCR. 
@unique
class TiposPCR(Enum):
    CONVENCIONAL = 1
    TEMPO_REAL  = 2

    def describe(self):
        return {
            1: 'PCR Convencional',
            2: 'PCR Em tempo real',
        }.get(self.value, 'Indefinido')

    def __str__(self):
        return self.describe()