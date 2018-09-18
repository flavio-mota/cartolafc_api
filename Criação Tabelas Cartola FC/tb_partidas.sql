CREATE TABLE cartola_fc.tb_partidas (
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
);