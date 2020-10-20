# Roteiro
> Neste roteiro são apresentadas as instruções sobre o código de caracterização da Corrente de Escuro (DC).

# DC:
   - Este roteiro visa caracterizar a corrente de escuro dos CCDs, descrevendo seu comportamento em função do tempo de exposição e da temperatura. Para tanto devem ser obtidas 10 imagens de bias e 10 imagens de corrente de escuro, variando o tempo de exposição de 0 a 60 segundos (6 segundos entre cada uma). Em seguida, obter imagens para tempos de exposição de 2, 3, 4 e 5 minutos. Essa série deve ser feita para temperaturas de -30, -40, -50, -60 e -70°C. Ao final do procedimento, serão cinco séries de dados contendo 10 imagens de bias e 15 imagens de corrente de escuro para cada temperatura.
   - O processamento dos dados inclue um gráfico com a variação da mediana das constagens de cada série em função do tempo de exposição, um gráfico da corrente de escuro em função da temperatura e dois gráficos da corrente de escuro ao longo das direções horizontal e vertical dos pixels do CCD para as imagens de menor temperatura.
   - Possui como entrada até seis séries de imagens diferentes, cada uma realizada para uma temperatura diferente. Cada série deve estar separada em um diretório (bias + dark).
  
   
### Exemplo:
   - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram os diretórios das imagens:
   
          ./DCCharact.py -iDC -bBias -dDC -g3.31 -c512,512,100 
          
   - A opção -i refere-se ao keyword dos diretórios (parte do nome em comum) para o código identificar quais são os diretórios que contém as imagens para as respectivas temperaturas.
   - A opção -b refere-se ao keyword das imagens de bias (parte do nome em comum) usadas na redução dos dados.
   - A opção -d refere-se ao keyword das imagens para caracterização da corrente de escuro (parte do nome em comum).
   - A opção -g refere-se ao ganho do CCD para as respectivas taxas de leitura e pré - amplificação;
   - A opção -c refere-se aos parâmetros da caixa onde serão retirados os pixels de cada imagem para a caracterização temporal da corrente de escuro, seguindo a formatação (xcoord, ycoord, dimensão).
   - Há uma opção -e que refere-se ao keyword usado no cabeçalho das imagens da câmera para indicar tempo de exposição (keyword varia de câmera para câmera). Caso essa opção não seja fornecida, o código irá considerar keyword='EXPOSURE'
    
 Caso haja interesse em gerar um arquivo Log contendo as informações do experimento, execute o comando:

      ./DCcompleto.py -iDC -bBias -dDC -g3.31 -c512,512,100 -l
 

### Resultados:
![relatorio dc](https://user-images.githubusercontent.com/23655702/28124742-f1c0f166-66fa-11e7-8072-f0f8d851ba84.png)
