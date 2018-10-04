import requests
import psycopg2


conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Conectado ao banco")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/atletas/mercado"
try:
    data = requests.get(url).json()
    
    print("Carregando os dados dos status dos atletas na rodada - - - - - Aguarde")
    for atleta in data['atletas']:
        result = []
        
        rodada_id = atleta['rodada_id']
        atleta_id = atleta['atleta_id']
        id_status = atleta['status_id']

        result = [rodada_id, atleta_id, id_status]
        cur.execute("""INSERT into cartola_fc.tb_status_rodada
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