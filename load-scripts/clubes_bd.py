#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:34:04 2018

@author: flaviomota
"""

import requests
import psycopg2
import json

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Conectado ao banco")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/clubes"
try:
    
    data = requests.get(url).json()
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_clubes CASCADE""")

    print("Carregando dados dos clubes - - - - - Aguarde")
    for item in data:
        result = []
        
        id_clube = data[item]['id']
        nome = data[item]['nome']
        abreviacao = data[item]['abreviacao']
        escudo_60x60 = data[item]['escudos']['60x60']
        escudo_45x45 = data[item]['escudos']['45x45']
        escudo_30x30 = data[item]['escudos']['30x30']
        if 'posicao' not in data[item]:
            posicao = None
        else: 
            posicao = data[item]['posicao']
        result = [id_clube, nome, abreviacao, posicao, escudo_60x60, escudo_45x45, escudo_30x30]
        cur.execute("""INSERT into cartola_fc.tb_clubes
                       VALUES
                       ( %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s
                       )""",(result))
        conn.commit()
    cur.close()
    print("Sucesso! Inicializando próxima carga....")
except IOError as io:
    print("Erro")