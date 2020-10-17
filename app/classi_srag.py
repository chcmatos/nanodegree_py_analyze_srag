from enum import Enum, unique

@unique
class SRAG(Enum):
    INFLUENZA = 1
    OUTRO_VIRUS_RESP = 2
    OUTRO_AGENTE_ETIOLOG = 3
    NAO_ESPECIFICADO = 4
    IGNORADO = 9



    def describe(self):
        return {
                1: 'SRAG por\nInfluenza', 
                2: 'SRAG por\noutros vírus\nrespiratórios',
                3: 'SRAG por\noutros agentes\netiológicos',
                4: 'SRAG não\nespecificado'
                }.get(self.value, 'Ignorados')

    @classmethod
    def all_describe(cls, arr:list):
        for i in arr:
            yield cls(i).describe()

    @classmethod
    def all_describe_as_list(cls, arr:list):
        return list(cls.all_describe(arr))

    def __str__(self):
        return self.describe()
