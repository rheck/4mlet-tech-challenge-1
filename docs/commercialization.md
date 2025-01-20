# Endpoint de Comercialização
### FIAP - 4MLET - Tech Challenge 1

Banco de dados de comercialização de vinhos e derivados no Rio Grande do Sul.

## Requisição

Para acessar as informações desse serviço, faça uma requisição para o seguinte endpoint:
```
GET /commercialization
```

As informações estão disponibilizadas e classificadas por ano, podendo estar entre 1970 e 2023.
Para filtrar os dados por ano, adicione à URL um parâmetro chamado `year`. Conforme exemplo abaixo:
```
GET /commercialization?year=1970
```

## Resposta

A resposta dos dados é classificada de acordo com a categoria e produto.

Exemplo de resposta:
```
{
  "success": true,
  "year": "2023"
  "category": "commercialization",
  "is_realtime": true,
  "parse_date": "2025-01-20 12:30:32",
  "totals": 472291085,
  "totals_text": "472.291.085",
  "data": [
    {
      "items": [
        {
          "name": "Tinto",
          "quantity": 165097539,
          "quantity_text": "165.097.539"
        },
        {
          "name": "Rosado",
          "quantity": 2520748,
          "quantity_text": "2.520.748"
        },
        {
          "name": "Branco",
          "quantity": 19398561,
          "quantity_text": "19.398.561"
        }
      ],
      "name": "VINHO DE MESA",
      "quantity": 187016848,
      "quantity_text": "187.016.848"
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
- `totals`: número inteiro contendo o total de comercializações para o ano considerado.
- `totals_text`: número total de comercializações para o ano considerado em texto, conforme informação original no site da Embrapa.
- `data`: array de objetos de cada categoria de comercializações.
    - `name`: nome da categoria de comercializações.
    - `quantity`: número inteiro contendo o total da categoria de comercializações.
    - `quantity_text`: número total de comercializações da categoria.
    - `items`: itens de comercializações de cada categoria.
        - `name`: nome do item de comercialização.
        - `quantity`: número inteiro contendo o total do item de comercialização.
        - `quantity_text`: número total de comercialização do item. 


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
