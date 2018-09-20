#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:24:34 2018

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

url = "https://api.cartolafc.globo.com/patrocinadores"
try:
    data = requests.get(url).json()
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_patrocinadores""")

    print("Carregando dados dos patrocinadores - - - - - Aguarde")
    for item in data:
        result = []
        
        liga_editorial_id = data[item]['liga_editorial_id']
        liga_id = data[item]['liga_id']
        tipo_ranking = data[item]['tipo_ranking']
        url_link = data[item]['url_link']
        img_background = data[item]['img_background']
        img_marca_patrocinador = data[item]['img_marca_patrocinador']
        img_marca_patrocinador_png = data[item]['img_marca_patrocinador_png']
        nome = data[item]['nome']
        optin = data[item]['optin']
        destaque = data[item]['destaque']
        nome_patrocinador = data[item]['nome_patrocinador']
        descricao = data[item]['descricao']
        url_flamula_svg = data[item]['url_flamula_svg']
        url_flamula_png = data[item]['url_flamula_png']
        total_times	= data[item]['total_times']
        result = [liga_editorial_id,liga_id,tipo_ranking,url_link,
                  img_background,img_marca_patrocinador,img_marca_patrocinador_png,
                  nome,optin,destaque,nome_patrocinador,descricao,url_flamula_svg,
                  url_flamula_png,total_times]
        cur.execute("""INSERT into cartola_fc.tb_patrocinadores
                       VALUES
                       ( %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s,
                         %s,
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
    print("Sucesso! Inicializando próxima carga....")
except IOError as io:
    print("Erro")