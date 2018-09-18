CREATE TABLE cartola_fc.tb_patrocinadores (
liga_editorial_id int,
liga_id int,
tipo_ranking varchar(10),
url_link varchar(100),
img_background varchar(200),
img_marca_patrocinador varchar(200),
img_marca_patrocinador_png varchar(200),
nome text,
optin boolean,
destaque boolean,
nome_patrocinador text,
descricao text,
url_flamula_svg	text,
url_flamula_png	text,
total_times	int,
primary key(liga_id, liga_editorial_id)
);