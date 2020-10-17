import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from obesidade import Obesidade
from tipos_pcr import TiposPCR
from uf import UF
from classi_srag import SRAG


class Analyze:

    def __init__(self, file_name: str, delimiter: str):
        self.file_name = file_name
        self.delimiter = delimiter

    def __sum_column_values_by_cond__(self, column_name: str, condValue: any):
        try:
            df = pd.read_csv(
                self.file_name, delimiter=self.delimiter, usecols=[column_name])
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

    def histograma_classificar_SRAG(self):
        try:
            df = pd.read_csv(self.file_name, delimiter=self.delimiter, usecols=[
                             'CLASSI_FIN', 'DT_ENCERRA'])
            df = df[df['DT_ENCERRA'].str.len() > 0]
            classi_fin = df.groupby(df.iloc[:, 0]).sum()['CLASSI_FIN']

            y = classi_fin.values.tolist()
            x = classi_fin.index.values.tolist()
            plt.bar(x, height=y)
            plt.xticks(x, SRAG.all_describe(x))
            plt.yticks(self.__fill_interval_range__(y))

            maxSRAG = SRAG(x[y.index(max(y))])
            result = ["Podemos identificar que a maioria\ndos casos foram classificados como\n" +
                      maxSRAG.describe() + " (" + str(max(y)) + " casos)"]

            plt.legend(result)
            plt.title('SRAG - Diagnóstico final do caso suspeito')
            plt.xlabel('Classificação')
            plt.ylabel('Número de casos')
            plt.show()
            return result.pop()
        finally:
            del df
            del classi_fin

    def histograma_paciente_por_UF(self):
        try:
            df = pd.read_csv(
                self.file_name, delimiter=self.delimiter, usecols=['SG_UF_NOT'])
            classi_fin = df.groupby(df.iloc[:, 0]).sum()['SG_UF_NOT']
            y = classi_fin.values.tolist()
            x = classi_fin.index.values.tolist()
            plt.bar(x, height=y)
            plt.xticks(x, UF.all_names(x))
            plt.yticks(self.__fill_interval_range__(y))

            maxUF = UF(x[y.index(max(y))])
            result = ["Podemos identificar que a maioria\n" +
                      "dos casos ocorreram em\n" +
                      maxUF.describe() + " (" + str(max(y)) + " casos)"]
            plt.legend(result)

            plt.title('Distribuição geográfica por unidade federativa (UF)')
            plt.xlabel('Unidade Federativa')
            plt.ylabel('Número de casos')
            plt.show()
            return result.pop()
        finally:
            del df
            del classi_fin

    def total_aprox_por_obesidade(self, tipo: Obesidade):
        return self.__sum_column_values_by_cond__('OBESIDADE', tipo.value)

    def total_por_PCR(self, tipo: TiposPCR):
        return self.__sum_column_values_by_cond__('TIPO_PCR', tipo.value)


def main():
    a = Analyze('../doc/influd18_limpo-final.csv', ';')
    print('Iniciando Analise do arquivo ', a.file_name)

    print('4 - Qual a quantidade de pessoas que estão acima do IMC ideal?',
          '\n\tResp: ', a.total_aprox_por_obesidade(Obesidade.SIM), 'pessoa(s).\n')

    print('5 - Faça um histograma da variável CLASSI_FIN. O que esse histograma nos diz?\n',
          '\n\tResp: ', a.histograma_classificar_SRAG(), '\n')

    print('6 - Quantas pessoas realizaram PCR do tipo convencional?',
          '\n\tResp: ', a.total_por_PCR(TiposPCR.CONVENCIONAL), 'pessoa(s).\n')

    print('7 -Faça o histograma da distribuição geográfica por unidade federativa\n(UF) dos pacientes com desta base de dados.',
          '\n\tResp: ', a.histograma_paciente_por_UF(), '\n')


if __name__ == "__main__":
    main()
