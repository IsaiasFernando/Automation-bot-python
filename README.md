# 🤖 Automation Bot Python (Nível Empresa)

Este projeto é um bot de automação completo desenvolvido em **Python**, utilizando **Playwright** para a interação com o navegador e **Pandas** para a manipulação e salvamento de dados. 

O foco deste projeto é demonstrar práticas profissionais de engenharia de software, como organização modular, tratamento de exceções e persistência de dados.

---

## 🚀 Funcionalidades

* **Login Automatizado:** Realiza autenticação segura em sistemas web.
* **Web Scraping:** Extração de dados dinâmicos após o login.
* **Data Processing:** Organização dos dados coletados utilizando a biblioteca Pandas.
* **Exportação Automática:** Gera relatórios em formato `.csv` na pasta `data/`.
* **Logs de Execução:** Feedback em tempo real no terminal sobre o status do processo.

---

## 🛠️ Tecnologias Utilizadas

* [Python 3.x](https://www.python.org/) - Linguagem principal.
* [Playwright](https://playwright.dev/python/) - Automação de navegador moderna e resiliente.
* [Pandas](https://pandas.pydata.org/) - Manipulação e análise de dados.
* [Git/GitHub](https://github.com/) - Controle de versionamento.

---

## 🏗️ Estrutura do Projeto

```text
automation-bot-python/
│
├── data/               # Arquivos gerados pelo bot (CSV/Excel)
├── venv/               # Ambiente virtual (não enviado ao Git)
├── main.py             # Script principal de execução
├── .gitignore          # Filtro de arquivos para o repositório
└── README.md           # Documentação do projeto