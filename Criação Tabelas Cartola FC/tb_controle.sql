CREATE TABLE cartola_fc.tb_controle(
	id_carga int not null primary key,
	data timestamp not null,
	foreign key (id_carga) references cartola_fc.tb_rodadas(rodada_id)
)