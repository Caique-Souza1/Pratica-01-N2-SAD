# Prática 01 - Introdução à Ciência de Dados

## Sistemas de Apoio à Decisão

## Dupla: 

**Caique de Souza Oliveira, Nicolas Pereira Dias**

### Dataset utilizado

**E-Commerce Sales & Profit Analysis Dataset**

---

## 1. Escolha e contexto da base

### 1. Qual dataset foi escolhido?

Foi utilizado o dataset **E-Commerce Sales & Profit Analysis Dataset**, disponibilizado na plataforma Kaggle(Link: https://www.kaggle.com/datasets/nalisha/e-commerce-sales-and-profit-analysis-dataset).

### 2. Qual é o contexto da base de dados?

A base reúne informações sobre vendas realizadas por uma empresa de comércio eletrônico. Cada registro contém dados referentes à data do pedido, produto vendido, categoria do produto, região da venda, quantidade comercializada, valor das vendas e lucro obtido.

### 3. Que tipo de organização poderia usar esses dados?

Empresas de comércio eletrônico (e-commerce), marketplaces, lojas virtuais e organizações do varejo digital podem utilizar esses dados para acompanhar o desempenho das vendas, identificar oportunidades de crescimento e melhorar o processo de tomada de decisão.

### 4. Qual decisão poderia ser apoiada com esses dados?

Os dados podem apoiar decisões como:

* identificar as categorias mais lucrativas;
* verificar quais regiões apresentam melhor desempenho;
* definir estratégias de marketing;
* planejar estoques;
* otimizar campanhas promocionais;
* aumentar a rentabilidade da empresa.

---

## 2. Problema de decisão

### 1. Qual é o problema de decisão que será analisado?

Identificar quais fatores influenciam o desempenho das vendas e do lucro da empresa, permitindo direcionar investimentos para produtos e regiões com maior potencial de retorno.

### 2. Quem seria o usuário interessado nessa análise?

Os principais usuários seriam:

* gestores comerciais;
* gerentes de vendas;
* analistas de negócios;
* diretoria da empresa.

### 3. Qual pergunta inicial de análise pode ser formulada?

**Quais categorias de produtos e regiões geram maior volume de vendas e maior lucro para a empresa?**

### 4. A análise será mais descritiva, diagnóstica, preditiva ou prescritiva? Justifique.

A análise será predominantemente **descritiva**, pois o objetivo é compreender o comportamento atual dos dados por meio de estatísticas, tabelas e gráficos, identificando padrões que auxiliem a tomada de decisão.

---

## 3. Conhecimento inicial da base

### 1. Quantas linhas a base possui?

A base possui **3.500 registros**.

### 2. Quantas colunas a base possui?

A base possui **7 colunas**.

### 3. O que cada linha representa?

Cada linha representa uma venda realizada pela empresa.

### 4. O que cada coluna representa?

| Coluna       | Descrição                   |
| ------------ | --------------------------- |
| Order Date   | Data da venda               |
| Product Name | Nome do produto             |
| Category     | Categoria do produto        |
| Region       | Região onde ocorreu a venda |
| Quantity     | Quantidade vendida          |
| Sales        | Valor total da venda        |
| Profit       | Lucro obtido na venda       |

### 5. Qual é a unidade de investigação da base?

A unidade de investigação é **cada venda registrada**.

### 6. Existe alguma variável identificadora? Qual?

Não. A base não possui um identificador único para cada venda, como um código ou número do pedido.

---

## 4. Classificação das variáveis

| Variável        | Descrição                                   | Classificação         |
| --------------- | ------------------------------------------- | --------------------- |
| Order Date      | Data da venda                               | Temporal              |
| Product Name    | Nome do produto                             | Qualitativa nominal   |
| Category        | Categoria do produto                        | Qualitativa nominal   |
| Region          | Região da venda                             | Qualitativa nominal   |
| Quantity        | Quantidade vendida                          | Quantitativa discreta |
| Sales           | Valor da venda                              | Quantitativa contínua |
| Profit          | Lucro obtido                                | Quantitativa contínua |
| Índice da linha | Identificador do registro durante a análise | Identificador         |

---

## 5. Qualidade dos dados

### 1. Existem valores ausentes?

Não. Nenhuma coluna possui valores ausentes.

### 2. Existem registros duplicados?

Não. Não foram encontrados registros duplicados.

### 3. Existem variáveis com nomes pouco claros?

Os nomes das variáveis são compreensíveis, porém podem ser traduzidos para português para facilitar a interpretação durante a análise.

### 4. Existem categorias inconsistentes?

Não. As categorias encontradas são consistentes e padronizadas.

Categorias:

* Electronics
* Accessories
* Office

Regiões:

* North
* South
* East
* West

### 5. Existem valores impossíveis ou suspeitos?

Não foram identificados valores negativos ou inconsistentes nas variáveis numéricas.

### 6. Existem colunas numéricas que, na verdade, representam códigos?

Não. Todas as variáveis numéricas representam medidas reais.

### 7. Existem datas? Elas estão em formato adequado?

Sim. A coluna **Order Date** contém datas. Inicialmente estava armazenada como texto, sendo convertida para o formato `datetime`, adequado para análises temporais.

### Principais problemas encontrados

| Problema encontrado                        | Variável afetada | Possível tratamento                              |
| ------------------------------------------ | ---------------- | ------------------------------------------------ |
| Data armazenada como texto                 | Order Date       | Converter para datetime                          |
| Colunas em inglês                          | Todas            | Traduzir os nomes para facilitar a interpretação |
| Ausência de identificador único            | Base inteira     | Criar um ID durante a análise, se necessário     |
| Não foram encontrados valores ausentes     | —                | Nenhum tratamento necessário                     |
| Não foram encontrados registros duplicados | —                | Nenhum tratamento necessário                     |

---

## 6. Análise de variáveis qualitativas

### 1. Quais variáveis foram escolhidas?

As variáveis qualitativas escolhidas foram:

* **Category**
* **Region**

### 2. Qual é a frequência absoluta de cada categoria?

#### Category

| Categoria   | Frequência |
| ----------- | ---------: |
| Electronics |       1742 |
| Accessories |       1401 |
| Office      |        357 |

#### Region

| Região | Frequência |
| ------ | ---------: |
| West   |        898 |
| South  |        883 |
| East   |        861 |
| North  |        858 |

### 3. Qual é a frequência relativa de cada categoria?

#### Category

| Categoria   | Frequência Relativa |
| ----------- | ------------------: |
| Electronics |              49,77% |
| Accessories |              40,03% |
| Office      |              10,20% |

#### Region

| Região | Frequência Relativa |
| ------ | ------------------: |
| West   |              25,66% |
| South  |              25,23% |
| East   |              24,60% |
| North  |              24,51% |

### 4. Qual categoria aparece com maior frequência?

Na variável **Category**, a categoria **Electronics** é a mais frequente.

Na variável **Region**, a região **West** apresenta a maior quantidade de vendas, embora a diferença entre as regiões seja pequena.

### 5. Há alguma categoria rara, inconsistente ou inesperada?

Não foram encontradas categorias inconsistentes. Entretanto, a categoria **Office** possui uma quantidade de registros significativamente menor quando comparada às demais.

### 6. Que gráfico foi utilizado para representar a variável?

Foi utilizado um **gráfico de barras (Bar Chart)**, pois facilita a comparação entre as frequências das categorias.

---

## 7. Análise de variáveis quantitativas

### 1. Quais variáveis foram escolhidas?

As variáveis escolhidas foram:

* **Sales**
* **Profit**

### 2. Qual é a média de cada variável?

| Variável |   Média |
| -------- | ------: |
| Sales    | 3047,97 |
| Profit   |  527,05 |

### 3. Qual é a mediana de cada variável?

| Variável | Mediana |
| -------- | ------: |
| Sales    | 2350,50 |
| Profit   |  361,07 |

### 4. Qual é o valor mínimo?

| Variável | Mínimo |
| -------- | -----: |
| Sales    |     51 |
| Profit   |   6,97 |

### 5. Qual é o valor máximo?

| Variável |   Máximo |
| -------- | -------: |
| Sales    |   10.782 |
| Profit   | 2.946,93 |

### 6. Qual é o desvio padrão?

| Variável | Desvio padrão |
| -------- | ------------: |
| Sales    |       2440,21 |
| Profit   |        504,14 |

### 7. Existem valores extremos?

Sim. Os valores máximos estão bastante distantes da média, indicando a presença de possíveis outliers. O uso de um boxplot permite visualizar esses valores extremos.

### 8. A média e a mediana são parecidas? O que isso pode indicar?

Não. Em ambas as variáveis a média é superior à mediana, sugerindo uma distribuição assimétrica à direita. Isso indica que existem algumas vendas com valores muito elevados que aumentam a média.

### 9. Que gráficos foram utilizados?

Foram utilizados:

* Histograma;
* Boxplot.

Esses gráficos permitem observar a distribuição dos dados, a dispersão e a presença de possíveis valores extremos.

---

## 8. Relação entre variáveis

### Relação 1

#### 1. Quais variáveis foram comparadas?

**Category × Profit**

#### 2. Que tipo de gráfico foi usado?

Gráfico de barras com o lucro médio por categoria.

#### 3. O que a relação observada sugere?

A comparação permite identificar quais categorias apresentam maior rentabilidade, auxiliando na definição de estratégias comerciais.

#### 4. Essa relação pode apoiar alguma decisão?

Sim. A empresa pode priorizar investimentos nas categorias mais lucrativas ou desenvolver estratégias para melhorar o desempenho das categorias menos rentáveis.

#### 5. É possível afirmar causalidade? Justifique.

Não. A análise identifica apenas associação entre as variáveis. Outros fatores podem influenciar o lucro, como custos operacionais, fornecedores e promoções.

---

### Relação 2

#### 1. Quais variáveis foram comparadas?

**Region × Sales**

#### 2. Que tipo de gráfico foi usado?

Gráfico de barras.

#### 3. O que a relação observada sugere?

A análise permite comparar o desempenho das vendas entre as diferentes regiões e identificar onde a empresa possui maior participação.

#### 4. Essa relação pode apoiar alguma decisão?

Sim. A empresa pode direcionar campanhas de marketing, estoques e investimentos para regiões com maior potencial de crescimento.

#### 5. É possível afirmar causalidade? Justifique.

Não. A região está relacionada ao desempenho das vendas, mas não é possível afirmar que ela seja a causa direta dos resultados.

---

## 9. Relação com Sistemas de Apoio à Decisão

### 1. Que decisão poderia ser apoiada com os resultados encontrados?

Os resultados podem auxiliar na definição de estratégias comerciais, distribuição de produtos, planejamento de estoque e priorização de investimentos.

### 2. Quem seria o usuário do sistema?

* Diretoria;
* Gerentes comerciais;
* Analistas de negócios;
* Equipe de vendas.

### 3. Que indicadores deveriam aparecer em um painel de apoio à decisão?

* Total de vendas;
* Lucro total;
* Lucro médio;
* Quantidade vendida;
* Vendas por região;
* Lucro por categoria;
* Evolução das vendas ao longo do tempo.

### 4. Que alertas poderiam ser gerados?

* Queda nas vendas de determinada região;
* Redução do lucro de uma categoria;
* Crescimento anormal nas vendas;
* Produtos com baixo desempenho;
* Margem de lucro abaixo do esperado.

### 5. Que cuidados éticos devem ser considerados?

* Garantir a qualidade dos dados;
* Evitar interpretações incorretas;
* Proteger informações confidenciais da empresa;
* Utilizar os resultados apenas como apoio à decisão, e não como única fonte de análise.

### 6. Quais são as limitações da base de dados?

* Não possui identificador único para cada venda;
* Não apresenta informações sobre clientes;
* Não contém dados sobre custos operacionais;
* Possui poucas variáveis para análises mais profundas;
* Não permite explicar todas as causas dos resultados observados.

---

## 10. Conclusão

### 1. Quais foram os principais achados da análise?

A análise mostrou que a base apresenta boa qualidade, sem valores ausentes ou registros duplicados. A categoria **Electronics** concentra a maior quantidade de vendas, enquanto as regiões apresentam distribuição bastante equilibrada. Também foi observado que as variáveis de vendas e lucro possuem distribuição assimétrica, indicando a existência de vendas com valores elevados.

### 2. Que evidências os dados apresentaram?

Os dados evidenciaram diferenças entre categorias de produtos, além de permitirem comparar o desempenho entre regiões. As estatísticas descritivas mostraram grande variabilidade nos valores de vendas e lucro, reforçando a importância do monitoramento desses indicadores.

### 3. Que recomendação poderia ser feita com base nos dados?

Recomenda-se acompanhar continuamente os indicadores de vendas e lucro, investir nas categorias com melhor desempenho e analisar as categorias menos representativas para identificar oportunidades de crescimento. Também é interessante utilizar painéis interativos para facilitar o acompanhamento dos resultados pelos gestores.

### 4. Quais cuidados devem ser tomados antes de usar essa análise para uma decisão real?

Antes da tomada de decisão é importante validar a qualidade dos dados, atualizar a base periodicamente, considerar fatores externos (como sazonalidade e mercado) e complementar a análise com outras informações do negócio, evitando decisões baseadas exclusivamente neste conjunto de dados.
