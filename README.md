# Script para mineração de dados sobre acidentes rodoviários no Brasil

Este script foi desenvolvido em Python para mineração de dados sobre acidentes rodoviários no Brasil e para agrupamento de todos os dados em um único arquivo JSON para consulta de dataset.
## Pré-requisitos

- Python 3.x


## Como usar

Faça o clone deste repositório:

```bash
git clone https://github.com/oguhpereira/dataset-road-traffic-accidents-brazil.git
```

- Navegue até o diretório raiz do projeto usando o comando cd dataset-road-traffic-accidents-brazil;
- Use o comando `cd dataset` para navegar até o diretório do dataset;

Dentro da pasta "dataset", você encontrará vários arquivos JSON gerados pelo script. Esses arquivos contêm dados de acidentes rodoviários do Brasil, organizados por estado e ano. Você pode usar esses dados para análise, visualização ou qualquer outro propósito de sua escolha.


Além de baixar os dados extraídos pelo script, você também pode acessar as informações via URL do GitHub Raw. Isso pode ser útil se você quiser integrar os dados a um aplicativo da web ou se quiser acessá-los remotamente.

Para acessar o dataset, basta utilizar a seguinte URL:


```bash
https://raw.githubusercontent.com/oguhpereira/dataset-road-traffic-accidents-brazil/main/dataset/dataset.json
```
Você pode utilizar essa URL para acessar diretamente o arquivo dataset.json em qualquer linguagem de programação que suporte requisições HTTP. Por exemplo, em Python, você pode usar a biblioteca requests para obter os dados:

```python

import requests

response = requests.get('https://raw.githubusercontent.com/oguhpereira/dataset-road-traffic-accidents-brazil/main/dataset/dataset.json')
data = response.json()

print(data)
```

Lembre-se de que, como esses dados estão em formato JSON, você pode usar qualquer biblioteca de análise de dados ou visualização de gráficos que suporte esse formato.

https://github.com/oguhpereira/dashboard-brazil-road-accidents


## Exemplo de aplicação

Para demonstrar como os dados podem ser utilizados, você pode conferir o projeto no repositório do GitHub: [dashboard-brazil-road-accidents](https://github.com/oguhpereira/dashboard-brazil-road-accidents).
