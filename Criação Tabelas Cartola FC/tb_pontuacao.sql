CREATE TABLE cartola_fc.tb_pontuacao(
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
);