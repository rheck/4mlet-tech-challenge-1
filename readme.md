# Dados da Vitivinicultura
### FIAP - 4MLET - Tech Challenge 1

Autor: Ricardo Heck (RM360046) <bheck.ricardo@gmail.com>
FIAP: Pós - Machine Learning Engineering

O presente projeto tem por objetivo fazer um scrapping dos dados da Vitivinicultura do site da Embrapa.
[Site fonte dos dados - Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php)

Todos os dados são solicitados em tempo real ao site da Embrapa. Caso o link não esteja disponível, os dados são solicitados a uma base de dados em PostgreSQL.

Toda requisição respondida com sucesso, atualiza o banco de dados com os dados mais atualizados, dessa forma, qualquer instabilidade no link da Embrapa, os últimos dados retornados são respondidos pela API.

## Como executar

É recomendado o uso de ambiente virtual do Python para evitar conflitos entre as bibliotecas.
Também, o ambiente virtual permite que você instale as bibliotecas de dependências sem privilégios de administrador, de forma local ao projeto.
```
pip install virtualenv
```

Após clonar o projeto na máquina local, entre no diretório e crie o ambiente virtual

```
git clone git@github.com:rheck/4mlet-tech-challenge-1.git
cd 4mlet-tech-challenge-1
python -m venv env
```

Uma vez que o ambiente virtual foi criado no diretório do projeto, é necessário ativar o ambiente virtual, com o seguinte comando:
```
source env/bin/activate
```

Agora que o ambiente virtual está configurado e o projeto clonado, deve-se instalar as bibliotecas de dependências, através do seguinte comando:
```
pip install -r requirements.txt
```

O projeto usa a biblioteca do SQLAlchemy para controle dos modelos e conexão com o banco de dados PostgreSQL.
Com isso, caso um banco de dados vazio seja conectado, ele automaticamente criará as tabelas necessárias para o funcionamento das APIs de dados.

Antes de executar o projeto, copie o arquivo `.env.local` e crie um arquivo `.env`, alterando as informações necessárias, como a URL do banco de dados.
Uma vez que todas as variáveis de ambiente estejam prontas e configuradas, execute o projeto:
```
python app.py
```

## Swagger

O projeto conta com uma rota renderizando o Swagger UI, contendo toda a documentação das rotas do projeto.
Para isso, abra a seguinte URL: [Swagger UI do Projeto](https://rheck-4mlet-tech-challenge-1.vercel.app/swagger-ui)

## Endpoints

Os dados escavados são disponibilizados em diferentes endpoints de API no projeto.
As classificações estão disponíveis conforme tabela abaixo:
| Classificação dos dados | Endpoint de API | Documentação |
| ------ | ------ | ------ |
| Produção | `/production` | [Mais informações](https://github.com/rheck/4mlet-tech-challenge-1/blob/main/docs/production.md) |
| Processamento | `/processing` | [Mais informações](https://github.com/rheck/4mlet-tech-challenge-1/blob/main/docs/processing.md) |
| Comercialização | `/commercialization` | [Mais informações](https://github.com/rheck/4mlet-tech-challenge-1/blob/main/docs/commercialization.md) |
| Importação | `/imported` | [Mais informações](https://github.com/rheck/4mlet-tech-challenge-1/blob/main/docs/imported.md) |
| Exportação | `/exported` | [Mais informações](https://github.com/rheck/4mlet-tech-challenge-1/blob/main/docs/exported.md) |

## Redundância dos dados

Como o projeto lê as informações de um site disponibilizado na internet, problemas de conexão e instabilidades nos servidores são comuns e podem acontecer sem aviso prévio.
Tendo em vista essas possibilidades, o projeto conta com uma camada de persistência em PostgreSQL, o qual recebe os dados toda vez que uma consulta ao site é feita com sucesso. Os dados anteriores são removidos e o conteúdo atualizado é persistido.

Isso significa que quando o site da Embrapa tiver qualquer problema de instabilidade, os dados anteriores são retornados desde essa camada de persistência.

Para que o usuário saiba se o conteúdo que a API está retornando é em tempo real ou da base de dados, foram adicionados duas propriedades na resposta da API.
- `is_realtime`: caso a informação tenha sido escavada em tempo real do site da Embrapa, o retorno será `true`, caso contrário o retorno será `false`
- `parse_date`: contém a data de quando a informação foi escavada, se for em tempo real, a data atual será retornada. Caso seja do banco de dados, a data da última escavação será retornada.

Exemplo de output:
```
{
    ... (demais propriedades)
    is_realtime: true
    parse_date: "2025-01-20 00:45:08"
}
```

## Autenticação

Todas as rotas são protegidas por autenticação via token JWT.
Dessa forma, é necessário chamar a rota de login para gerar o `accessToken` e posteriormente enviá-lo como `Authorization: Bearer {accessToken}` em todas as requisições à API.

| Rota | Descrição |
| ------ | ------ |
| `/authentication/login` | Recebe o `username` e `password` e gera o `accessToken` como resposta. |
| `/authentication/register` | Rota para registrar um novo usuário. [Essa rota necessita de autenticação via JWT também] |

## Licença

Projeto exclusivamente criado para o Tech Challenge 1 da pós graduação FIAP.
