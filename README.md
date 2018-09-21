# Carga de dados utilizando a API do Cartola FC

## Requisitos

Instalar o virtualenv

```bash
sudo apt-get install virtualenv
```
Criar o banco de dados 'cartola_fc', o esquema 'cartola_fc' e dentro do esquema as tabelas presentes nos scripts de criação

## Construir

Rode o seguinte comando para criar o virtualenv e instalar as dependências.

```bash
make install
```

## Executar

Rode o seguinte comando para criar executar a as cargas sequêncialmente.

```bash
make run
```

## Limpar

Rode o seguinte comando se deseja limpar o virtualenv

```bash
make clean
```

