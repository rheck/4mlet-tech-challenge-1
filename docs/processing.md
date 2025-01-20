# Endpoint de Processamento
### FIAP - 4MLET - Tech Challenge 1

Banco de dados de quantidade de uvas processadas no Rio Grande do Sul.

## Requisição

Para acessar as informações desse serviço, faça uma requisição para o seguinte endpoint:
```
GET /processing
```

As informações estão disponibilizadas e classificadas por ano, podendo estar entre 1970 e 2023.
Para filtrar os dados por ano, adicione à URL um parâmetro chamado `year`. Conforme exemplo abaixo:
```
GET /processing?year=1970
```

As informações estão disponibilizadas e classificadas por sub-categoria.
Para filtrar os dados por sub-categoria, adicione à URL um parâmetro chamado `category`. Conforme o mapa de valores abaixo:
```
GET /processing?category=viniferas
```
| Categoria do site | Valor do parâmetro |
| ------ | ------ |
| Viniferas | `?category=viniferas` |
| Americanas e híbridas | `?category=american_and_hybrid` |
| Uvas de mesa | `?category=table_grapes` |
| Sem classificação | `?category=unclassified` |


## Resposta

A resposta dos dados é classificada de acordo com a categoria e produto.

Exemplo de resposta:
```
{
  "success": true,    
  "year": "2023",
  "category": "viniferas",
  "is_realtime": true,
  "parse_date": "2025-01-20 00:45:08",
  "totals": 256370050,
  "totals_text": "256.370.050",
  "data": [
    {
      "items": [
        {
          "name": "Alicante Bouschet",
          "quantity": 4108858,
          "quantity_text": "4.108.858"
        },
        {
          "name": "Ancelota",
          "quantity": 783688,
          "quantity_text": "783.688"
        },
        {
            ...
        }
      ],
      "name": "TINTAS",
      "quantity": 35881118,
      "quantity_text": "35.881.118"
    },
    {
        ...
    }
  ],
}
```

Descrição das variáveis de retorno da API:

- `success`: flag informando se a requisição à API foi feita com sucesso ou não.
- `year`: ano aplicado no filtro para busca das informações. Valor padrão `2023`.
- `category`: informação da categoria das informações.
- `is_realtime`: caso a API consiga obter os dados em tempo real do site da Embrapa, o valor será `true`, caso contrário os dados serão obtidos do banco de dados e o valor será `false`.
- `parse_date`: data em que foi feito a escavação, sendo a data atual para dados em realtime ou a última vez em que foi possível obter os dados do site.
- `totals`: número inteiro contendo o total de processamento para o ano considerado.
- `totals_text`: número total de processamento para o ano considerado em texto, conforme informação original no site da Embrapa.
- `data`: array de objetos de cada categoria de processamento.
    - `name`: nome da categoria de processamento.
    - `quantity`: número inteiro contendo o total da categoria de processamento.
    - `quantity_text`: número total de processamento da categoria.
    - `items`: itens de processamento de cada categoria.
        - `name`: nome do item de processamento.
        - `quantity`: número inteiro contendo o total do item de processamento.
        - `quantity_text`: número total de processamento do item. 


Falhas a chamada da API poderão acontecer nos seguintes casos:

- Caso o site da Empraba esteja fora do ar e não existir a informação no banco de dados.
- Caso a comunicação com o banco de dados esteja falha.

Retorno da API:

```
{
    "success": false,
    "error": "string"
}
```
