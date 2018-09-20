SHELL:=/bin/bash

install: create-virtualenv update

clean:
	rm -R -f venv

create-virtualenv:
	virtualenv venv -p python3

update:
	. venv/bin/activate && pip install -r requirements.txt

run:
	@echo -e "\e[32mCarregando dados...\e[0m"
	@. venv/bin/activate && python load-scripts/clubes_bd.py && python load-scripts/patrocinadores_bd.py && python load-scripts/mercado_status_bd.py && python load-scripts/mercado_destaques_bd.py && python load-scripts/rodadas_bd.py && python load-scripts/posicoes_status_atletas_bd.py && python load-scripts/partidas_aproveitamento_bd.py && python load-scripts/prox_partidas_aproveitamento.py