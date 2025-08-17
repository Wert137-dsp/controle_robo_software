# Controle Robo Software

[![Status do Projeto](https://img.shields.io/badge/status-em_desenvolvimento-blue.svg)](#)  
[![Linguagens](https://img.shields.io/github/languages/count/Wert137-dsp/controle_robo_software)](#)  
[![Licença](https://img.shields.io/github/license/Wert137-dsp/controle_robo_software)](#)

##  Descrição

**Controle Robo Software** é uma aplicação para gerenciar o controle de um robô, com interface web para controlar e monitorar em tempo real, e backend estruturado segundo o padrão MVC.
Utiliza Python, JavaScript, HTML e CSS para interligar visualização, lógica e dados.

---

##  Índice
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Começando](#começando)
- [Configuração e Uso](#configuração-e-uso)
- [Tecnologias](#tecnologias)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

##  Funcionalidades

- Interface web para controle remoto do robô.
- Estrutura organizada em **Controllers**, **Models** e **Views**.
- Suporte a banco de dados via SQL (`bd_robo.sql`).
- Scripts auxiliares para testes (`teste.py`).
- Fluxo de trabalho com Git: crie *branches*, commit claro e organize suas contribuições.

---

##  Estrutura do Projeto

controle_robo_software/
├── Controllers/
├── Models/
├── Views/
├── controle_robo/
├── bd_robo.sql
└── teste.py

## Começando

git clone https://github.com/Wert137-dsp/controle_robo_software.git
cd controle_robo_software
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt  # se aplicável


## Uso

# Importando o Banco
sqlite3 bd_robo.db < bd_robo.sql


# Execute a aplicação:

python controle_robo/main.py


##Tecnologias

- Python – Lógica backend.

- HTML / CSS / JavaScript – Interface de usuário.

- SQL – Estrutura de banco de dados.

## Contribuição

1. Fork o projeto.
2. Crie uma branch: feature/sua-alteracao.
3. Faça commits claros.
4. Abra um Pull Request explicando suas mudanças.




