CREATE TABLE aproveitamento (
	id_clube int not null,
	id_rodada int not null,
	id_partida int not null,
	ap0 varchar(2) not null,
	ap1 varchar(2) not null,
	ap2 varchar(2) not null,
	ap3 varchar(2) not null,
	ap4 varchar(2) not null,
	primary key (id_clubes, id_rodada, id_partida),
	foreign key (id_clube) references cartola_fc.tb_clubes (id_clube),
	foreign key (id_rodada) references cartola_fc.tb_rodadas(id_rodada),
	foreign key (id_partida) references cartola_fc.tb_partidas (id_partida)
);