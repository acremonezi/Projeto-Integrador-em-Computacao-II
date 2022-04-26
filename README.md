# Projeto Integrador em Computacao II
O objetivo do projeto é desenvolver um software com **Framework Web** que utilize/inclua:

1. Banco de Dados.
2. Script Web (JavaScript).
3. Nuvem.
4. Uso de API.
5. Acessibilidade.
6. Controle de Versão.
7. Testes.
8. Análise de Dados.

**Ementa:**  Resolução de problemas. Levantamento de requisitos. Desenvolvimento web com framework. HTML. CSS. Linguagem de script (Javascript). Banco de Dados. Controle de Versão. Nuvem. API. Acessibilidade. Testes. Análise de dados.<br>

Data: 1o Semestre, 2022.
<br>

## O Projeto Escolhido
Software para acompanhamento de Indicadores OKRs (Objectives and Key Results) e/ou KPIs (Key Performance Indicator).

### Dor:
Como medir a evolução de um planejamento de curto, médio e longo prazo? Como saber se a execução realmente está sendo efetiva e se vai cumprir o prazo?

### Solução:
Criar um software que permita cadastrar indicadores e a partir deles gerar um Dashboard para a apresentação de indicadores diversos de maneira clara e que suporte a tomada de decisão.

### Funcionalidades:
1. Criar conta (tennant)
2. Área Administrativa (acessada pelo criador da conta tennat ou admins) para:
   1. Cadastrar usuários adicionais, selecionar o nível (admin/gerente/user)
   2. Cadastrar indicador, selecionar se é OKR ou KPI,
   3. Cadastrar suas metas cadastrar a frequência de leitura, se é diária, semanal ou mensal.

3. Área de Usuário para:
   1. Imput dos indicadores.
   2. Dashboard para Visualização dos Indicadores.

4. API-REST para:
   1. POST com o ID do indicador - Permite o input do valor do indicador. (isso pode ser útil para cadastrar valores de indicadores automaticamente. Indicadores que recebam dados de outras aplicações.)
   2. GET com o ID do indicador - Permite a leitura do valor do indicador em JSON.
   
### Tecnologias Escolhidas para Implementar:
1. Código:
   1. Linguagem de Programação: **Python** (https://www.python.org).
   2. Framework Web: **Django** (https://www.djangoproject.com).
   3. Bibliotecas: **django-allauth** (https://www.intenct.nl/projects/django-allauth).
   4. Bando de Dados: ????
   5. Controle de Versões: **Github** (https://github.com).

6. Infraestrutura de Nuvem:
   1. Servidor físico na nuvem utilizando So you Start (https://www.soyoustart.com).
   2. Sistema operacional do Servidor utilizando Linux distribuição Debian 11 (https://www.debian.org).
   3. Containers em **docker** utilizando **docker-compose** (https://www.docker.com).
   4. Registro de domínio publico utilizando Registro Br (https://registro.br).
   5. Gerenciamento de DNS público e Registro de hostnames (https://www.cloudflare.com).
   6. Certificado de segurança SSL/HTTPS utilizando Let's Encrypt (https://letsencrypt.org).
   7. Serviço de envio de e-Mails Sendgrid (https://sendgrid.com).

7. Arquitetura:

Estrutura de microserviços com (**arquitetura em n-níveis**) utilizando um container docker para cada um dos servicos abaixo:
   1. **Proxy Reverso** utilizando Traefik (https://traefik.io)
   2. **Banco de Dados** utilizando XXXXX.
   3. **Aplicação Django** utilizando Gunicorn (https://gunicorn.org).

<br>
<br>

## Links:
1. Gerenciamento do Projeto: https://github.com/acremonezi/Projeto-Integrador-em-Computacao-II/projects/1
2. Documentação: https://github.com/acremonezi/Projeto-Integrador-em-Computacao-II/wiki
3. Protótipo:
4. Data Models: https://github.com/acremonezi/Projeto-Integrador-em-Computacao-II/tree/main/docs/data_models
5. Arquitetura: https://github.com/acremonezi/Projeto-Integrador-em-Computacao-II/tree/main/docs/architecture
6. Repositório Git: https://github.com/acremonezi/Projeto-Integrador-em-Computacao-II/
7. Versões do Software: https://github.com/acremonezi/Projeto-Integrador-em-Computacao-II/releases
8. Software: https://bee.espertamente.com.br/
9. Vídeo:
