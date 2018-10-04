#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:15:52 2018

@author: flaviomota
"""

import requests
import psycopg2


conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Conectado ao banco")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/atletas/mercado"
try:
    data = requests.get(url).json()
        
    print("Carregando os dados das posições dos atletas - - - - - Aguarde")
    for posicao in data['posicoes']:
        result = []
        
        id_posicao = data['posicoes'][posicao]['id']
        nome = data['posicoes'][posicao]['nome']
        abreviacao = data['posicoes'][posicao]['abreviacao']

        result = [id_posicao, nome, abreviacao]
        cur.execute("""INSERT into cartola_fc.tb_posicoes_atleta
                       VALUES
                       ( %s,
                         %s,
                         %s
                       )""",(result))
        conn.commit()
        
    cur.close()
    print("Sucesso! Inicializando próxima carga....")
except IOError as io:
    print("Erro")