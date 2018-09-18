CREATE TABLE cartola_fc.tb_aproveitamento (
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
);