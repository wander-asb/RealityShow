# RealityShow

Você auxiliará uma liderança do time de marketing a
avaliar o impacto causal de um grande investimento que a AcquirerCo está
fazendo para patrocinar um famoso reality show 📺 👀. Seu objetivo é medir se
esse investimento em marketing está atraindo novos clientes, em particular
clientes credenciados através do canal de autocredenciamento (i.e. aqueles
que adquirem a maquininha por conta própria, pelo site da companhia).
Case - Economic Research 4
Para além do patriocínio per se, a AcquirerCo está realizando campanhas de
marketing específicas durante a exibição do programa, que costuma ser
televisionado diariamente, após às 22h. Um exemplo de campanha é um
anúncio do apresentador, com duração entre 1 e 2 minutos, sobre um desconto
de 20% (válido apenas por algumas horas) para a compra de qualquer
maquininha pelo site, com a exibição de um QR Code na tela direcionando o
telespectador para o site da oferta. 
Para fazer esse trabalho, o time de marketing te deu acesso ao dataset
“Reality_Show”, contendo as seguintes variáveis:

date : Dia de referência.
campaign : =1 se houve uma campanha de marketing específica durante o
programa e =0 caso contrário.
new_clients_autocredenciamento : Quantidade de clientes credenciados pela
AcquirerCo exclusivamente através do canal de autocredenciamento.
new_clients : Quantidade total de clientes credenciados pela AcquirerCo.
investment_digital_marketing : Valor de investimento em marketing para mídias
digitais (em R$ mil), incluindo anúncios no Google, Facebook, etc.
audience : Audiência do reality show (em %). =NA se date está fora do
período do programa, ou se ele não foi ao ar.
