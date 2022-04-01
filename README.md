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
4. Infraestrutura:
   1. Servidor Linux na nuvem com a distribuição Debian 11.
   2. Containers em **docker** utilizando **docker-compose**.
   3. Registro de domínio publico utilizando Registro Br (https://registro.br).
   4. Certificado de segurança SSL/HTTPS utilizando Let's Encrypt (https://letsencrypt.org).
   5. Estrutura de microserviços com:
          1.  1 Container com o serviço de Proxy Reverso utilizando Traefik (https://traefik.io)
          2.  1 Container com o serviço de Bando de Dados utilizando XXXXX.
          3.  1 Container com o serviço do Projeto Django utilizando Python, Django e Gunicorn (https://gunicorn.org).
