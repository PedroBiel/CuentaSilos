# -*- coding: utf-8 -*-
"""
CUENTASILOS
Busca en el directorio
Z:\01. PEDIDOS CLIENTES
los pedidos y cuenta los silos

20/10/2022

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pedro.biel@vamanholding.com
"""


import pandas as pd
import streamlit as st

from data.constantes import Constantes
from src.control.cnt_pedidos import CntDataFramePedidos
from src.control.cnt_graficas import CntGraficas


class MyStreamlit:
    
    def __init__(self):
        """Cuenta los silos de los pedidos SM y hace Data Science."""
        
        constantes = Constantes()
        self.pedidos = constantes.PEDIDOS
        self.txt_pedidos = constantes.WRITE_PEDIDOS
        self.cnt_df_pedidos = CntDataFramePedidos()

        self.set_page_config()
        self.titulo()
        self.df = self.file_upload()
        if self.df is not None:
            self.df = self.dataframe_filtrada_(self.df)
            self.graficas_segun_diametro(self.df)
            self.graficas_segun_cantidad(self.df)
            self.graficas_segun_alturas(self.df)
            self.graficas_segun_alturas_max(self.df)
            self.graficas_segun_alturas_medias(self.df)
            self.version()

    def set_page_config(self):
        """Streamlit page config."""
        
        st.set_page_config(
            page_title='CuentaSilos',
            page_icon=':)',
            layout='wide',
            initial_sidebar_state='expanded',
        )
        
    def titulo(self):
        """DataFrame con los pedios."""
        
        st.title('Cuenta Silos')
        # st.markdown(
        #     """
        #     Cuenta el número de silos del directorio 
        #     'Z:\\01. PEDIDOS CLIENTES' y muestra los resultados organizado por 
        #     diámetros y periodo de tiempo.
        #     """
        #     )
        st.sidebar.title('Selección de pedidos')

    def file_upload(self):
        """Carga el fichero para el estudio de los silos."""

        file = st.sidebar.file_uploader(
            'Selecciona fichero ÍNDICE_PEDIDOS.xlsx en dierctorio Z:\\01. PEDIDOS CLIENTES (Ofitec)',
            type='xlsx'
        )
        if file:

            # d = pd.read_excel(file, sheet_name=['PSM19', 'PSM20', 'PSM21', 'PSM22'])
            d = pd.read_excel(file, sheet_name=None)
            # st.write(d)
            df = pd.concat(d)
            df = df.reset_index(drop=True)
            df.drop(['Otro'], axis=1, inplace=True)
            df.dropna(subset=['Num_silos'], inplace=True)
            df.drop(df[df.Num_silos == '--'].index, inplace=True)
            df['Num_silos'] = df['Num_silos'].astype('int')
            # st.write(df)


            return df

    def seleccion_pedidos(self):
        """
        Selección de pedidos.
        :return: pedidos; str
        """
        
        pedidos = st.sidebar.selectbox('Pedidos:', self.pedidos)
        idx = self.pedidos.index(pedidos)
        st.subheader(self.txt_pedidos[idx])
        
        return pedidos

    def seleccion_clientes(self, df):
        """
        Multiselección de clientes.
        :return:
        """

        clientes_unicos_ordenados = sorted(df.Cliente.unique())
        clientes = st.sidebar.multiselect('Clientes', clientes_unicos_ordenados, clientes_unicos_ordenados)

        return clientes

    def seleccon_modelos(self, df):

        modelos_unicos_ordenados = sorted(df.Modelo.unique())
        modelos = st.sidebar.multiselect('Modelos', modelos_unicos_ordenados, modelos_unicos_ordenados)

        return modelos

    def seleccon_diametros(self, df):

        diametros_unicos_ordenados = sorted(df.Diámetro.unique())
        diametros = st.sidebar.multiselect('Diámetros', diametros_unicos_ordenados, diametros_unicos_ordenados)

        return diametros

    def seleccon_alturas(self, df):

        alturas_unicas_ordenadas = sorted(df.Alturas.unique())
        alturas = st.sidebar.multiselect('Alturas', alturas_unicas_ordenadas, alturas_unicas_ordenadas)

        return alturas

    def seleccon_tolvas(self, df):

        tolvas_unicas_ordenadas = sorted(df.Tolva.unique())
        tolvas = st.sidebar.multiselect('Tolvas', tolvas_unicas_ordenadas, tolvas_unicas_ordenadas)

        return tolvas

    @st.cache
    def dataframe_pedidos(self):
        """
        DataFrame con los datos de los pedidos.
        :return df: pandas DataFrame
        """

        df = self.cnt_df_pedidos.dataframe_silos()

        return df

    @st.cache
    def dataframe_pedidos(self, df):
        """
        DataFrame con los datos de los pedidos.
        :return df: pandas DataFrame
        """

        df = self.cnt_df_pedidos.dataframe_silos(df)

        return df

    def dataframe_filtrada(self):
        """
        DataFrame con los datos filtrados según la selección
        :return df: pandas DataFrame
        """

        # DataFrame filtrada por pedidos PSM.
        seleccion = self.seleccion_pedidos()
        df_pedidos = self.dataframe_pedidos()
        df = self.cnt_df_pedidos.dataframe_silos_filtrada(seleccion, df_pedidos)

        # DataFrame filtrada por clientes.
        clientes = self.seleccion_clientes(df)
        df = df[df.Cliente.isin(clientes)]

        # DataFrame filtrada por modelos.
        modelos = self.seleccon_modelos(df)
        df = df[df.Modelo.isin(modelos)]

        # DataFrame filtrada por diámetros.
        diametros = self.seleccon_diametros(df)
        df = df[df.Diámetro.isin(diametros)]

        # DataFrame filtrada por alturas.
        alturas = self.seleccon_alturas(df)
        df = df[df.Alturas.isin(alturas)]

        # DataFrame filtrada por tolvas.
        tolvas = self.seleccon_tolvas(df)
        df = df[df.Tolva.isin(tolvas)]

        st.subheader('Tabla de pedidos')
        st.write(df)
        st.markdown('#### Estadísticas')
        df_ = pd.DataFrame()
        df_['Num_silos'] = df['Num_silos'].copy()
        df_['Num_silos'] = df_['Num_silos'].astype('int')
        df_['Diámetro'] = df['Diámetro'].copy()
        df_['Diámetro'] = df_['Diámetro'].astype('int')
        df_['Alturas'] = df['Alturas'].copy()
        df_['Alturas'] = df_['Alturas'].astype('int')
        st.write(df_.describe().T)

        return df

    def dataframe_filtrada_(self, df):
        """
        DataFrame con los datos filtrados según la selección
        :return df: pandas DataFrame
        """

        # DataFrame filtrada por pedidos PSM.
        seleccion = self.seleccion_pedidos()
        df_pedidos = self.dataframe_pedidos(df)
        df = self.cnt_df_pedidos.dataframe_silos_filtrada(seleccion, df_pedidos)

        # DataFrame filtrada por clientes.
        clientes = self.seleccion_clientes(df)
        df = df[df.Cliente.isin(clientes)]
        # st.write(df)

        # DataFrame filtrada por modelos.
        modelos = self.seleccon_modelos(df)
        df = df[df.Modelo.isin(modelos)]

        # DataFrame filtrada por diámetros.
        diametros = self.seleccon_diametros(df)
        df = df[df.Diámetro.isin(diametros)]

        # DataFrame filtrada por alturas.
        alturas = self.seleccon_alturas(df)
        df = df[df.Alturas.isin(alturas)]

        # DataFrame filtrada por tolvas.
        tolvas = self.seleccon_tolvas(df)
        df = df[df.Tolva.isin(tolvas)]

        st.subheader('Tabla de pedidos')
        st.write(df)
        st.markdown('#### Estadísticas')
        df_ = pd.DataFrame()
        df_['Num_silos'] = df['Num_silos'].copy()
        df_['Num_silos'] = df_['Num_silos'].astype('int')
        df_['Diámetro'] = df['Diámetro'].copy()
        df_['Diámetro'] = df_['Diámetro'].astype('int')
        df_['Alturas'] = df['Alturas'].copy()
        df_['Alturas'] = df_['Alturas'].astype('int')
        st.write(df_.describe().T)

        return df

    def graficas_segun_diametro(self, df):
        """Dibuja las gráficas de barras y de tarta del DataFrame df según diámetro."""

        st.subheader('Diagramas')
        st.markdown('#### Silos según diámetro')
        cnt_graficas = CntGraficas(df)
        col1, col2 = st.columns((2, 1))
        with col1:
            cnt_graficas.grafica_silos_diametro()
        with col2:
            cnt_graficas.grafica_tarta_silos_diametro()

    def graficas_segun_cantidad(self, df):
        """Dibuja las gráficas de barras y de tarta del DataFrame df según cantidad."""

        cnt_graficas = CntGraficas(df)
        st.markdown('#### Silos según cantidad')
        cnt_graficas.grafica_silos_cantidad()

    def graficas_segun_alturas(self, df):
        """Dibuja las gráficas de barras del DataFrame df según alturas."""

        cnt_graficas = CntGraficas(df)
        st.markdown('#### Alturas según diámetro')
        cnt_graficas.grafica_alturas()

    def graficas_segun_alturas_max(self, df):
        """Dibuja las gráficas de barras del DataFrame df según alturas máximas."""

        cnt_graficas = CntGraficas(df)
        st.markdown('#### Alturas máximas según diámetro')
        cnt_graficas.grafica_alturas_max()

    def graficas_segun_alturas_medias(self, df):
        """Dibuja las gráficas de barras del DataFrame df según alturas medias."""

        cnt_graficas = CntGraficas(df)
        st.markdown('#### Alturas medias según diámetro')
        cnt_graficas.grafica_alturas_medias()

    def version(self):
        """Versión de las librerías."""

        st.subheader('Versión')
        with st.expander('CuentaSilos 0.0.0'):
            st.markdown(
                """
                CuentaSilos | 0.0.0 | Primera edición
                
                | Librería | Versión |
                | --- | --- |
                | pandas | 1.5.1 |
                | python | 3.9.13 |
                | matplotlib | 3.5.2 |
                | numpy | 1.23.4 |
                | streamlit | 1.13.0 |
                """)


if __name__ == '__main__':

    myst = MyStreamlit()
    # myst.set_page_config()
    # myst.titulo()
    # st.write('hola')
    # print(df)
    # st.dataframe(df)
    # myst.sidebar()
    # myst.seleccion_pedidos()
    # myst.dataframe()
    
    




