# Roteiro
> Aqui serão apresentadas as instruções sobre o código de caracterização da Corrente de Escuro.

# DC:
   - Código para caracterização da corrente de escuro (DC). O processamento dos dados inclue um gráfico com a variação das constagens de cada série em função do tempo de exposição, um gráfico da corrente de escuro em função da temperatura e dois gráficos da corrente de escuro ao longo das direções horizontal e vertical dos pixels do CCD.
   - Possui como entrada até seis séries de imagens diferentes, cada uma realizada para uma temperatura diferente.
Cada série deve estar em um diretório, junto com duas listas: 

      - bias = contendo o nome das imagens de bias para subtração das imagens;
      - dark = contendo o nome das imagens usadas para caracterização da corrente de escuro;
   - É necessário ainda uma terceira lista contendo o nome de cada diretório que separa as séries;
   
### Exemplo:
   - Após baixar e extrair os arquivos, execute o comando via terminal:
   
          ./DCcompleto.py -i'Lista_diretorios' -b'Lista_bias' -d'Lista_dark' -eExposure -lLogfile
    
    - A opção -i refere-se à lista de diretórios que contém cada série de imagens para as respectivas temperaturas.
    - A opção -d refere-se à lista de imagens de bias usadas na redução dos dados.
    - A opção -d refere-se à lista de imagens para caracterização da corrente de escuro.
    - A opção -e refere-se ao keyword usado no cabeçalho das imagens da câmera para indicar tempo de exposição (keyword varia de câmera para câmera). 

### Resultados:
![relatorio dc](https://cloud.githubusercontent.com/assets/23655702/20596138/1e853c84-b224-11e6-8703-095d6ae7595b.png)
