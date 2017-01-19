# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de bias.

## Bias:
  - Código para caracterização do ruído de leitura;
  - Possui como entrada uma série de imagens, retornando um arquivo .pdf com um histograma,
gradiente e variação temporal sobre os pixels das imagens;

#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram as imagens:
  
         ./biasCompleto.py --list=list --logfile='Nome do Arquivo'
      
  - A opção list refere-se a um arquivo texto contendo uma lista com o nome de cada imagem de série.
  - A opção --logfile retorna um arquivo contendo todas as informações relacionadas ao experimento 
de aquisição das imagens. O uso deste flag é opcional.

#### Resultados:
![relatorio bias](https://cloud.githubusercontent.com/assets/23655702/21142404/0db0c4c8-c129-11e6-97da-111fe046d321.png)



  
