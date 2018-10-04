import psycopg2

conn = psycopg2.connect(host="localhost", database="cartola_fc", 
                        user="postgres", password="postgres")
print("Conectado ao banco!")
cur = conn.cursor()
rowcount = cur.rowcount

cur.execute("""CREATE TABLE cartola_fc.tb_clubes(
id_clube int primary key,
nome varchar(20),
abreviacao varchar(5),
posicao int,
escudo_60x60 text,
escudo_45x45 text,
escudo_30x30 text
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_status_atleta (
	id int primary key,
	nome_status varchar(15)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_posicoes_atleta (
	id int primary key,
	nome varchar(15),
	abreviacao varchar(5)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_rodadas(
rodada_id int primary key,
inicio timestamp,
fim timestamp
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_atletas (
	atleta_id int primary key,
	nome varchar(100),
	slug varchar(50),
	apelido varchar(100),
	foto text,
	clube_id int not null,
	posicao_id int not null,
	foreign key (clube_id) references cartola_fc.tb_clubes(id_clube),
	foreign key (posicao_id) references cartola_fc.tb_posicoes_atleta(id)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_aproveitamento (
	id_clube int not null,
	id_rodada int not null,
	ap0 varchar(2) not null,
	ap1 varchar(2) not null,
	ap2 varchar(2) not null,
	ap3 varchar(2) not null,
	ap4 varchar(2) not null,
	primary key (id_clube, id_rodada),
	foreign key (id_clube) references cartola_fc.tb_clubes (id_clube),
	foreign key (id_rodada) references cartola_fc.tb_rodadas(rodada_id)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_status_rodada(
	id_rodada int not null,
	id_atleta int not null,
	id_status int not null,
	primary key(id_rodada, id_atleta, id_status),
	foreign key (id_rodada) references cartola_fc.tb_rodadas(rodada_id),
	foreign key (id_atleta) references cartola_fc.tb_atletas(atleta_id),
	foreign key (id_status) references cartola_fc.tb_status_atleta (id)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_controle(
	id_carga int not null primary key,
	data timestamp not null,
	foreign key (id_carga) references cartola_fc.tb_rodadas(rodada_id)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_partidas (
	id_rodada int not null,
	id_partida int not null,
	clube_casa_id int not null,
	clube_casa_posicao int not null,
	clube_visitante_id int not null,
	clube_visitante_posicao int not null,
	partida_data timestamp,
	local varchar(50),
	valida boolean,
	placar_oficial_mandante int,
	placar_oficial_visitante int,
	url_confronto text,
	url_transmissao text,
	primary key (id_partida),
	foreign key (clube_casa_id) references cartola_fc.tb_clubes (id_clube),
	foreign key (clube_visitante_id) references cartola_fc.tb_clubes (id_clube)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_pontuacao(
	id_atleta int not null,
	id_rodada int not null,
	pontos_num int,
	preco_num float,
	variacao_num float,
	media_num float,
	jogos_num int,
	primary key (id_atleta, id_rodada),
	foreign key (id_atleta) references cartola_fc.tb_atletas(atleta_id),
	foreign key (id_rodada) references cartola_fc.tb_rodadas(rodada_id)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_mercado_destaques (
	atleta_id int not null,
	id_rodada int not null,
	preco_editorial int,
	escalacoes int,
	clube varchar(5),
	posicao varchar(50),
	primary key (atleta_id, id_rodada),
	foreign key (atleta_id) references cartola_fc.tb_atletas (atleta_id),
	foreign key (id_rodada) references cartola_fc.tb_rodadas (rodada_id)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_prox_partida (
	id_rodada int not null,
	id_partida int not null,
	clube_casa_id int not null,
	clube_casa_posicao int not null,
	clube_visitante_id int not null,
	clube_visitante_posicao int not null,
	partida_data timestamp,
	local varchar(50),
	valida boolean,
	placar_oficial_mandante int,
	placar_oficial_visitante int,
	url_confronto text,
	url_transmissao text,
	primary key (id_partida),
	foreign key (clube_casa_id) references cartola_fc.tb_clubes (id_clube),
	foreign key (clube_visitante_id) references cartola_fc.tb_clubes (id_clube)
);""")

cur.execute("""CREATE TABLE cartola_fc.tb_scout (
	id_atleta int not null,
	id_rodada int not null,
	CA int,
	FC int,
	FF int,
	FS int,
	FT int,
	G int,
	PE int,
	RB int,
	A int,
	I int,
	CV int,
	SG int,
	GS int,
	DD int,
	primary key (id_atleta, id_rodada),
	foreign key (id_atleta) references cartola_fc.tb_atletas (atleta_id),
	foreign key (id_rodada) references cartola_fc.tb_rodadas (rodada_id)
);""")

conn.commit()

print("Tabelas criadas com sucesso!")