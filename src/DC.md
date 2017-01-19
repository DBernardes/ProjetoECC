# Roteiro
> Neste roteiro são apresentadas as instruções sobre o código de caracterização da Corrente de Escuro (DC).

# DC:
   - O processamento dos dados inclue um gráfico com a variação das constagens de cada série em função do tempo de exposição, um gráfico da corrente de escuro em função da temperatura e dois gráficos da corrente de escuro ao longo das direções horizontal e vertical dos pixels do CCD.
   - Possui como entrada até seis séries de imagens diferentes, cada uma realizada para uma temperatura diferente.
Cada série deve estar em um diretório, junto com duas listas: 

      - bias = contendo o nome das imagens de bias para subtração das imagens;
      - dark = contendo o nome das imagens usadas para caracterização da corrente de escuro;
   - É necessário ainda uma terceira lista contendo o nome de cada diretório que separa as séries;
   
### Exemplo:
   - Após baixar e extrair os arquivos, execute o comando via terminal:
   
          ./DCcompleto.py -iDirectories -bBias -dDark -eEXPOSURE
    - A opção -i refere-se à lista de diretórios que contém cada série de imagens para as respectivas temperaturas.
    - A opção -b refere-se à lista de imagens de bias usadas na redução dos dados.
    - A opção -d refere-se à lista de imagens para caracterização da corrente de escuro.
    - A opção -e refere-se ao keyword usado no cabeçalho das imagens da câmera para indicar tempo de exposição (keyword varia de câmera para câmera). 
    
 Caso haja interesse em gerar um arquivo Log contendo as informações do experimento, execute o comando:

      ./DCcompleto.py -iDirectorys -bBias -dDark -eEXPOSURE --logfile='Nome do arquivo'
      
 Há uma opção -c que refere-se aos parâmetros da caixa de pixels que será retirada das imagens no código ''DCvariacaoTemporal'' com o fim de uma caracterização mais precisa. Caso esta opção no seja fornecida, o programa considera as variáveis ''coordx'' e ''coordy'' como sendo as coordenadas do pixel central da imagem e a dimensão da caixa será 100 pixels;

       ./DCcompleto.py -iDirectorys -bBias -dDark -eEXPOSURE -c'coordx','coordy','dimensão'



### Resultados:
![relatorio dc](https://cloud.githubusercontent.com/assets/23655702/21142571/fee9d168-c129-11e6-9115-24d5dad37bbb.png)
