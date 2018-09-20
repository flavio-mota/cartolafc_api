#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:02:39 2018

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

cur.execute("""TRUNCATE TABLE cartola_fc.tb_partidas CASCADE""")

url = "https://api.cartolafc.globo.com/partidas"
try:
    data = requests.get(url).json()
    fim = data['rodada']
except IOError as io:
        print("Erro")        

print("Carregando os dados das partidas - - - - - Aguarde")
for i in range(1, fim):
    url = "https://api.cartolafc.globo.com/partidas/"+str(i)
    try:
        data = requests.get(url).json()
        #print i
    
        
        """Carregando"""
        for partida in data['partidas']:
            
            result_partida = []
            
            id_rodada = i
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
            cur.execute("""INSERT into cartola_fc.tb_partidas
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
            
    except IOError as io:
        print("cannot open")
cur.close()
print("Sucesso! Inicializando próxima carga....")            