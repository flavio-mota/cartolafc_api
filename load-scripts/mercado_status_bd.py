#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:26:16 2018

@author: flaviomota
"""


import requests
import psycopg2
import json
from datetime import date

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Conectado ao banco")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/mercado/status"
try:

    data = requests.get(url).json()
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_mercado_status""")

    print("Carregando status do mercado - - - - - Aguarde")

    result = []
    
    rodada_atual = data['rodada_atual']
    status_mercado = data['status_mercado']
    esquema_default_id = data['esquema_default_id']
    cartoleta_inicial = data['cartoleta_inicial']
    max_ligas_free = data['max_ligas_free']
    max_ligas_pro = data['max_ligas_pro']
    max_ligas_matamata_free = data['max_ligas_matamata_free']
    max_ligas_matamata_pro = data['max_ligas_matamata_pro']
    max_ligas_patrocinadas_free = data['max_ligas_patrocinadas_free']
    max_ligas_patrocinadas_pro_num = data['max_ligas_patrocinadas_pro_num']
    game_over = data['game_over']
    temporada = data['temporada']
    reativar = data['reativar']
    exibe_sorteio_pro = data['exibe_sorteio_pro']
    times_escalados = data['times_escalados']
    fechamento_dia = data['fechamento']['dia']
    fechamento_mes = data['fechamento']['mes']
    fechamento_ano = data['fechamento']['ano']
    fechamento_hora = data['fechamento']['hora']
    fechamento_minuto = data['fechamento']['minuto']
    fechamento_timestamp = date.fromtimestamp(data['fechamento']['timestamp'])
    mercado_pos_rodada = data['mercado_pos_rodada']
    aviso = data['aviso']
    aviso_url = data['aviso_url']
    result = [rodada_atual, status_mercado, esquema_default_id, cartoleta_inicial,
              max_ligas_free, max_ligas_pro, max_ligas_matamata_free, 
              max_ligas_matamata_pro, max_ligas_patrocinadas_free, 
              max_ligas_patrocinadas_pro_num, game_over, temporada,
              reativar,exibe_sorteio_pro ,times_escalados ,
              fechamento_dia ,fechamento_mes ,
              fechamento_ano ,fechamento_hora ,
              fechamento_minuto ,fechamento_timestamp ,
              mercado_pos_rodada ,aviso ,aviso_url]

    cur.execute("""INSERT into cartola_fc.tb_mercado_status 
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