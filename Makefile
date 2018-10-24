SHELL:=/bin/bash

install: create-virtualenv update

clean:
	rm -R -f venv

create-virtualenv:
	virtualenv venv -p python3

update:
	. venv/bin/activate && pip install -r requirements.txt

create-db:
	@echo -e "\e[32mCriando Tabelas...\e[0m"
	@. venv/bin/activate && python create-tables-scripts/create_bd.py

run-inicial:
	@echo -e "\e[32mCarregando dados iniciais...\e[0m"
	@. venv/bin/activate && python first-load-scripts/clubes_bd.py && python first-load-scripts/status_bd.py && python first-load-scripts/posicoes_bd.py && python first-load-scripts/atletas_bd.py

run:
	@echo -e "\e[32mCarregando dados...\e[0m"
	@. venv/bin/activate && python load-scripts/rodadas_bd.py && python load-scripts/status_rodada_bd.py && python load-scripts/mercado_destaques_bd.py && python load-scripts/aproveitamentos_bd.py && python load-scripts/prox_partidas_bd.py && python load-scripts/scouts_bd.py && python load-scripts/pontuados_bd.py && python load-scripts/partidas_controle_bd.py
