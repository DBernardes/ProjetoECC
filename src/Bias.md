# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de bias.

## Bias:
  - Código para caracterização do ruído de leitura;
  - O codigo ira criar um arquivo contendo a lista de nomes das imagens; dessa lista ira retirar uma amostra de 10 imagens e retorna-la para as funcoes gradiente e histograma. A funcao gradiente ira expressar em um grafico em cores a variacao das contagens dos pixels ao longo desta imagem mediana, junto de dois outros graficos da variacao da media das constagens ao longo de suas linhas e colunas; a funcao histograma ira calcular uma distribuicao de frequencia das contagens para um intervalo da media dos pixels +/- 7sigmas. A funcao variacaoTemporal ira receber a lista de imagens completa, retornando um grafico com a mediana das contagens de cada imagem em funcao do tempo do experimento. Sobre esses dados e realizada uma FFT; e gerada uma segunda lista de dados normais em relacao a media e desvio padrao dos dados originais, de modo que a FFT desta serie e plotada junto a primeira, permitindo comparar os picos com intensidade acima de media+3sigmas.


#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram as imagens:
  
         ./ReadNoiseCharact.py

      
Caso haja o interesse em criar um arquivo log contendo todas as informações do experimento, execute o comando:

    ./ReadNoiseCharact.py

#### Resultados:
![relatorio bias](https://user-images.githubusercontent.com/23655702/28124600-86354f1e-66fa-11e7-8024-ada05c0da8a3.png)
  
