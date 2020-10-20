import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from base_type import BaseType
from hospitalizado import Hospitalizado
from obesidade import Obesidade
from tipos_pcr import TiposPCR
from uf import UF
from mes import MES
from classi_srag import SRAG

pd.options.mode.chained_assignment = None  # default='warn'

class Analyze:

    def __init__(self, file_name: str, delimiter: str):
        self.file_name = file_name
        self.delimiter = delimiter

    def __sum_column_values_by_cond__(self, column_name: str, condValue: any):
        try:
            df = pd.read_csv(self.file_name, delimiter=self.delimiter, usecols=[column_name])
            return np.sum(df[column_name] == condValue)
        finally:
            del df

    def __interval_extract__(self, target):
        new_list = target.copy()
        new_list.sort()
        l = len(new_list)
        i = 0
        arr = []
        while((i + 1) < l):
            arr.append(new_list[i + 1] - new_list[i])
            i += 1
        return sum(arr) / len(arr)

    def __fill_interval_range__(self, arr):
        return list(range(
            int(min(arr)),
            int(max(arr)),
            int(self.__interval_extract__(arr))))

    def __histograma_base__(self, columns: list, title: str, xlabel: str, ylabel: str, base_type: BaseType = None, xticks_labels=None, legend: str = None, df_filter=None):
        try:
            df = pd.read_csv(self.file_name, delimiter=self.delimiter, usecols=columns)

            if(df_filter != None):
                df = df_filter(df)

            y = df.values.tolist()
            x = df.index.values.tolist()

            plt.bar(x, height=y)

            if(xticks_labels != None):
                plt.xticks(x, xticks_labels(x))
            else:
                plt.xticks(x)

            plt.yticks(self.__fill_interval_range__(y))

            btype = base_type(int(x[y.index(max(y))]))
            result = [legend + btype.describe() + " (" + str(max(y)) + " casos)"]

            plt.legend(result)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
            return result.pop()
        finally:
            del df

    def histograma_classificar_SRAG(self):
        def df_filter(df):
            df = df[df['DT_ENCERRA'].str.len() > 0]
            df = df.groupby('CLASSI_FIN').size()
            return df
        return self.__histograma_base__(
            columns=['CLASSI_FIN', 'DT_ENCERRA'],
            title='SRAG - Diagnóstico final do caso suspeito',
            xlabel='Classificação',
            ylabel='Número de casos',
            base_type=SRAG,
            xticks_labels=SRAG.all_describe,
            legend='Podemos identificar que a maioria\ndos casos foram classificados como\n',
            df_filter=df_filter
        )

    def histograma_paciente_por_UF(self):
        def df_filter(df):
            df = df.groupby('SG_UF_NOT').size()
            return df
        return self.__histograma_base__(
            columns=['SG_UF_NOT'],
            title='Distribuição geográfica por unidade federativa (UF)',
            xlabel='Unidade Federativa',
            ylabel='Número de casos',
            base_type=UF,
            xticks_labels=UF.all_names,
            legend='Podemos identificar que a maioria\ndos casos ocorreram em\n',
            df_filter=df_filter)

    def histograma_paciente_por_mes_internacao(self):
        def df_filter(df):
            df = df[(df['HOSPITAL'] == Hospitalizado.SIM.value) & (df['DT_INTERNA'].str.len() > 0)]
            df['MES'] = df['DT_INTERNA'].str.slice(3, 5)
            df = df.groupby('MES').size()
            return df
        return self.__histograma_base__(
            columns=['HOSPITAL', 'DT_INTERNA'],
            title='Distribuição casos (de hospitalização) por mês de internação',
            xlabel='Mês de internação',
            ylabel='Número de casos',
            base_type=MES,
            xticks_labels=MES.all_names,
            legend='Podemos identificar que a maioria\ndos casos ocorreram em\n',
            df_filter=df_filter)

    def total_aprox_por_obesidade(self, tipo: Obesidade):
        return self.__sum_column_values_by_cond__('OBESIDADE', tipo.value)

    def total_por_PCR(self, tipo: TiposPCR):
        return self.__sum_column_values_by_cond__('TIPO_PCR', tipo.value)

    def media_internacao_SRAG_no_ano(self, ano: int):
        df = pd.read_csv(self.file_name, delimiter=self.delimiter, usecols=['CLASSI_FIN', 'HOSPITAL', 'DT_INTERNA'])
        df = df[(df['HOSPITAL'] == Hospitalizado.SIM.value) & (df['CLASSI_FIN'] != SRAG.IGNORADO.value) & (pd.to_numeric(df['DT_INTERNA'].str.slice(6, 10)) == ano)]
        df = df['DT_INTERNA']        
        y_size = df.size
        m_size = int(y_size / 12)
        d_size = int(y_size / 365)
        return "No ano de {year} ocorreram {y_size} internações, aproximadamente {m_size} por mês, {d_size} por dia.".format(year=ano, y_size=y_size, m_size=m_size, d_size=d_size)


def main():
    a = Analyze('../doc/influd18_limpo-final.csv', ';')
    print('Iniciando Analise do arquivo ', a.file_name)

    print('4 - Qual a quantidade de pessoas que estão acima do IMC ideal?',
          '\n\tResp.: ', a.total_aprox_por_obesidade(Obesidade.SIM), 'pessoa(s).\n')

    print('5 - Faça um histograma da variável CLASSI_FIN. O que esse histograma nos diz?\n',
          '\n\tResp.: ', a.histograma_classificar_SRAG(), '\n')

    print('6 - Quantas pessoas realizaram PCR do tipo convencional?',
          '\n\tResp.: ', a.total_por_PCR(TiposPCR.CONVENCIONAL), 'pessoa(s).\n')

    print('7 - Faça o histograma da distribuição geográfica por unidade federativa\n(UF) dos pacientes com desta base de dados.',
          '\n\tResp.: ', a.histograma_paciente_por_UF(), '\n')

    print('8 - Faça um histograma por mês de internação dos pacientes?',
          '\n\tResp.: ', a.histograma_paciente_por_mes_internacao(), '\n')

    # print('9 - É possível identificar o número de mortes nesta base de dados?\n',
    #       'Se sim, coloque o número de mortos por SRAG em 2018 na sua frequência absoluta\n',
    #       'e na sua frequência relativa. Se não, qual estratégia o grupo utilizaria para\n',
    #       'conseguir estes números de forma real ou por uma aproximação boa?\n',
    #       '\n\tResp.: ', '\n')

    print('10 - Qual a quantidade média de internações por SRAG no ano de 2018?\n',
          '\n\tResp.: ', a.media_internacao_SRAG_no_ano(2018), '\n')


if __name__ == "__main__":
    main()
