# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de caracterização do ganho.

## Ganho:
  - Código para caracterização do ganho do CCD;
  - O objetivo deste experimento é a caracterização do ganho do CCD para uma determinada taxa de leitura e pré-amplificação. Para tanto, as imagens devem ser adquiridas da seguinte forma: dez imagens de bias devem sem obtidas consecutivamente; feito isso, deve-se expor o CCD à uma iluminação uniforme (Flat Field) que produza uma imagem com número médio de contagens pertencente a um intervalo de 20% a 60% do intervalo dinâmico do CCD. Um conjunto de cinco imagens (imagens flat) devem ser adquiridas em sequência para esta configuração. Uma série de conjuntos deve ser adquirida para dez valores médios de contagens ao longo do intervalo especificado. O código plota um gráfico da intensidade do sinal em função da variância e, através do coeficiente linear da curva, retorna qual o valor do ganho.
  - Em seguida, é plotado um segundo gráfico dos resíduos dos dados expressos pela subtração do valor da intensidade do sinal calculada pelo valor do ajuste linear sobre o mesmo ponto; o resultado esperado é uma curva em função da variância ao redor de zero. 

 

#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram as imagens:
  
         ./ganhoCompleto.py -bBias -fFlat,5 -c612,588,100 
      
   - A opção -f refere-se à uma indicação para o código do nome das imagens de flat (parte do nome em comum) e o número de imagens adquiridas para cada intensidade de luz;
   - A opção -b refere-se à uma indicação para o código do nome das imagens de bias (parte do nome em comum); Os resultados aparecerão no diretório atual;
   - A opção -c refere-se ao parâmetros da caixa onde serão retirados os pixels de cada imagem, seguindo a formatação (xcoord, ycoord,dimensão)
Caso haja o interesse de gerar um arquivo Log com as informações do experimento, executar o seguinte comando:

         ./ganhoCompleto.py -bBias -fFlat,5 -c612,588,100 -l
          
          
#### Resultados:
![ganho](https://user-images.githubusercontent.com/23655702/28124798-16fad2b2-66fb-11e7-98da-ed21cf9d7001.png)
