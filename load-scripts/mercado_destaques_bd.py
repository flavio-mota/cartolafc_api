#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:45:33 2018

@author: flaviomota
"""

import requests
import psycopg2
import json

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Database Connected")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/mercado/destaques"
try:
    #response = urllib.urlopen(url)
    #data = json.loads(response.read())
    #print data
    data = requests.get(url).json()
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_mercado_destaques""")
    for item in data:
        result = []
        
        atleta_id = item['Atleta']['atleta_id']
        nome = item['Atleta']['nome']
        apelido = item['Atleta']['apelido']
        foto = item['Atleta']['foto']
        preco_editorial = item['Atleta']['preco_editorial']
        escalacoes = item['escalacoes']
        clube = item['clube']
        escudo_clube = item['escudo_clube']
        posicao = item['posicao']
        result = [atleta_id, nome, apelido, foto, preco_editorial, escalacoes, 
                  clube, escudo_clube, posicao]

        cur.execute("""INSERT into cartola_fc.tb_mercado_destaques 
                       VALUES
                       ( %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s
                       )""",(result))
        conn.commit()
    cur.close()
    
except IOError as io:
    print("cannot open")
    


