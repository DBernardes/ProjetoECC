# Roteiro
> Neste roteiro são apresentadas as instruções sobre o código de caracterização da Corrente de Escuro (DC).

# DC:
   - Este roteiro visa caracterizar a corrente de escuro dos CCDs, descrevendo seu comportamento em função do tempo de exposição e da temperatura. Para tanto devem ser obtidas 10 imagens de bias e 10 imagens de corrente de escuro, variando o tempo de exposição de 0 a 60 segundos (6 segundos entre cada uma). Em seguida, obter imagens para tempos de exposição de 2, 3, 4 e 5 minutos. Essa série deve ser feita para temperaturas de -30, -40, -50, -60 e -70°C. Ao final do procedimento, serão cinco séries de dados contendo 10 imagens de bias e 15 imagens de corrente de escuro para cada temperatura.
   - O processamento dos dados inclue um gráfico com a variação da mediana das constagens de cada série em função do tempo de exposição, um gráfico da corrente de escuro em função da temperatura e dois gráficos da corrente de escuro ao longo das direções horizontal e vertical dos pixels do CCD para as imagens de menor temperatura.
   - Possui como entrada até seis séries de imagens diferentes, cada uma realizada para uma temperatura diferente. Cada série deve estar separada em um diretório (bias + dark).
  
   
### Exemplo:
   - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram os diretórios das imagens:
   
          ./DCcompleto.py -iDirectories -bBias -dDark 
    - A opção -i refere-se ao keyword dos diretórios (parte do nome em comum) para o código identificar quais são os diretórios que contém as imagens para as respectivas temperaturas.
    - A opção -b refere-se ao keyword das imagens de bias (parte do nome em comum) usadas na redução dos dados.
    - A opção -d refere-se ao keyword das imagens para caracterização da corrente de escuro (parte do nome em comum).
    - Há uma opção -e que refere-se ao keyword usado no cabeçalho das imagens da câmera para indicar tempo de exposição (keyword varia de câmera para câmera). Caso essa opção não seja fornecida, o código irá considerar keyword='EXPOSURE'
    
 Caso haja interesse em gerar um arquivo Log contendo as informações do experimento, execute o comando:

      ./DCcompleto.py -iDirectorys -bBias -dDark  --logfile='Nome do arquivo'
      
 Há uma opção -c que refere-se aos parâmetros da caixa de pixels que será retirada das imagens no código ''DCvariacaoTemporal'' com o fim de uma caracterização mais precisa. Caso esta opção no seja fornecida, o programa considera as variáveis ''coordx'' e ''coordy'' como sendo as coordenadas do pixel central da imagem e a dimensão da caixa será 100 pixels;

       ./DCcompleto.py -iDirectorys -bBias -dDark -c'coordx','coordy','dimensão'



### Resultados:
![relatorio dc](https://cloud.githubusercontent.com/assets/23655702/21142571/fee9d168-c129-11e6-9115-24d5dad37bbb.png)
