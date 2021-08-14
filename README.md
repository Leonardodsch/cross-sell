# Cross Selling

Disclaimer: O Contexto a seguir, é completamente fictício, a empresa, o contexto, as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam em um projeto do site https://sejaumdatascientist.com/.

<p align="center">
  <img width="700" height="350" src="https://user-images.githubusercontent.com/76128123/129287844-877c2e29-dcd0-4995-b9e6-00649ade9028.png"/>
</p>



## Contexto de negócio

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis.

Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.

## O Desafio

Nesse contexto, você foi contratado como um consultor de Ciência de Dados para construir um modelo que prediz se o cliente estaria ou não interessado no seguro de automóvel. 

Com a sua solução, o time de vendas espera conseguir priorizar as pessoas com maior interesse no novo produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a compra.

Como resultado da sua consultoria, você precisará entregar um relatório contendo algumas análises e respostas às seguintes perguntas:

1. Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.
2. Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel, o time de vendas conseguirá contatar fazendo 20.000 ligações?
3. E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?
4. Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?

## Dados

O conjunto de dados está disponível na plataforma do Kaggle, através desse link: https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction 

Cada linha representa um cliente e cada coluna contém alguns atributos que descrevem esse cliente, além da sua resposta à pesquisa, na qual ela mencionou interesse ou não ao novo produto de seguros. 

O conjunto de dados inclui as seguintes informações:

 - **Id**: identificador único do cliente.
 - **Gender**: gênero do cliente.
 - **Age**: idade do cliente.
 - **Driving License**: 0, o cliente não tem permissão para dirigir e 1, o cliente tem para dirigir ( CNH – Carteira Nacional de Habilitação )
 - **Region Code**: código da região do cliente.
 - **Previously Insured**: 0, o cliente não tem seguro de automóvel e 1, o cliente já tem seguro de automóvel.
 - **Vehicle Age**: idade do veículo.
 - **Vehicle Damage**: 0, cliente nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado.
 - **Anual Premium**: quantidade que o cliente pagou à empresa pelo seguro de saúde anual.
 - **Policy sales channel**: código anônimo para o canal de contato com o cliente.
 - **Vintage**: número de dias que o cliente se associou à empresa através da compra do seguro de saúde.
 - **Response**: 0, o cliente não tem interesse e 1, o cliente tem interesse.

## Planejamento da solução

**1. Entendimento do negócio e problemas e serem resolvidos** - Buscar entender os reais motivos da necessidade da previsão de vendas e como o probelma pode ser resolvido através de machine learning, quais aspectos serão considerados na hora da predição e quão melhor a solução proposta pode ser considerando os modelos de predição utilizados atualmente na empresa.    

**2. Coleta de dados** - Acesso a plataforma do Kaggle para download dos arquivos que serão usados.

**3. Limpeza dos dados** - Os dados são analisados usando diferentes técnicas para verificar a existência de dados faltantes, outliers (valor discrepantes) , ou qualquer tipo de inconsistências para que assim possam ser tratados devidamente e não impactar nas análises futuras. 

**4. Exploração dos dados** - Busca um melhor entendimento do negócio através da geração de insights e das variáveis mais importantes na modelagem do modelo de Machine Learning. Diversas hipóteses foram levantadas e validadas para obtenção de um conhecimento de negócio mais profundo, verificando também a correlação entre os atributos para que se possa ter uma ideia da importância de cada um para o modelo de machine learning. 

**5. Preparação dos dados** - Os dados foram transformados, balanceados e regularizados para que atendam as premissas de funcionamento dos algoritmos de machine learning, nesta etapa é importante deixar os dados preparados para que os algoritmos possam ter o melhor desempenho possível, e possíveis inconsistencias no dataset não interfiram no resultado final.

**6. Seleção de features** - Após a preparação dos dados nesta seção algoritmos, como o Boruta e o feature importance, selecionarão as melhores colunas a serem utilizadas para o treinamento do modelo de machine learning. Elas serão analisadas e selecionadas de acordo com descobertas feitas na análise exploratória e levando em conta o contexto de nagócio.

**7. Aplicação dos algoritmos de machine learning** - Nesta etapa foram escolhidos os algoritmos de machine learning que seriam usados e então os mesmos foram treinados com os dados já preparados e prontos, cada algoritmo foi testado usando seus devidos parâmetros e posteriormente estratégias de cross validation foram usadas para verificar o real resultado do medelo, bem como tecnicas de hyperparameter fine tunning para encontrar os melhores parâmetros para o modelo escolhido. 

**8. Avaliação do algoritmo** - O algoritmo é avaliado com base em algumas métricas e nesse ponto verifica-se ou não a necessidade de realizar mais um ciclo para melhorar o desempenho final.

**9. Tradução do erro em métricas de negócio** - Com o melhor modelo escolhido, treinado e otimizado a taxa de erro encontrada é trasnformada em mátricas de negócio para que se saiba concretamente quanto de retorno financeiro aquela solução trouxe para a empresa. 

**10. Deploy do modelo em produção** - O modelo foi colocado em produção no ambiente cloud Heroku para que as predições possam ser acessados através de requisições a uma API e consulta em uma planilha no google sheets.

O projeto utiliza a metodologia CRISP-DM, que consiste desenvolver o projeto de forma ciclica entendendo todos os passos do projeto e buscando entregar valor ao negócio o mais rápido possível e aperfeiçoar a solução a cada ciclo.

