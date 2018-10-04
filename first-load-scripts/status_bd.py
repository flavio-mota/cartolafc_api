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
     
    cur.close()
    print("Sucesso! Inicializando próxima carga....")
except IOError as io:
    print("Erro")