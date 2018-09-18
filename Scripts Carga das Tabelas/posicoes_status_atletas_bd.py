#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:17:30 2018

@author: flaviomota
"""

import urllib
import psycopg2
import json

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Database Connected")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/atletas/mercado"
try:
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_posicoes_atleta CASCADE""")
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_status_atleta CASCADE""")
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_atletas""")
    
    """Carregando as posiçoes dos atletas"""
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
    
    """Carregando os status dos atletas"""
    for status in data['status']:
        result = []
        
        id_posicao = data['status'][status]['id']
        nome = data['status'][status]['nome']

        result = [id_posicao, nome]
        cur.execute("""INSERT into cartola_fc.tb_status_atleta
                       VALUES
                       ( %s,
                         %s
                       )""",(result))
        conn.commit()
    
    """Carregando os atletas"""
    for atleta in data['atletas']:
        result = []
        
        atleta_id = atleta['atleta_id']
        nome = atleta['nome']
        slug = atleta['slug']
        apelido = atleta['apelido']
        foto = atleta['foto']
        rodada_id = atleta['rodada_id']
        clube_id = atleta['clube_id']
        posicao_id = atleta['posicao_id']
        status_id = atleta['status_id']
        pontos_num = atleta['pontos_num']
        preco_num = atleta['preco_num']
        variacao_num = atleta['variacao_num']
        media_num = atleta['media_num']
        jogos_num = atleta['jogos_num']
        scout = atleta['scout']
        
        result = [atleta_id, nome, slug, apelido, foto, rodada_id, clube_id, posicao_id,
                  status_id, pontos_num, preco_num, variacao_num, media_num, jogos_num, scout]
        cur.execute("""INSERT into cartola_fc.tb_atletas
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
except IOError as io:
    print("cannot open")