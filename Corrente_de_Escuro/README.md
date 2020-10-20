# Roteiro
Neste roteiro é apresentada uma breve explicação sobre o código de caracterização da Corrente de Escuro (DC) e o passo-a-passo para a execução do código.

Este ensaio visa caracterizar a corrente de escuro dos CCDs, descrevendo seu comportamento em função do tempo de exposição e da temperatura. Para tanto devem ser obtidas 10 imagens de bias e 10 imagens de corrente de escuro, variando o tempo de exposição de 0 a 60 segundos (6 segundos entre cada uma). Em seguida, obter imagens para tempos de exposição de 2, 3, 4 e 5 minutos. Essa série deve ser feita para temperaturas de -30, -40, -50, -60 e -70°C. Ao final do procedimento, serão cinco séries de dados contendo 10 imagens de bias e 15 imagens de corrente de escuro para cada temperatura.

O processamento dos dados inclue um gráfico com a variação da mediana das constagens de cada série em função do tempo de exposição, um gráfico da corrente de escuro em função da temperatura e dois gráficos da corrente de escuro ao longo das direções horizontal e vertical dos pixels do CCD para as imagens de menor temperatura. O software permite a caracterização de até seis séries de imagens diferentes, cada uma realizada para uma temperatura. Cada série deve estar separada em um diretório (bias + dark).
  
   
### Rodando o código:
- Baixar e extrair as imagens presentes no arquivo .ZIP apresentado neste diretório.
- Abrir o arquivo run.py. Este arquivo executa o código da caracterização desenvolvido. Para tanto, devem ser fornecidos o ganho do CCD e o caminho do diretório onde as imagens foram extraídas.
- Após isso, o arquivo pode ser executado e o relatório da caracterização aparecerá no diretório das imagens.
- Abaixo, segue um exemplo do resultado a ser obtido
 

### Resultados:
![relatorio dc](https://github.com/DBernardes/ProjetoECC/blob/master/Corrente_de_Escuro/Relat%C3%B3rio%20Corrente%20de%20Escuro.png)
