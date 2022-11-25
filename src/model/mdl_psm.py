# -*- coding: utf-8 -*-
"""
CUENTASILOS
Modelo para filtrar el DataFrame de pandas según PSM

25/10/2022

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pedro.biel@vamanholding.com
"""

# from src.control.cnt_pedidos import CntDataFramePedidos
import numpy as np


class PSM:
    
    def __init__(self, psm, df_psm):
        """
        Filtra el DataFrame con todos los pedidos por el pedido SM psm,

        Parameters
        ----------
        psm : str
            Pedido SM por año.
        df_psm : pandas DataFrame
            pandas DataFrame a filtrar
        """
        
        # self.psm = psm

        # self.cnt_df_pedidos = CntDataFramePedidos()

        self.filtro = psm
        self.df_filtrar = df_psm
        
    def get_dataframe(self):
        """Getter del DataFrame."""
        
        df = self.df_filtrar
        
        return df
        
    def filtra_psm(self):
        """
        Filtra el DataFrame según por pedidos SM.

        Returns
        -------
        df : DataFrame
            DataFrame con los datos filtrados.

        """


        df_filtrar = self.get_dataframe()
        df1, df2 = np.array_split(df_filtrar, 2)
        df21, df22 = np.array_split(df2, 2)

        if self.filtro == 'Todos':
            df = df_filtrar
        elif self.filtro == 'Segunda mitad':
            df = df2
        elif self.filtro == 'Último cuarto':
            df = df22
        else:
            df = df_filtrar[df_filtrar.Pedido.str.contains(self.filtro)]

        return df


if __name__ == '__main__':

    import pandas as pd

    pedidos = ['PSM19', 'PSM20', 'PSM21', 'PSM22']
    d = {
        'Pedido': ['PSM19', 'PSM20', 'PSM21', 'PSM22'],
        'col': [1, 2, 3, 4]
    }
    df = pd.DataFrame(d)
    print(df, '\n')

    for pedido in pedidos:
        psm = PSM(pedido, df)
        df_filtro = psm.filtra_psm()
    
        print(pedido)
        print(df_filtro, '\n')
        
