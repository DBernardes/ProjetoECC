# Roteiro:
Neste roteiro é apresentado uma breve explicação sobre a caracterização do ganho dos CCDs e um passo-a-passo para a execução do código.

O objetivo deste experimento é a caracterização do ganho do CCD para uma determinada taxa de leitura e pré-amplificação. Para tanto, devem ser adquiridas dez imagens de bias consecutivas. Em seguida, devem ser adquiridas 10 sequências de imagens de Flat Field. Cada sequência deve conter um total de 5 imagens. A iluminação sobre o CCD para cada serie deve ser aumentada gradualmente, ao longo do intervalo de 20% a 60% do intervalo dinâmico do dispositivo. Com estes resultados, o código plota um gráfico da intensidade do sinal em função da variância, realizando-se um ajuste linear sobre os dados. Através do coeficiente linear da curva, é obtido qual o valor do ganho. Além disso, é plotado um segundo gráfico da subtração do valor da intensidade do sinal calculada pelo valor do ajuste linear. O resultado esperado neste procedimento é uma curva em função da variância ao redor de zero. 

 

#### Rodando o código:
 - Baixar e extrair as imagens presentes no arquivo .ZIP apresentado neste diretório.
 - Abrir o arquivo run.py. Este arquivo executa o código da caracterização desenvolvido. Para tanto, devem ser fornecidos o caminho do diretório onde as imagens foram extraídas, o número de imagens de Flat Field obtidas, uma keyword para o nome das imagens de Flat e uma keyword para o nome das imagens de Bias.
 - Após isso, o arquivo pode ser executado e o relatório da caracterização aparecerá no diretório das imagens.
 - Abaixo, segue um exemplo do resultado a ser obtido

          
          
#### Resultados:
![ganho](https://github.com/DBernardes/ProjetoECC/blob/master/Ganho/Relatorio%20Ganho.png)
