CREATE TABLE cartola_fc.tb_scout (
	id_atleta int not null,
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
	foreign key (id_atleta) references cartola_fc.tb_atletas (atleta_id)
);