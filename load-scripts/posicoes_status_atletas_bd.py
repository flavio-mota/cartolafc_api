#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:17:30 2018

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

url = "https://api.cartolafc.globo.com/atletas/mercado"
try:
    data = requests.get(url).json()
    
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_posicoes_atleta CASCADE""")
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_status_atleta CASCADE""")
    cur.execute("""TRUNCATE TABLE cartola_fc.tb_atletas""")
    
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
    
    print("Carregando os dados dos status dos atletas - - - - - Aguarde")
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
    
    print("Carregando as informações dos atletas")
    print("!!!!!Essa operação pode ser demorada!!!!!")
    print("Aguarde")
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
                
        result = [atleta_id, nome, slug, apelido, foto, rodada_id, clube_id, posicao_id,
                  status_id, pontos_num, preco_num, variacao_num, media_num, jogos_num]
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
                         %s
                       )""",(result))
        conn.commit()
        
        
        ca = None 
        fc = None
        ff = None
        fs = None
        ft = None
        g = None
        pe = None
        rb = None
        a = None
        i = None
        cv = None
        sg = None
        gs = None
        dd = None
      
        result_scout = []
      
        if 'CA' in atleta['scout']:
            ca = atleta['scout']['CA']
        if 'FC' in atleta['scout']:
            fc = atleta['scout']['FC']
        if 'FF' in atleta['scout']:
            ff = atleta['scout']['FF']
        if 'FS' in atleta['scout']:
            fs = atleta['scout']['FS']
        if 'FT' in atleta['scout']:
            ft = atleta['scout']['FT']
        if 'G' in atleta['scout']:
            g = atleta['scout']['G']
        if 'PE' in atleta['scout']:
            pe = atleta['scout']['PE']
        if 'RB' in atleta['scout']:
            rb = atleta['scout']['RB']
        if 'A' in atleta['scout']:
            a = atleta['scout']['A']
        if 'I' in atleta['scout']:
            i = atleta['scout']['I']
        if 'CV' in atleta['scout']:
            cv = atleta['scout']['CV']
        if 'SG' in atleta['scout']:
            sg = atleta['scout']['SG']
        if 'GS' in atleta['scout']:
            gs = atleta['scout']['GS']
        if 'DD' in atleta['scout']:
            dd = atleta['scout']['DD']
        
        result_scout = [atleta_id, ca, fc, ff, fs, ft, g, pe, rb, a, i, cv, sg,
                        gs, dd]
        
        cur.execute("""INSERT into cartola_fc.tb_scout
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
                       )""",(result_scout))
        conn.commit()
    
    cur.close()
    print("Sucesso! Inicializando próxima carga....")
except IOError as io:
    print("Erro")