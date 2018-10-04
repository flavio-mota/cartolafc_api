CREATE TABLE cartola_fc.tb_status_rodada(
	id_rodada int not null,
	id_atleta int not null,
	id_status int not null,
	primary key(id_rodada, id_atleta, id_status),
	foreign key (id_rodada) references cartola_fc.tb_rodadas(rodada_id),
	foreign key (id_atleta) references cartola_fc.tb_atletas(atleta_id),
	foreign key (id_status) references cartola_fc.tb_status_atleta (id)
);