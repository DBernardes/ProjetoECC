# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de caracterização do ganho.

## Ganho:
  - Código para caracterização do ganho do CCD;
  - O objetivo deste experimento é a caracterização do ganho do CCD para uma determinada taxa de leitura e pré-amplificação. Para tanto, as imagens devem ser adquiridas da seguinte forma: dez imagens de bias devem sem obtidas consecutivamente; feito isso, deve-se expor o CCD à uma iluminação uniforme (Flat Field) que produza uma imagem com número médio de contagens pertencente a um intervalo de 20% a 60% do intervalo dinâmico do CCD. Um conjunto de cinco imagens (imagens flat) devem ser adquiridas em sequência para esta configuração. Uma série de conjuntos deve ser adquirida para dez valores médios de contagens ao longo do intervalo especificado. O código plota um gráfico da intensidade do sinal em função da variância e, através do coeficiente linear da curva, retorna qual o valor do ganho.
  - Em seguida, é plotado um segundo gráfico dos resíduos dos dados expressos pela subtração do valor da intensidade do sinal calculada pelo valor do ajuste linear sobre o mesmo ponto; o resultado esperado é uma curva em função da variância ao redor de zero. 

 

#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram as imagens:
  
         ./ganhoCompleto.py -f'Flat','nImages' -b'Bias' 
      
   - A opção -f refere-se à uma indicação para o código do nome das imagens de flat (parte do nome em comum) e o número de imagens adquiridas para cada intensidade de luz;
   - A opção -b refere-se à uma indicação para o código do nome das imagens de bias (parte do nome em comum); Os resultados aparecerão no diretório atual;
   
Caso haja o interesse de gerar um arquivo Log com as informações do experimento, executar o seguinte comando:

         ./ganhoCompleto.py -f'Flat','nImages'  -b'Bias' --logfile='Nome do Arquivo'
          
          
#### Resultados:
![ganho](https://cloud.githubusercontent.com/assets/23655702/22106976/908f5686-de32-11e6-8d3a-e892f602171c.png)