<p align="center">
  <img width="500" height="400" src="https://user-images.githubusercontent.com/76128123/129281894-1a9389f5-e953-4c7d-ad6a-cadbc62e9abc.png"/>
</p>


## Melhores Insights

- **Clientes que estão com o seguro de saúde a mais de 100 dias tem mais interesse por um seguro de carro**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129283345-a09438a1-11cd-4579-a5db-0f8e237e6d4b.png"/>
</p>


- **Clientes com veículos com idade entre 1 e 2 anos tem mais interesse por seguro de carro**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129284007-062bfaec-be2e-4160-8f39-2fc2e3bd043d.png"/>
</p>


- **Homens se interessam 57% a mais do que mulheres em um seguro de carro**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129284047-a21562bf-1a06-4dac-8b46-6ace0afbd470.png"/>
</p>

## Machine Learning Models

Os algoritmos utilizados para fazer a predição foram:

- Modelo Dummy Clisifier para que fosse possível ter um modelo base de comparação,
- Logistic Regression;
- KNN;
- LightGBM;
- ExtraTrees;
- Random Forest Classifier;
- XGBoost Classifier.

Após a realização dos testes com todos os algoritmos e verificação das métricas de performnace, verificou-se um melhor desempenho nos algoritmos baseados em árvores, então a decisão foi usar o algoritmo LightGBM pois é um algoritmo mais leve e rápido e que se mostrou muito eficiente com uma performance muito satisfatória.

As métricas utilizadas foram a Precision@K e Recall@K que são as mais adequadas para probelmas de rankeamento, elas são capazes de verificar a qualidade do modelo em ordenar as predições em determinado número de amostras(K).

O gráfico da curva de ganhos cumulativos mostra a quantitade de pessoas interessadas que o modelo consegue identificar em determinada amostra de clientes.

Já a curva Lift mostra o quão melhor o modelo de machine learning é em comparação com um modelo aleatório em determinada amostra de clientes. 

- Curva de ganhos cumulativos

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129285702-50363d43-cce3-428f-9f73-b398345dc93d.png"/>
</p>


- Curva Lift

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129285753-4c6e6158-a566-43c0-9829-3b56eb355852.png"/>
</p>


## Resultados

### Perguntas de negócio

**1. Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar fazendo 20.000 ligações?**

Utilizando uma amostra com aproximadamente 76.000 clientes, e fazendo as 20.000 ligações (o que representa aproximadamente 26% da base) é possível identificar 71% dos clientes interessados em adquirir o seguro de automóvel, como é possivel observar no grafico de ganhos cumulativos abaixo.  
A curva de Lift mostra um comparativo de quão melhor o modelo de machine learning é em relação a um modelo Baseline com previsões aleatórias. Nota-se que nos mesmos 26% da base de clientes o modelo é aproximadamente 2,7 vezes melhor do que um modelo baseline que identificaria apenas 26% dos clientes.

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129287017-e106acc6-ff35-43ec-b8f6-d3f0dadf6010.png"/>
</p>

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129287061-a9028546-d265-4657-acd6-b1b40ae84463.png"/>
</p>



**2. E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?**

Com uma capacidade de fazer 40.000 ligações (o que representa aproximadamente 53% da base) seria possível contatar mais de 99% dos clientes interessados. O Gráfico da curva Lift mostra que nesse percentual da base o modelo de machine learning seria quase 2 vezes mais eficiente do que um modelo aleatório, que teria identificado apenas metade dos clientes interessados no seguro.   

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129287166-2a12efbc-6793-4634-81ed-c4fa1bd51a80.png"/>
</p>

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129287200-29474eed-8a68-4851-b02b-82fc60edd180.png"/>
</p>



**3. Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?**

Para contatar 80% dos clientes interessados seriam necessárias aproximadamente 24.000 ligações (o que representa 31% da base total analisada). Utilizando um modelo baseline, com as mesmas 24.000 ligações, seria possível contatar apenas 31% dos clientes interessados.

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129287411-75ee8ce3-d8eb-4907-9213-020abce8d067.png"/>
</p>


## Conclusão

Após todo o estudo, análise e testes com diferentes modelos de machine learning foi possível responder as perguntas de negócio e gerar insights para que o time de vendas consiga realizar o contato com os clientes de uma forma muito mais otmizada e acertiva, reduzindo ou eliminando o tempo gasto com clientes que não possuem interesse no seguro e consequentemente reduzindo custos da empresa. Usando um modelo de rankeamento é possível maximizar a eficiêcia da detecção de clientes possivelmente interessados, sendo possível, a partir dos testes feitos e avaliação de métricas, encontrar 100% dos clientes interessados em cerca de metade da base total de clientes, um resultados bastente considerável ainda mais considerando que o número de contatos que o time de vendas consegue fazer é limitado.

Utilizar técnicas de ciencia de dados e inteligência artificial para otimizar a tomada de decisões e fazer com que a empresa cresça cada vez mais, se torna algo essencial tendo em vista o crescimento da competitividade nos mais diversos setores. Soluções baseadas em dados se motram uma ferramenta muito poderosa e que pode se tornar uma vantagem competitiva se usadas de forma estratégica e inteligente, fazendo com que empresas que não percebem o valor disso consequentemente se tornem obsoletas. 

