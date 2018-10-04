CREATE TABLE cartola_fc.tb_mercado_destaques (
	atleta_id int not null,
	id_rodada int not null,
	preco_editorial int,
	escalacoes int,
	clube varchar(5),
	posicao varchar(50)
	primary key (atleta_id, id_rodada),
	foreign key (atleta_id) references cartola_fc.tb_atletas (atleta_id),
	foreign key (id_rodada) references cartola_fc.tb_rodadas (rodada_id)
);