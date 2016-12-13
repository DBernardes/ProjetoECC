# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de caracterização do ganho.

## Ganho:
  - Código para caracterização do ganho do CCD;
  - Possui como entrada quatro séries de imagens: duas de bias (subtração) e duas de flat (correção do Flat Field), retornando um arquivo .pdf com gráfico da intensidade do sinal em função da variância
de cada imagem do CCD. Sobre a curva é feito um ajuste linear, de modo que o ganho é obtido através de sua derivada.
  - Um arquivo texto deve ser fornecido contendo o nome das imagens a serem processadas no formato biasA,biasB,flatA,flatB;

#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal:
  
         ./ganhoCompleto.py --list=list --logfile='Nome do Arquivo'
      
   - A opção --logfile retorna um arquivo contendo todas as informações relacionadas ao experimento 
de aquisição das imagens. O uso deste flag  opcional.

#### Resultados:
![ganho](https://cloud.githubusercontent.com/assets/23655702/21147767/430ee33e-c13d-11e6-8bf7-42646fc8ba7b.png)
