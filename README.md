# Projeto Integrador em Computacao II
O objetivo do projeto é desenvolver um software com **Framework Web** que utilize/inclua:
1. Banco de Dados
2. Script Web (JavaScript)
3. Nuvem
4. Uso de API
5. Acessibilidade
6. Controle de Versão
7. Análise de Dados


## O Projeto Escolhido
Software para acompanhamento de Indicadores OKRs/KPIs.

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
1. Framework Web: Django
2. Bibliotecas, django-allauth
3. Bando de Dados: 

4. Infraestrutura de Nuvem:
   1. Servidor físico na núvem utilizando So you Start (https://www.soyoustart.com).
   2. Sistema operacional do Servidor utilizando Linux stribuição Debian 11 (https://www.debian.org).
   3. Containers em **docker** utilizando **docker-compose** (https://www.docker.com).
   4. Registro de domínio publico utilizando Registro Br (https://registro.br).
   5. Certificado de segurança SSL/HTTPS utilizando Let's Encrypt (https://letsencrypt.org).

5. Estrutura de microserviços utilizando um container docker para cada um dos servicos abaixo:
   1. Proxy Reverso utilizando Traefik (https://traefik.io)
   2. Bando de Dados utilizando XXXXX.
   3. Aplicação Django utilizando Python (https://www.python.org), Django (https://www.djangoproject.com) e Gunicorn (https://gunicorn.org).
 
