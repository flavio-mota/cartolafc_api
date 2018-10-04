CREATE TABLE cartola_fc.tb_atletas (
	atleta_id int primary key,
	nome varchar(100),
	slug varchar(50),
	apelido varchar(100),
	foto text,
	clube_id int not null,
	posicao_id int not null,
	foreign key (clube_id) references cartola_fc.tb_clubes(id_clube),
	foreign key (posicao_id) references cartola_fc.tb_posicoes_atleta(id),
);