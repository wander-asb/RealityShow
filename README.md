# RealityShow


Você auxiliará uma liderança do time de marketing a
avaliar o impacto causal de um grande investimento que a AcquirerCo está
fazendo para patrocinar um famoso reality show 📺 👀. Seu objetivo é medir se
esse investimento em marketing está atraindo novos clientes, em particular
clientes credenciados através do canal de autocredenciamento (i.e. aqueles
que adquirem a maquininha por conta própria, pelo site da companhia).

Para além do patriocínio per se, a AcquirerCo está realizando campanhas de
marketing específicas durante a exibição do programa, que costuma ser
televisionado diariamente, após às 22h. Um exemplo de campanha é um
anúncio do apresentador, com duração entre 1 e 2 minutos, sobre um desconto
de 20% (válido apenas por algumas horas) para a compra de qualquer
maquininha pelo site, com a exibição de um QR Code na tela direcionando o
telespectador para o site da oferta. 
Para fazer esse trabalho, o time de marketing te deu acesso ao dataset
“Reality_Show”, contendo as seguintes variáveis:

**date** : Dia de referência.
**campaign** : =1 se houve uma campanha de marketing específica durante o
programa e =0 caso contrário.
**new_clients_autocredenciamento** : Quantidade de clientes credenciados pela
AcquirerCo exclusivamente através do canal de autocredenciamento.
**new_clients** : Quantidade total de clientes credenciados pela AcquirerCo.
investment_digital_marketing : Valor de investimento em marketing para mídias
digitais (em R$ mil), incluindo anúncios no Google, Facebook, etc.
**audience** : Audiência do reality show (em %). =NA se date está fora do
período do programa, ou se ele não foi ao ar.

## Objetivo
  - Para endereçar o problema, você decidiu se familiarizar com os dados para
entendê-los melhor. Para isso, crie um plot com a evolução das variáveis 
new_clients_autocredenciamento e investment_digital_marketing ao longo do tempo,
adicionando linhas na vertical para indicar os dias em que houve alguma
campanha de marketing específica durante o programa.
  - Explorando as variáveis do dataset descritivamente, o que você observa de
interessante?
  - Usando somente os dados fornecidos pelo time de marketing, como você
procederia para estimar o impacto causal do investimento feito pela
AcquirerCo em patrocinar o programa (incluindo tanto o patrocínio per se
quanto as campanhas específicas de marketing) na quantidade de clientes
credenciados exclusivamente através do canal de autocredenciamento?
  - Na sua opinião, quais são as principais limitações de uma análise feita com
esses dados?

💡 Dica: observe a evolução das métricas new_clients e 
investment_digital_marketing ao longo do tempo

  - Suponha que o time de marketing disponibilize esse mesmo conjunto de
dados, porém em alta frequência, no nível do minuto. Como essas
informações poderiam auxiliá-lo a estimar o impacto causal de uma
determinada campanha de marketing exibida ao vivo no reality show?
  - Agora, imagine que seja possível obter os dados em “Reality_Show” com
uma granularidade ainda maior, no nível do município-dia. Porém, como
organizar essas informações demandaria um grande esforço do time de
marketing, você precisa explicar porque elas são úteis e como te ajudariam
a estimar o impacto que está tentando medir. O que você diria para eles?
  - Por fim, além de new_clients_autocredenciamento , você usaria alguma outra
variável para analisar a performance do patrocínio
para expandir a sua base de clientes?

## Resultados e Discussões

De acordo com os dados disponibilizados, realizei um tratamento básico de dados para mudar o tipo 
primitivo da variável de data, a fim de criarmos um range quando plotarmos as estruturas de visualização. Logo
após, analisei alguns fatores interessantes da nossa base de dados, composta inicialmente por 5 colunas e 425 
linhas, divididas em dados de tratamento de campanha, histórico de criação de conta por auto credenciamento
(nosso QR Code) e quantidade geral de novos clientes.

A partir da estrutura comentada anteriormente, criei duas colunas, na seguinte ordem, uma nova 
coluna de data, no qual traz a informação de ANO_MES e acquisition_diff, responsável por trazer o número de 
clientes que não entraram em nosso ecossistema por auto credenciamento.

Diante disso, a adesão ao auto credenciamento por campanha é um dado interessante, por exemplo, 
sabe-se que o percentual de audiência capturado e disponibilizado na base de dados pode sofrer impacto por 
não ter ido ao ar, ou então, o programa não foi disponibilizado na data. Para dias que ocorreram campanhas 
que apresentam alguma dessas duas possibilidades, respectivamente dia 31 de janeiro de 2024 e 16 de 
fevereiro de 2024, a conversão de auto credenciamento foi de 40% e 53%, o dado pode ser visualizado na 
tabela abaixo.
