from base_type import BaseType
from enum import unique


# Meses
@unique
class MES(BaseType):
    JAN = 1
    FEV = 2
    MAR = 3
    ABR = 4
    MAI = 5
    JUN = 6
    JUL = 7
    AGO = 8
    SET = 9
    OUT = 10
    NOV = 11
    DEZ = 12

    def describe(self):
        return {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
            6: 'Junho',
            7: 'Julho',
            8: 'Agosto',
            9: 'Setembro',
            10: 'Outubro',
            11: 'Novembro',
            12: 'Dezembro',
        }.get(self.value)
