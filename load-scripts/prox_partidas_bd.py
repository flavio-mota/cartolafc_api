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
        
    print("Carregando os dados das próximas partidas e dos aproveitamentos")
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
    
    cur.close()
    print("Sucesso!")
    print("Carga de dados finalizada!")    
except IOError as io:
    print("Erro")
        