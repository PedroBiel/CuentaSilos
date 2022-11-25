# -*- coding: utf-8 -*-
"""
CUENTASILOS
Modelo para crear nuevas columnas de DataFrame de pedidos.
Las nuevas columans son Modelo, Dimámtero, Alturas

09/11/2022

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pedro.biel@vamanholding.com
"""

import pandas as pd

class ModeloDiametroAlturas:

    def __init__(self, df):
        """
        Crea nuevas columnas de DataFrame de pedidos.
        :param df: pandas DataFrame
        """

        self.df = df

    def dataframe_nuevas_columnas(self):
        """
        DataFrame con las nuevas columnas
        :return df: pandas DataFrame
        """

        s_modelo = self.df.Modelo_silo.str[0]
        s_diametro = self.df.Modelo_silo.str[1:3]
        s_alturas = self.df.Modelo_silo.str[3:5]
        s_tolva = self.df.Modelo_silo.str[6:]
        s_tolva.loc[s_tolva == ''] = '--'
        self.df['Modelo'] = s_modelo
        self.df['Diámetro'] = s_diametro
        self.df['Alturas'] = s_alturas
        self.df['Tolva'] = s_tolva

        return self.df.copy()


if __name__ == '__main__':

    d = {
        'col': [1, 2, 3],
        'Modelo_silo': ['I0408-45', 'C1512', 'N0505-45']
    }
    df = pd.DataFrame(d)

    mda = ModeloDiametroAlturas(df)
    df_nuevo = mda.dataframe_nuevas_columnas()
    print(df_nuevo)
