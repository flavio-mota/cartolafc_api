import requests
import psycopg2

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
user="postgres", password="postgres")
print("Conectado ao banco")
cur = conn.cursor()
rowcount = cur.rowcount

url = "https://api.cartolafc.globo.com/partidas"
try:
    data = requests.get(url).json()
    rodada = data['rodada']
except IOError as io:
        print("Erro")        


url = "https://api.cartolafc.globo.com/mercado/destaques"
try:

    data = requests.get(url).json()

    print("Carregando os destaques do mercado - - - - - Aguarde")
    for item in data:
        result = []
        
        rodada_id = rodada-1
        atleta_id = item['Atleta']['atleta_id']
        preco_editorial = item['Atleta']['preco_editorial']
        escalacoes = item['escalacoes']
        clube = item['clube']
        posicao = item['posicao']
        result = [atleta_id, rodada_id, preco_editorial, escalacoes, clube, posicao]

        cur.execute("""INSERT into cartola_fc.tb_mercado_destaques 
                       VALUES
                       ( %s,
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