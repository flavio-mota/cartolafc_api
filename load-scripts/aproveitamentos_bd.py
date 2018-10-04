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
        
    print("Carregando os dados dos aproveitamentos")
    for partida in data['partidas']:
        
        result_partida = []
        result_mandante = []
        result_visitante = []
        
        id_rodada = data['rodada']
        clube_casa_id = partida['clube_casa_id']       
        clube_visitante_id = partida['clube_visitante_id']
        
        ap0 = partida['aproveitamento_mandante'][0]
        ap1 = partida['aproveitamento_mandante'][1]
        ap2 = partida['aproveitamento_mandante'][2]
        ap3 = partida['aproveitamento_mandante'][3]
        ap4 = partida['aproveitamento_mandante'][4]
        
        result_mandante = [clube_casa_id, id_rodada, ap0, ap1, ap2, ap3, ap4]
        
        """Carregando dados do aproveitamento do clube da casa"""
        cur.execute("""INSERT into cartola_fc.tb_aproveitamento
               VALUES
               ( %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s
               )""",(result_mandante))
        conn.commit()
        
        ap0 = partida['aproveitamento_visitante'][0]
        ap1 = partida['aproveitamento_visitante'][1]
        ap2 = partida['aproveitamento_visitante'][2]
        ap3 = partida['aproveitamento_visitante'][3]
        ap4 = partida['aproveitamento_visitante'][4]
        
        result_visitante = [clube_visitante_id, id_rodada, ap0, ap1, ap2, ap3, ap4]
        
        """Carregando dados do aproveitamento do clube visitante"""
        cur.execute("""INSERT into cartola_fc.tb_aproveitamento
               VALUES
               ( %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s,
                 %s
               )""",(result_visitante))
        conn.commit()
    
    cur.close()
    print("Sucesso!")
    print("Carga de dados finalizada!")    
except IOError as io:
    print("Erro")
        