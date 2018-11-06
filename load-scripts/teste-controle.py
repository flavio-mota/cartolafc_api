import requests
import psycopg2
import datetime

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Conectado ao banco")
cur = conn.cursor()
rowcount = cur.rowcount

cur.execute("""SELECT count(id_carga) FROM cartola_fc.tb_controle""")        
ctr = cur.fetchone()
ctr = ctr[0]
print("Carregando os dados das partidas - - - - - Aguarde")
print(ctr)
url = "https://api.cartolafc.globo.com/partidas"
try:
	data = requests.get(url).json()
	fim = data['rodada']
	cur.execute("""SELECT count(id_carga) FROM cartola_fc.tb_controle""")        
	ctr = cur.fetchone()
	ctr = ctr[0]
	print(ctr,fim)
except IOError as io:
        print("Erro")
