CREATE TABLE cartola_fc.tb_atletas (
	atleta_id int primary key,
	nome varchar(100),
	slug varchar(50),
	apelido varchar(100),
	foto text,
	rodada_id int not null,
	clube_id int not null,
	posicao_id int not null,
	status_id int not null,
	foreign key (rodada_id) references cartola_fc.tb_rodadas,
	foreign key (clube_id) references cartola_fc.tb_clubes,
	foreign key (posicao_id) references cartola_fc.tb_posicoes_atleta,
	foreign key (status_id) references cartola_fc.tb_status_atleta
);