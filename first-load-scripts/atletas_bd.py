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
        clube_id = atleta['clube_id']
        posicao_id = atleta['posicao_id']
                
        result = [atleta_id, nome, slug, apelido, foto, clube_id, posicao_id]
        cur.execute("""INSERT into cartola_fc.tb_atletas
                       VALUES
                       ( %s,
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