
<p align="center"><img src="https://imgur.com/6foNNzk.png"></p>

<p align="center">
<a><img src="https://travis-ci.org/fga-eps-mds/2019.1-MaisMonitoria-ApiMonitorias.svg?branch=develop"></a>
<a><img src="https://codecov.io/gh/fga-eps-mds/2019.1-MaisMonitoria-ApiMonitorias/branch/develop/graph/badge.svg"></a>
<a><img src="https://img.shields.io/badge/license-GLP--3.0-red.svg"></a>
<a><img src="https://api.codeclimate.com/v1/badges/0b0956674000b10eb598/maintainability"></a>
</p>

<h1 align="center"> +Monitoria </h1>
<p align="justify"> O projeto +monitoria nasceu com a necessidade dos alunos da FGA de encontrar monitorias sem que sigam os modelos de monitorias atuais, devido as restrições de horário, disposição e limitações dos monitores.O projeto tem como objetivo suprir essa necessidade dos alunos, disponibilizando um catálogo de monitorias , estendendo o número de monitores para que os alunos da FGA possam ter mais opções, buscando aumentar a iteração entre os estudantes e incentivando a troca de conhecimento.</p>
<p align="center">
  <a href="https://fga-eps-mds.github.io/2019.1-MaisMonitoria/">Acesse o site de apresentação do +Monitoria</a>
</p>

## Contexto
Nesse repositório está localizado o código do API Monitorias do projeto. Responsável por gerenciar tudo que diz respeito a perfil do usuário, consequentemente sendo responsável por cuidar de toda lógica que envolve as monitorias.

## Requisitos
Requisitos para conseguir rodar o projeto.
 - Docker
 - Docker-compose
## Desenvolvimento
1. Dê um fork do projeto
2. No [repositório de docs](https://github.com/fga-eps-mds/2019.1-MaisMonitoria) crie uma issue de acordo com  [plano de gestão e configuração](https://fga-eps-mds.github.io/2019.1-MaisMonitoria/docs/plano-gcs) 
3. Para iniciar o desenvolvimento clone o repositório.
4. Faça a build do projeto 
> sudo make build
5. Dê o run no projeto
> sudo make run
6. Acesse http://localhost:8001

### Comandos Makefile

1. Para rodar em background
> sudo make run-d
2. Para rodar os testes
> sudo make tests
3. Para entrar no container
> sudo make enter
4. Para derrubar o container
> sudo make down
5. Para parar o container
> sudo make stop
6. Para iniciar o container
> sudo make start

## Outros repositorios
* [+Monitoria API DOCS](https://github.com/fga-eps-mds/2019.1-MaisMonitoria)
* [+Monitoria API Gateway](https://github.com/fga-eps-mds/2019.1-MaisMonitoria-api)
* [+Monitoria Front-End](https://github.com/fga-eps-mds/2019.1-MaisMonitoria-FrontEnd)
