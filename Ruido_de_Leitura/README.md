# Roteiro:
Neste roteiro é apresentado uma breve explicação da caracterização do Ruído de Leitura do CCD e o passo-a-passo para a execução do código

 Este código irá criar um arquivo contendo o relatório dos resultados da caracterização da uma série de 50 imagens de bias. Neste arquivo será apresentado o gradiente, o histograma e a variabilidade temporal do ruído de leitura.
  
  A caracterização do gradiente e do histograma do ruído de leitura fazem uso de uma imagem de bias 'master'. Esta imagem  resulta da combinação pela média de dez imagens de bias retiradas uniformemente ao longo da série. Através da caracterização do gradiente do ruído, é possível ver o comportamento da distribuição de contagens ao longo do CCD e determinar se existe algum fator sistemático interferindo na leitura dos dados. O histograma do ruído apresenta a distribuição de frequências dos valores de contagens para o intervalo da média ± 7 desvios padrão da imagem de bias 'master'. Essa distribuição é comparada à um curva normal distribuída sobre o mesmo intervalo, também permitindo determinar uma influência sobre a distribuição de contagens da imagem.
  
  A caracterização da variabilidade temporal utiliza de uma série de imagens de bias obtidas para um dado intervalo de tempo. É calculada a média de cada imagens ao longo da série, apresentando este resultado em forma gráfica das contagens em função do tempo do experimento. Sobre este resultado, é calculada uma FFT. Uma outra FFT é calculada para uma série aleatória de dados calculada para a média e desvio padrão da série real. Uma comparação entre estas duas transformadas permite determinar se existe algum fator sistemático periódico influenciando na série de imagens.


#### Rodando o código:
 - Baixe e extraia as imagens do arquivo .ZIP presentes neste diretório.
 - Abra o arquivo run.py. Neste arquivo, deve ser fornecido para a variável ```dir_path``` o repositório onde as imagens foram extraída.
 - Após isso, o arquivo pode ser executado e o relatório da caracterização aparecerá no diretório das imagens.
 - Abaixo, segue um exemplo do resultado a ser obtido
  
   
#### Resultados:
![relatorio bias](https://github.com/DBernardes/ProjetoECC/blob/master/Ruido_de_Leitura/Relatorio%20Ruido%20de%20Leitura.png)
  
