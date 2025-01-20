# Endpoint de Importação
### FIAP - 4MLET - Tech Challenge 1

Banco de dados de importação de derivados de uva.

## Requisição

Para acessar as informações desse serviço, faça uma requisição para o seguinte endpoint:
```
GET /imported
```

As informações estão disponibilizadas e classificadas por ano, podendo estar entre 1970 e 2023.
Para filtrar os dados por ano, adicione à URL um parâmetro chamado `year`. Conforme exemplo abaixo:
```
GET /imported?year=1970
```

As informações estão disponibilizadas e classificadas por sub-categoria.
Para filtrar os dados por sub-categoria, adicione à URL um parâmetro chamado `category`. Conforme o mapa de valores abaixo:
```
GET /imported?category=table_grapes
```
| Categoria do site | Valor do parâmetro |
| ------ | ------ |
| Vinhos de mesa | `?category=table_grapes` |
| Espumantes | `?category=sparkling` |
| Uvas frescas | `?category=fresh_grapes` |
| Uvas passas | `?category=raisins` |
| Suco de uva | `?category=grape_juice` |

## Resposta

A resposta dos dados é classificada de acordo com a categoria e produto.

Exemplo de resposta:
```
{
  "success": true,
  "year": "2023",
  "category": "table_grapes",
  "is_realtime": true,
  "parse_date": "2025-01-20 12:36:12",
  "totals": 137712871,
  "totals_text": "137.712.871",
  "value": 428292652,
  "value_text": "428.292.652",
  "data": [
    {
      "name": "Africa do Sul",
      "quantity": 522733,
      "quantity_text": "522.733",
      "value": 1732850,
      "value_text": "1.732.850"
    },
    {
      "name": "Alemanha",
      "quantity": 102456,
      "quantity_text": "102.456",
      "value": 557947,
      "value_text": "557.947"
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
- `totals`: número inteiro contendo o total de importações para o ano considerado.
- `totals_text`: número total de importações para o ano considerado em texto, conforme informação original no site da Embrapa.
- `value`: número inteiro contendo o valor total de importações em dólar para o ano considerado.
- `value_text`: número do valor total de importações em dólar para o ano considerado em texto, conforme informação original no site da Embrapa.
- `data`: array de objetos de cada país que realizou a importação.
    - `name`: nome do país.
    - `quantity`: número inteiro contendo o total de importações.
    - `quantity_text`: número total de importações.
    - `value`: número inteiro contendo o valor total de importações em dólar.
    - `value_text`: número do valor total de importações em dólar.


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
