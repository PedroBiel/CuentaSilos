"""
CUENTASILOS
Controlador de las gráficas de resultados

23/11/2022

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pedro.biel@vamanholding.com
"""


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


class CntGraficas:
    """Controlador de las gráficas de resultados."""

    def __init__(self, df):
        """
        Inizializador del controlador de los gráficos de resultados.
        :param df: pandas DataFrame
        """
        self.df = df
        plt.style.use('dark_background')

    def grafica_silos_diametro(self):
        """Gráfica de barras según diámetro."""

        try:
            df_grouped = self.df.groupby('Diámetro')['Num_silos'].sum()
            fig, ax = plt.subplots(figsize=(15, 6.6))
            ax = df_grouped.plot.bar(xlabel='Diámetro', ylabel='Cantidad de silos', color='b')
            ax.set_title('Cantidad de silos según diámetro')
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() * 1.01, p.get_height() * 1.02))
            st.pyplot(fig)
        except Exception as e:
            print(e)

    def grafica_tarta_silos_diametro(self):
        """Gráfica de tarta según diámetro."""

        try:
            df_grouped = self.df.groupby('Diámetro')['Num_silos'].sum()
            fig, ax = plt.subplots(figsize=(5, 5))
            df_grouped.plot.pie(ylabel='', startangle=90, counterclock=False)
            st.pyplot(fig)
        except Exception as e:
            print(e)

    def grafica_silos_cantidad(self):
        """Gráfica de barras según cantidad."""

        try:
            num_diam = len(pd.unique(self.df.Diámetro))
            df_grouped = self.df.groupby('Diámetro')['Num_silos'].sum().nlargest(num_diam)
            fig, ax = plt.subplots(figsize=(15, 6))
            ax = df_grouped.plot.bar(xlabel='Diámetro', ylabel='Cantidad de silos', color='g')
            ax.set_title('Silos ordenados por cantidad')
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() * 1.01, p.get_height() * 1.02))
            st.pyplot(fig)
        except Exception as e:
            print(e)

    def grafica_alturas(self):
        """Gráfica de barras con las alturas de cada silo."""

        try:
            df_diam_alt = self.df[['Diámetro', 'Alturas']].sort_values(by='Diámetro')
            df_diam_alt['Diámetro'] = df_diam_alt['Diámetro'].astype(int)
            df_diam_alt['Alturas'] = df_diam_alt['Alturas'].astype(int)
            df_diam_alt.set_index('Diámetro', inplace=True)
            fig, ax = plt.subplots(figsize=(15, 6))
            ax = df_diam_alt['Alturas'].plot.bar(xlabel='Diámetro', ylabel='Alturas', color='y')
            ax.set_title('Alturas  según diámetro')
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() * 1.01, p.get_height() * 1.02))
            st.pyplot(fig)
        except Exception as e:
            print(e)

    def grafica_alturas_max(self):
        """Gráfica de barras con las alturas máximas de cada silo."""

        try:
            df_diam_alt = self.df[['Diámetro', 'Alturas']].sort_values(by='Diámetro')
            df_diam_alt_max = df_diam_alt.groupby('Diámetro').max().reset_index()
            df_diam_alt_max['Diámetro'] = df_diam_alt_max['Diámetro'].astype(int)
            df_diam_alt_max['Alturas'] = df_diam_alt_max['Alturas'].astype(int)
            df_diam_alt_max.set_index('Diámetro', inplace=True)
            fig, ax = plt.subplots(figsize=(15, 6))
            ax = df_diam_alt_max['Alturas'].plot.bar(xlabel='Diámetro', ylabel='Alturas', color='orange')
            ax.set_title('Alturas máximas según diámetro')
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() * 1.01, p.get_height() * 1.02))
            st.pyplot(fig)
        except Exception as e:
            print(e)

    def grafica_alturas_medias(self):
        """Gráfica de barras con las alturas medias de cada silo."""

        try:
            df_diam_alt = self.df[['Diámetro', 'Alturas']].sort_values(by='Diámetro')
            df_diam_alt['Diámetro'] = df_diam_alt['Diámetro'].astype(int)
            df_diam_alt['Alturas'] = df_diam_alt['Alturas'].astype(int)
            df_diam_alt_mean = df_diam_alt.groupby('Diámetro').mean().reset_index()
            df_diam_alt_mean.set_index('Diámetro', inplace=True)
            fig, ax = plt.subplots(figsize=(15, 6))
            ax = df_diam_alt_mean['Alturas'].plot.bar(xlabel='Diámetro', ylabel='Alturas', color='r')
            ax.set_title(f'Alturas medias según diámetro', fontsize=20)
            for p in ax.patches:
                ax.annotate(str(round(p.get_height(), 1)), (p.get_x() * 1.01, p.get_height() * 1.02))
            st.pyplot(fig)
        except Exception as e:
            print(e)
