# 🚗 **Automatização de Preenchimento de Dados de Veículos** 🚗

Estou empolgado para compartilhar um projeto que desenvolvi para automatizar o preenchimento de dados de veículos, como marca, modelo e cor, com base na placa do veículo. A solução foi construída utilizando tecnologias como Django, Celery, RabbitMQ, Playwright e Docker, criando uma arquitetura escalável e eficiente.

---

## 💻 **Tecnologias Utilizadas:**

- **Python** | **Django**: Framework backend para gerenciar a aplicação 🖥️
- **Celery**: Orquestração de tarefas assíncronas e escaláveis ⚡
- **RabbitMQ**: Comunicação eficiente entre os serviços 🔄
- **Playwright**: Web scraping para capturar dados dos veículos 🔍
- **Docker**: Ambiente containerizado para garantir portabilidade e escalabilidade 🐳
- **PostgreSQL**: Banco de dados para armazenar as informações dos veículos 🗄️
- **Django Admin + Jazmin**: Interface administrativa personalizada para gerenciamento dos dados ⚙️

---

## ⚡ **Como Funciona o Sistema?**

- **Django** gerencia o backend da aplicação e interage com o banco de dados PostgreSQL para armazenar as informações dos veículos 🏙️.
- **Celery** processa as tarefas de scraping de forma assíncrona, garantindo eficiência 📈.
- **RabbitMQ** gerencia a troca de mensagens entre os diferentes serviços 🔄.
- **Playwright** realiza o scraping da página web, extraindo dados como marca, modelo e cor do veículo, com base na placa 🚗💻.
- **Docker** facilita a execução e escalabilidade dos serviços em containers independentes, permitindo fácil orquestração e gestão ⚙️.

---

## 🚀 **Destaques do Projeto:**

- **Automação Completa**: Preenchimento automático dos dados dos veículos no banco de dados, sem intervenção manual 🧑‍💻💡
- **Processamento Assíncrono e Escalável**: O uso de **Celery** e **RabbitMQ** garante que múltiplas tarefas sejam executadas simultaneamente e de forma eficiente 📈
- **Ambiente Containerizado**: **Docker** proporciona um ambiente isolado e facilita a escalabilidade e o gerenciamento dos serviços 🐳🔧

---

## 🌱 **Como Rodar o Projeto:**

1. Clone o repositório:  
   `git clone https://github.com/caiomello42/parking_service.git`
2. Navegue até o diretório do projeto:
   `cd projeto`
3. Configure e inicie os containers Docker:
   `docker-compose up --build`
4. Acesse a interface administrativa do Django em `http://localhost:8000/admin`

---
