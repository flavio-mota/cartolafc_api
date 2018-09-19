#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:43:07 2018

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

cur.execute("""TRUNCATE TABLE cartola_fc.tb_prox_partida CASCADE""")
cur.execute("""TRUNCATE TABLE cartola_fc.tb_aproveitamento CASCADE""")

url = "https://api.cartolafc.globo.com/partidas"
try:
    data = requests.get(url).json()
        
    """Carregando"""
    for partida in data['partidas']:
        
        result_partida = []
        result_mandante = []
        result_visitante = []
        
        id_rodada = data['rodada']
        id_partida = partida['partida_id']
        clube_casa_id = partida['clube_casa_id']
        clube_casa_posicao = partida['clube_casa_posicao']           
        clube_visitante_id = partida['clube_visitante_id']
        clube_visitante_posicao = partida['clube_visitante_posicao']
        partida_data = partida['partida_data']
        local = partida['local']
        valida = partida['valida']
        placar_oficial_mandante = partida['placar_oficial_mandante']
        placar_oficial_visitante = partida['placar_oficial_visitante']
        url_confronto = partida['url_confronto']
        url_transmissao = partida['url_transmissao']
        
        result_partida = [id_rodada,id_partida,clube_casa_id,
                  clube_casa_posicao,clube_visitante_id,
                  clube_visitante_posicao,partida_data,local,
                  valida,placar_oficial_mandante,placar_oficial_visitante,
                  url_confronto,url_transmissao]
        """Carregando dados das partidas"""
        cur.execute("""INSERT into cartola_fc.tb_prox_partida
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
                 %s
               )""",(result_partida))
        conn.commit()
        
        ap0 = partida['aproveitamento_mandante'][0]
        ap1 = partida['aproveitamento_mandante'][1]
        ap2 = partida['aproveitamento_mandante'][2]
        ap3 = partida['aproveitamento_mandante'][3]
        ap4 = partida['aproveitamento_mandante'][4]
        
        result_mandante = [clube_casa_id, id_rodada, ap0, ap1, ap2, ap3, ap4]
        
        """Carregando dados do aproveitamento do clube da casa"""
        cur.execute("""INSERT into cartola_fc.tb_aproveitamento
               VALUES
               ( %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s
               )""",(result_mandante))
        conn.commit()
        
        ap0 = partida['aproveitamento_visitante'][0]
        ap1 = partida['aproveitamento_visitante'][1]
        ap2 = partida['aproveitamento_visitante'][2]
        ap3 = partida['aproveitamento_visitante'][3]
        ap4 = partida['aproveitamento_visitante'][4]
        
        result_visitante = [clube_visitante_id, id_rodada, ap0, ap1, ap2, ap3, ap4]
        
        """Carregando dados do aproveitamento do clube visitante"""
        cur.execute("""INSERT into cartola_fc.tb_aproveitamento
               VALUES
               ( %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s
               )""",(result_visitante))
        conn.commit()
        
        
except IOError as io:
    print("cannot open")
        