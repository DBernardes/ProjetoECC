# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de bias.

## Bias:
  - Código para caracterização do ruído de leitura;
  
  - Este código irá criar um arquivo contendo os resultados da caracterização da série de imagens de bias. Neste arquivo será apresentado o gradiente, o histograma e a variabilidade temporal do ruído de leitura.
  
  A caracterização do gradiente e do histograma do ruído de leitura fazem uso de uma imagem de bias 'master'. Esta imagem  resulta da combinação pela média de dez imagens de bias retiradas uniformemente ao longo da série. Através da caracterização do gradiente do ruído, é possível ver o comportamento da distribuição de contagens ao longo do CCD e determinar se existe algum fator sistemático interferindo na leitura dos dados. O histograma do ruído apresenta a distribuição de frequências dos valores de contagens para o intervalo da média ± 7 desvios padrão da imagem de bias 'master'. Essa distribuição é comparada à um curva normal distribuída sobre o mesmo intervalo, também permitindo determinar uma influência sobre a distribuição de contagens da imagem.
  
  A caracterização da variabilidade temporal utiliza de uma série de imagens de bias obtidas para um longo intervalo de tempo (o utilizado em nossos ensaios foram 2 horas). É calculada a média de cada imagens ao longo da série, apresentando este resultado em forma gráfica das contagens em função do tempo do experimento. Sobre este resultado, é calculada uma FFT. Uma outra FFT é calculada para uma série aleatória de dados calculada para a média e desvio padrão da série real. Uma comparação entre estas duas transformadas permite determinar se existe algum fator sistemático periódico influenciando na série de imagens.


#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram as imagens:
  
         ./ReadNoiseCharact.py

      
Caso haja o interesse em criar um arquivo log contendo todas as informações do experimento, execute o comando:

    ./ReadNoiseCharact.py

#### Resultados:
![relatorio bias](https://user-images.githubusercontent.com/23655702/28124600-86354f1e-66fa-11e7-8024-ada05c0da8a3.png)
  
