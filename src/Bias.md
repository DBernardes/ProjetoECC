# Roteiro:
> Aqui será apresentada uma breve explicação e exemplo de cada um dos algoritmos .

## Bias:
  - Algoritmo para caracterização do ruído de leitura (bias);
  - Possui como entrada uma série de imagens, retornando um arquivo .pdf com um histograma,
gradiente e variação temporal sobre os pixels das imagens;

#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal:
  
         ./biasCompleto.py --list=list --logfile='Nome do Arquivo'
      
  - A opção list refere-se a um arquivo texto contendo uma lista com o nome de cada imagens de série
  - A opção --logfile retorna um arquivo contendo todas as informações relacionadas ao experimento 
de aquisição das imagens. Não haverá implicação nenhuma nos resultados caso essa informação não seja fornecida;

#### Resultados:

![relatorio bias](https://cloud.githubusercontent.com/assets/23655702/20595444/0c996ac0-b221-11e6-94e5-4e0b5d1700e8.png)


  
