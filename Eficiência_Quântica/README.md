# Roteiro:
Neste roteiro é apresentado uma breve explicação da caracterização da Eficiência Quântica do CCD e um passo-a-passo para a execução do código.
  
 O objetivo deste experimento é determinar a eficiência quântica do CCD para uma faixa do espectro de 350 nm a 1100 nm com um passo de 50 nm, para a menor temperatura permitida. Para cada comprimento de onda medido, devem ser adquiridas duas imagens do spot de luz do monocormador. A segunda imagem deve ser obtida com o dobro do tempo de exposição da primeira. Este procedimento serve para a correção devido ao fluxo adicional incidente sobre o CCD por causa do tempo de abertura e fechamento do shutter. Para servir de referência da quantidade de luz incidente, este mesmo prcedimento deve ser realizado para um fotômetro, de modo que a eficiência quântica possa ser obtida através da medida relativa entre os dados do fotômetro e da câmera. Um gráfico da EQ em função do comprimento de onda será plotado, retornando algumas informações como a maior EQ obtida e seu respectivo comprimento de onda.
  
#### Rodando o código:
- Baixar e extrair as imagens presentes no arquivo .ZIP apresentado neste diretório.
- Abrir o arquivo run.py. Este arquivo executa o código da caracterização desenvolvido. Para tanto, deve ser fornecido o caminho do diretório onde as imagens foram extraídas.         
- Ao executar o comando pela primeira vez, irá aparecer uma mensagem pedindo para preencher um arquivo contendo as informações do ensaio. Neste arquivo, deve-se preencher:

> Espectro (nm): espectro utilizado no ensaio (em nanômetros); nele devem constar o comprimento de onda inicial, comprimento de onda final e o passo utilizado, respectivamente;

> nome do arquivo contendo a curva de transmissão do filtro de densidade (opcional);

> nome do arquivo contendo a curva de Eficiência Quântica do fabricante (opcional);

> nome do arquivo contendo os dados detector;

> tag (parte do nome) do par de imagens; esta opção servirá para o código separar os pares de imagens para subtração

> ganho do CCD.
  
- Preenchendo o arquivos com as informações, execute o arquivo novamente. O relatório da caracterização aparecerá no diretório das imagens.
- Abaixo, segue um exemplo do resultado a ser obtido


#### Resultados:
![eficiencia quantica](https://github.com/DBernardes/ProjetoECC/blob/master/Efici%C3%AAncia_Qu%C3%A2ntica/Relat%C3%B3rio%20Eficiencia%20Quantica.png)

