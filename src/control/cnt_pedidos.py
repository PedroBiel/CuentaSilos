# -*- coding: utf-8 -*-
"""
CUENTASILOS
Controlador de la lista de subdirectorios y de la lista de fecha de creación

21/10/2022

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pedro.biel@vamanholding.com
"""


from data.constantes import Constantes
from src.model.mdl_xls2pd import Excel2Pandas
from src.model.mdl_psm import PSM
from src.model.mdl_modelodiametroalturas import ModeloDiametroAlturas


class CntDataFramePedidos:
    """Controlador de los DataFrame con los valores de los pedidos."""
    
    def __init__(self):
        """
        Inicializador del controlador de los DataFrames con los valores de los pedidos.
        """
        
        self.constantes = Constantes()
    
    def dataframe_silos_(self):
        """
        DataFrame de los pedidos.
        Lectura de datos según datos de constantes.
        """
           
        cwd = self.constantes.CWD
        excel = self.constantes.EXCEL
        worksheets = self.constantes.LIST_WS_INDICE_PEDIDOS
        excel2pandas = Excel2Pandas(cwd, excel, worksheets)
        df1 = excel2pandas.dataframe_silos()
        mda = ModeloDiametroAlturas(df1)
        df2 = mda.dataframe_nuevas_columnas()

        return df2

    def dataframe_silos(self, df):
        """DataFrame de los pedidos."""

        mda = ModeloDiametroAlturas(df)
        df1 = mda.dataframe_nuevas_columnas()

        return df1

    def dataframe_silos_filtrada(self, filtro, df_filtrar):
        """
        DataFrame filtrada según filtro.
        :param filtro: str; filtro seleccionado
        :param df_filtrar: DataFrame con los datos a filtrar
        :return df: pandas DataFrame
        """

        psm = PSM(filtro, df_filtrar)
        df = psm.filtra_psm()

        return df


if __name__ == '__main__':
    
    print('cnt_pedidos:')
    df_pedidos = CntDataFramePedidos()
    df = df_pedidos.dataframe_silos()
    print(df)
