# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:21:26 2022

@author: pbiel
"""


class Constantes:
    """Constantes empleadas en el código."""
    
    # CWD = r'Z:\01. PEDIDOS CLIENTES'  # Directorio de los pedidos.
    CWD = r'U:\zz pruebas 01. PEDIDOS CLIENTES'  # Directorio de los pedidos.
    EXCEL = 'ÍNDICE PEDIDOS.xlsx'  # Hoja Excel con los pedidos
    LIST_WS_INDICE_PEDIDOS = ['PSM19', 'PSM20', 'PSM21', 'PSM22']  # Lista de 
        # las hojas Excel de los pedidos.
    PEDIDOS = ['Todos', 'PSM19', 'PSM20', 'PSM21', 'PSM22', 'Segunda mitad', 'Último cuarto']  #  Pedidos a
        # seleccionar para visualizar.
    WRITE_PEDIDOS = [
            'Todos los pedidos',
            'Pedidos PSM19',
            'Pedidos PSM20',
            'Pedidos PSM21',
            'Pedidos PSM22',
            'Segunda mitad de los silos pedidos',
            'Último cuarto de los silos pedidos'
            ]  #  Texto de los medidos seleecionados,