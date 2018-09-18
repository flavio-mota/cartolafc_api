CREATE TABLE cartola_fc.tb_mercado_status(
rodada_atual int primary key, 
status_mercado int,
esquema_default_id int,
cartoleta_inicial int,
max_ligas_free int,
max_ligas_pro int,
max_ligas_matamata_free int,
max_ligas_matamata_pro int,
max_ligas_patrocinadas_free int,
max_ligas_patrocinadas_pro_num int,
game_over boolean,
temporada int,
reativar boolean,
exibe_sorteio_pro boolean,
times_escalados bigint,
fechamento_dia int,
fechamento_mes int,
fechamento_ano int,
fechamento_hora int,
fechamento_minuto int,
fechamento_timestamp timestamp,
mercado_pos_rodada boolean,
aviso text,
aviso_url text
);