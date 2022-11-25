# -*- coding: utf-8 -*-
"""
CUENTASILOS
Modelo para convertir hojas Excel a DataFrame de pandas

24/10/2022

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pedro.biel@vamanholding.com
"""

import pandas as pd


class Excel2Pandas:
    
    def __init__(self, cwd, excel, worksheets):
        """
        Convierte hojas Excel a DataFrame de pandas.

        Parameters
        ----------
        cwd : str
            Nombre del directorio donde se encuetra la hoja Excel.
        excel : str
            Nombre del fichero Excel.
        worksheets : list
            Lista de hojas Excel a convertir.
        """
        
        self.cwd = cwd
        self.excel = excel
        self.ws = worksheets
        
        self.df = pd.DataFrame()  # pandas DataFrame.
        
    def excel2pandas(self):
        """Convierte hojas Excel a DataFrame de pandas."""
        
        cwd_excel = self.cwd + r'\\' + self.excel
        d = pd.read_excel(cwd_excel, sheet_name=self.ws)  # Diccionario con 
            # los DataFrames.
        df = pd.concat(d)  # Concatena los DataFrames de las keys del 
            # dicccionario.
        df = df.reset_index(drop=True)
    
        return df
    
    def dataframe_silos(self):
        """
        Depura el DataFrame de los silos:
            1. Elimina columna Otro.
            2. Elimina filas con NaN.
            3. Elimina filas con Num_silos == 0.
            4. Convierte Num_silos a int.
        """
        
        df = self.excel2pandas()
        df.drop(['Otro'], axis=1, inplace=True)

        df.dropna(subset=['Num_silos'], inplace=True)
        df.drop(df[df.Num_silos == '--'].index, inplace=True)
        df['Num_silos'] = df['Num_silos'].astype('int')
        
        return df


if __name__ == '__main__':
    
    cwd = r'U:\zz pruebas 01. PEDIDOS CLIENTES'
    excel = 'ÍNDICE PEDIDOS.xlsx'
    worksheets = ['PSM19', 'PSM20', 'PSM21', 'PSM22']
    
    print('mdl_xls2pd:')
    xls2pd = Excel2Pandas(cwd, excel, worksheets)
    df = xls2pd.excel2pandas()
    print(df)
    df = xls2pd.dataframe_silos()
    print(df)
