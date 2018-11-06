import psycopg2
import requests

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Conectado ao banco")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/atletas/pontuados"

try:

    d = requests.get(url).json()

    print("Carregando as pontuações dos atletas - - - - - Aguarde")
    for atleta in d['atletas']:
        result = []
        
        rodada_id = d['rodada']
        atleta_id = atleta
        pontuacao = d['atletas'][atleta]['pontuacao']
        result = [atleta_id, rodada_id, pontuacao]

        cur.execute("""INSERT into cartola_fc.tb_pontuacao 
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