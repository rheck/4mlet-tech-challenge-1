# Endpoint de Produção
### FIAP - 4MLET - Tech Challenge 1

Banco de dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.

## Requisição

Para acessar as informações desse serviço, faça uma requisição para o seguinte endpoint:
```
GET /production
```

As informações estão disponibilizadas e classificadas por ano, podendo estar entre 1970 e 2023.
Para filtrar os dados por ano, adicione à URL um parâmetro chamado `year`. Conforme exemplo abaixo:
```
GET /production?year=1970
```

## Resposta

A resposta dos dados é classificada de acordo com a categoria e produto.

Exemplo de resposta:
```
{
  "success": true,    
  "year": "1970",
  "category": "production",
  "is_realtime": true,
  "parse_date": "2025-01-20 00:45:08",
  "totals": 256370050,
  "totals_text": "256.370.050",
  "data": [
    {
      "items": [
        {
          "name": "Tinto",
          "quantity": 174224052,
          "quantity_text": "174.224.052"
        },
        {
          "name": "Branco",
          "quantity": 748400,
          "quantity_text": "748.400"
        },
        {
          "name": "Rosado",
          "quantity": 42236152,
          "quantity_text": "42.236.152"
        }
      ],
      "name": "VINHO DE MESA",
      "quantity": 217208604,
      "quantity_text": "217.208.604"
    },
    {
      ...
    }
  ]
}
```

Descrição das variáveis de retorno da API:

- `success`: flag informando se a requisição à API foi feita com sucesso ou não.
- `year`: ano aplicado no filtro para busca das informações. Valor padrão `2023`.
- `category`: informação da categoria das informações.
- `is_realtime`: caso a API consiga obter os dados em tempo real do site da Embrapa, o valor será `true`, caso contrário os dados serão obtidos do banco de dados e o valor será `false`.
- `parse_date`: data em que foi feito a escavação, sendo a data atual para dados em realtime ou a última vez em que foi possível obter os dados do site.
- `totals`: número inteiro contendo o total de produção para o ano considerado.
- `totals_text`: número total de produção para o ano considerado em texto, conforme informação original no site da Embrapa.
- `data`: array de objetos de cada categoria de produção.
    - `name`: nome da categoria de produção.
    - `quantity`: número inteiro contendo o total da categoria de produção.
    - `quantity_text`: número total de produção da categoria.
    - `items`: itens de produção de cada categoria.
        - `name`: nome do item de produção.
        - `quantity`: número inteiro contendo o total do item de produção.
        - `quantity_text`: número total de produção do item. 


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
