    ~/Documentos/apiGeminiNotaFiscal/LucianoJunior    main ⇡1  git push origin                                                                                        ✔ 
To https://github.com/Avaliacao-de-Desempenho/LucianoJunior.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/Avaliacao-de-Desempenho/LucianoJunior.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    ~/Documentos/apiGeminiNotaFiscal/LucianoJunior    main ⇡1  git pull origin main                                                                                 1 ✘ 
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 1.99 KiB | 1016.00 KiB/s, done.
From https://github.com/Avaliacao-de-Desempenho/LucianoJunior
 * branch            main       -> FETCH_HEAD
   91e1c0e..0d99b9b  main       -> origin/main
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
    ~/Documentos/apiGeminiNotaFiscal/LucianoJunior    main ⇣2⇡1    ## SEMANA 1: API de Extração de Dados da Nota Fiscal
### Objetivo: Estruturar o projeto, rodar a API FastAPI e integrar com a API do Gemini
**02/07 - 04/07**
- **Backlog Semanal**
    - Criar repositório e estrutura inicial do projeto
    - Configurar ambiente virtual (`venv`) e `requirements.txt`
    - Criar `Dockerfile` e `docker-compose.yml` com serviços para a API e banco de dados
    - Subir containers com FastAPI e Postgres
    - Criar modelo inicial `GeminiMessage` e testar conexão com o banco
    - Integrar com a API do Gemini
    - Gerar banco de dados por SQLAlchemy
    - Integrar API com o banco de dados
    - Criar serviço `GeminiService` para gerar resposta com os principais campos da nota fiscal e salvar no banco de dados

- **Resultado Esperado**
    - Ambiente com API e banco de dados rodando em containers
    - Integração funcional com a API do Gemini, recebendo um prompt e salvando no banco
    - Evolução: **100% - 100%**

- **Dúvidas do Aluno/Impedimentos Encontrados**
    - Até o momento nenhuma dúvida.

- **Questões para o Aluno**
    - \<QUESTÕES\>

- **Respostas das Questões**
    - \<RESPOSTAS\>

## SEMANA 2: API de Extração de Dados da Nota Fiscal
### Objetivo: \<OBJETIVO DA SEMANA\>
**07/07 - 11/07**
- **Backlog Semanal**
    - Retirada do input do prompt
    - Correção no retorno da rota post

- **Resultado Esperado**
    - Aplicação do retorno padrozinado e retirada do input
    - Evolução: \<100% - 100%\>

- **Dúvidas do Aluno/Impedimentos Encontrados**
    - \<DÚVIDAS\>

- **Questões para o Aluno**
    - \<QUESTÕES\>

- **Respostas das Questões**
    - \<RESPOSTAS\>

## SEMANA 3: \<NOME DO PROJETO\>
### Objetivo: \<OBJETIVO DA SEMANA\>
**14/07 - 17/07**
- **Backlog Semanal**
    - \<QUEBRAR O OBJETIVO DA SEMANA EM PARTES MENORES\>

- **Resultado Esperado**
    - \<QUAL ENTREGÁVEL SERÁ PRODUZIDO QUANDO O OBJETIVO FOR ALCANÇADO (FINAL DA SEMANA)\>
    - Evolução: \<0% - 100%\>

- **Dúvidas do Aluno/Impedimentos Encontrados**
    - \<DÚVIDAS\>

- **Questões para o Aluno**
    - \<QUESTÕES\>

- **Respostas das Questões**
    - \<RESPOSTAS\>
---
## Descrição do Projeto
Criar uma API em Python, usando FastAPI, que receba uma imagem (.jpg, .jpeg, .png) ou um PDF de uma Nota Fiscal; salve o Valor Total, Data de Emissão e CNPJ no banco de dados Postgres e retorne os mesmos campos em formato json.

A API e o banco de dados devem rodar localmente em docker e o projeto como um todo deve poder ser iniciado usando o "docker compose". Também é necessário que os dados persistam mesmo que os dockers sejam pausados ou desligados.

O ambiente local deve estar num ambiente virtual, criado com o "venv", e os pacotes devem estar listados no arquivo "requirements.txt".

## Stack
- Python
- Postgres
- FastAPI
- Docker
    - Dockerfile
    - Docker compose
- Gemini
    - API

## Referências
- Python
    - https://www.python.org/downloads/
    - https://www.python.org/doc/
- Repositório de pacotes python
    - https://pypi.org/
- Ambiente virtual
    - https://docs.python.org/pt-br/3/library/venv.html
- Docker
    - Dockerfile, build de imagem e rodar container: https://docs.docker.com/build/concepts/dockerfile/
    - Docker compose: https://docs.docker.com/compose/
- FastAPI
    - https://fastapi.tiangolo.com/tutorial/
    - https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function
- Banco de dados
    - https://www.postgresql.org/
    - https://pypi.org/project/SQLAlchemy/
    - https://pypi.org/project/psycopg/
- Gemini
    - https://aistudio.google.com/apikey

## Passo a Passo do Projeto
1. Fazer o setup do ambiente
    - criar repositório
    - instalar dependências
    - instalar docker
1. Criar api do projeto com o FastAPI
1. Fazer a extração de campos com Gemini
1. Adicionar integração com banco de dados

## Benchmarks
- Semana 1
    - setup inicial: repositório, pacotes, docker
    - testar fastapi
    - testar gemini
- Semana 2
    - desenvolver api para fazer extração de campos
- Semana 3
    - integrar com banco de dados
    - finalizar documentação
    - apresentação final

## Diretivas
- **Reuniões**  
    **07/07 (segunda)** - report de progresso e impedimentos  
    **10/07 (quinta)** - report de progresso e impedimentos  
    **15/07 (terça)** - report de progresso e impedimentos  
    **17/07 (quinta, apresentação final)** - apresentação do resultado final  
- Documentar código e processos durante todo o projeto  
- Fazer update diário do relatório  
- Fazer update diário do código  
- O repositório deve ter um nome padrão: \<NOME DO ALUNO\>-AVALIAÇÃO

## Avaliação
- Evolução técnica com base nos resultados semanais
- Autonomia no desenvolvimento e impedimentos
- Organização (repositório, report, documentação, git)
