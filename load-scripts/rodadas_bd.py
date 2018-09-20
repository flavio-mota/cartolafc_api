#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:15:23 2018

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

url = "https://api.cartolafc.globo.com/rodadas"
try:
    data = requests.get(url).json()
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_rodadas CASCADE""")

    print("Carregando os dados das rodadas - - - - - Aguarde")
    for item in data:
        result = []
        
        rodada_id = item['rodada_id']
        inicio = item['inicio']
        fim = item['fim']
        result = [rodada_id, inicio, fim]
        cur.execute("""INSERT into cartola_fc.tb_rodadas
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