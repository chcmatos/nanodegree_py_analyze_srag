# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from enum import Enum

# class TiposPCR(Enum):
#     CONVENCIONAL = 1
#     TEMPO_REAL = 2


# class Obesidade(Enum):
#     SIM = 1
#     NAO = 2
#     IGNORADO = 9


# FILE_NAME = 'influd18_limpo-final.csv'
# DELIMITER = ';'


# def __sumColumnValuesByCond__(column_name: str, condValue: any):
#     try:
#         df = pd.read_csv(FILE_NAME, delimiter=DELIMITER, usecols=[column_name])
#         return np.sum(df[column_name] == condValue)
#     finally:
#         del df


# def _histogramBy(column_name: str, title: str, xl: str, yl: str):
#     # try:
#     df = pd.read_csv(FILE_NAME, delimiter=DELIMITER, usecols=[column_name])
#     print(df)
#         # df = df.pivot_table(index=[column_name], aggfunc='size')
#         # plt.hist(df, bins=df.size)
#     plt.hist(df)
#     plt.title(title)
#     plt.xlabel(xl)
#     plt.ylabel(yl)
#     plt.show()
#     # finally:
#         # del df


# def histogramForCLASSIFIN():
#     _histogramBy(
#         'CLASSI_FIN',
#         'Classificacao Diagnóstico SRAG',
#         'Tipo de SRAG',
#         'Número de casos')


# def histogramForUF():
#     _histogramBy(
#         'SG_UF_NOT',
#         'Classificacao pacientes por UF',
#         'Código da UF',
#         'Quantidade de pacientes')





# print('4 - Qual a quantidade de pessoas que estão acima do IMC ideal? Utilize a coluna OBESIDADE como uma proximadamente?',
#       '\n\tResp: ', totalAproxOBESIDADE(Obesidade.SIM), 'pessoa(s).\n')

# #print('5 - Faça um histograma da variável CLASSI_FIN. O que esse histograma nos diz?')
# #histogramForCLASSIFIN()

# print('6 - Quantas pessoas realizaram PCR do tipo convencional?',
#       '\n\tResp: ', totalPCR(TiposPCR.CONVENCIONAL), 'pessoa(s).\n')

# print('7 - Faça o histograma da distribuição geográfica por unidade federativa (UF) dos pacientes desta base de dados.')
# histogramForUF()
