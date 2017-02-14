# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de Eficiência Quântica.

## EQ:
  - Código para caracterização da eficiência quântica;
  - O objetivo deste experimento é determinar a eficiência quântica do CCD para uma faixa do espectro de 300 nm a 1100 nm com um passo de 20 nm, para a menor temperatura permitida. Para cada comprimento de onda medido, devem ser adquiridas três imagens com o intuito evitar erros estatísticos. Devido à um fluxo adicional incidente sobre o CCD devido ao tempo necessária para abertura e fechamento do shutter, são adquiridas duas séries de imagens: a primeira possuindo a metade do tempo de exposição da segunda e, através da subtração da segunda pela primeira, este fluxo excedente é subtraído. Para servir de referência da quantidade de luz incidente, este mesmo ensaio foi realizado para um fotômetro, de modo que a eficiência quântica pudesse ser obtida através de uma medida relativa entre os dados deste dispositivo e da câmera. Um gráfico da EQ em função do comprimento de onda será plotado, retornando algumas informações como a maior porcentagem de conversão e comprimento de onda associado e porcentagem de conversão total.
  
#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram as imagens:
  
         ./QEcompleto.py 
         
Ao executar o comando pela primeira vez, irá aparecer uma mensagem pedindo para preencher um arquivo contendo as informações do ensaio:
  - Espectro (nm): espectro utilizado no ensaio (em nanômetros); nele devem constar o comprimento de onda inicial, comprimento de onda final e o passo utilizado, respectivamente;
  - Numero de imagens adquiridas para cada comprimento de onda;
  - nome do arquivo contendo a curva de transmissão do filtro de densidade (opcional);
  - nome do arquivo contendo a curva de Eficiência Quântica do fabricante (opcional);
  - nome do arquivo contendo os dados detector;
  - nome arquivo Log (opcional)
  - tag (nome ou parte do nome) das imagens dos dados e referencia; esta opção servirá para o código separar quais as imagens de referência e quais as imagens de fluxo;
  - ganho do CCD.
  
Preenchendo o arquivos com as informações, execute novamente o comando.
Caso deseje saber quais os pontos do espectro estão dentro de um intervalo da curva de EQ, execute o comando:
         
          ./QEcompleto.py --range=vmin,vmax          



#### Resultados:
![eficiencia quantica](https://cloud.githubusercontent.com/assets/23655702/22292054/a85a9af6-e2f0-11e6-9e26-0fcb26909616.png)
