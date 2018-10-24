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
        rodada_id = atleta['rodada_id']
       
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
      	
        if atleta['scout']:

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
	        
	        result_scout = [atleta_id, rodada_id, ca, fc, ff, fs, ft, g, pe, rb, a, i, cv, sg,
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
	                         %s,
	                         %s
	                       )""",(result_scout))
	        conn.commit()
    
    cur.close()
    print("Sucesso! Inicializando próxima carga....")
except IOError as io:
    print("Erro")