# Roteiro:
> Aqui será apresentada uma breve explicação e exemplo do código de caracterização do ganho.

## Ganho:
  - Código para caracterização do ganho do CCD;
  - Possui como entrada quatro séries de imagens: duas de bias (subtração) e duas de flat (correção do Flat Field), retornando um arquivo .pdf com gráfico da intensidade do sinal em função da variância
de cada imagem do CCD. Sobre a curva é feito um ajuste linear, de modo que o ganho é obtido através de sua derivada.
  - Um arquivo texto deve ser fornecido contendo o nome das imagens a serem processadas no formato biasA,biasB,flatA,flatB;

#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal:
  
         ./ganhoCompleto.py --list=list --logfile='Nome do Arquivo'
      
   - A opção --logfile retorna um arquivo contendo todas as informações relacionadas ao experimento 
de aquisição das imagens. Não haverá implicação nenhuma nos resultados caso essa informação não seja fornecida;

#### Resultados:
![ganho](https://cloud.githubusercontent.com/assets/23655702/20624732/c49794ec-b2f5-11e6-9176-e613a41d08e5.png)
  
