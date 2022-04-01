# Projeto Integrador em Computacao II
O objetivo do projeto é desenvolver um software com **Framework Web** que utilize/inclua:
1. Banco de Dados
2. Script Web (JavaScript)
3. Nuvem
4. Uso de API
5. Acessibilidade
6. Controle de Versão
7. Análise de Dados


## O Projeto escolhido
Software para acompanhamento de Indicadores OKRs/KPIs.

### Dor:
Como medir a evolução de um planejamento de curto, médio e longo prazo? Como saber se a execução realmente está sendo efetiva e se vai cumprir o prazo?
### Solução:
Criar um software que permita cadastrar indicadores e a partir deles gerar um Dashboard para a apresentação de indicadores diversos de maneira clara e que suporte a tomada de decisão.

### Funcionalidades:
Criar conta (tennant)
Área Administrativa (acessada pelo criador da conta tennat ou admins) para:
Cadastrar usuários adicionais, selecionar o nível (admin/gerente/user)
Cadastrar indicador
selecionar se é OKR ou KPI,
cadastrar suas metas
cadastrar a frequência de leitura, se é diária, semanal ou mensal.
Área para:
Imput dos indicadores.
Dashboard para Visualização dos Indicadores.
API-REST para:
POST com o ID do indicador - Permite o input do valor do indicador. (isso pode ser útil para cadastrar valores de indicadores automaticamente. Indicadores que recebam dados de outras aplicações.)
GET com o ID do indicador - Permite a leitura do valor do indicador em JSON.
Tecnologias para Implementar:
Nodejs (ainda não sei nada a respeito, gostaria de aprender).
MongoDB (sei muito pouco, tb. gostaria de aprender).
Serviços em Docker (conheço razoavelmente bem).
