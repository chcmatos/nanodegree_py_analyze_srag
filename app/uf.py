from enum import Enum, unique

# Sigla da Unidade Federativa onde está
# localizada a unidade de saúde (ou outra fonte 
@unique
class UF(Enum):
    RO = 11
    AC = 12
    AM = 13
    RR = 14
    PA = 15
    AP = 16
    TO = 17
    MA = 21
    PI = 22
    CE = 23
    RN = 24
    PB = 25
    PE = 26
    AL = 27
    SE = 28
    BA = 29
    MG = 31
    ES = 32
    RJ = 33
    SP = 35
    PR = 41
    SC = 42
    RS = 43
    MS = 50
    MT = 51
    GO = 52
    DF = 53

    def describe(self):
        return {
            11: 'Rondônia',
            12: 'Acre',
            13: 'Amazonas',
            14: 'Roraima',
            15: 'Pará',
            16: 'Amapá',
            17: 'Tocantins',
            21: 'Maranhão',
            22: 'Piauí',
            23: 'Ceará',
            24: 'Rio Grande do Norte',
            25: 'Paraíba',
            26: 'Pernambuco',
            27: 'Alagoas',
            28: 'Sergipe',
            29: 'Bahia',
            31: 'Minas Gerais',
            32: 'Espírito Santo',
            33: 'Rio de Janeiro',
            35: 'São Paulo',
            41: 'Paraná',
            42: 'Santa Catarina',
            43: 'Rio Grande do Sul',
            50: 'Mato Grosso do Sul',
            51: 'Mato Grosso',
            52: 'Goiás',
            53: 'Distrito Federal'
        }.get(self.value)

    @classmethod
    def all_describe(cls, arr:list):
        for i in arr:
            yield cls(i).describe()

    @classmethod
    def all_describe_as_list(cls, arr:list):
        return list(cls.all_describe(arr))

    @classmethod
    def all_names(cls, arr:list):
        for i in arr:
            yield cls(i).name

    @classmethod
    def all_names_as_list(cls, arr:list):
        return list(cls.all_names(arr))

    def __str__(self):
        return self.describe()
