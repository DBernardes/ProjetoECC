# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de Eficiência Quântica.

## EQ:
  - Código para caracterização da eficiência quântica;
  - O objetivo deste experimento é determinar a eficiência quântica do CCD para uma faixa do espectro de 300 nm a 1100 nm com um passo de 10 nm, para a menor temperatura permitida. Para cada comprimento de onda medido, devem ser adquiridas três imagens com o intuito evitar erros estatísticos. Para servir de referência da quantidade de luz incidente, este mesmo ensaio foi realizado para um fotômetro, de modo que a eficiência quântica pudesse ser obtida através de uma medida relativa entre os dados deste dispositivo e da câmera. Um gráfico da EQ em função do comprimento de onda será plotado, retornando algumas informações como a maior porcentagem de conversão e comprimento de onda associado e porcentagem de conversão total.
  
#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal:
  
         ./QEcompleto.py -d'Nome_arq_fotometro' -s'lambda_min,lambda_max,passo' -n'Numero_imagens' -c'Nome_curva_de_calibração_detector' -g'Ganho' -l'Logfile'
         
    - A opção -d refere-se ao nome do arquivo do fotômetro onde estão os valores de fluxo;
    - A opção -s refere-se ao comprimento de onda mínimo e máximo e o passo utilizado no experimento, respectivamente;
    - A opção -n refere-se ao número de imagens obtidas para o mesmo comprimento de onda;
    - A opção -c refere-se ao nome do arquivo contendo os valores da curva de calibração do detector (opcional);
    - A opção -l refere-se ao nome do arquivo log gerado contendo todas as informações pertinentes ao ensaio de caracterização (opcional);
    - A opção -g refere-se ao ganho do CCD, que deve ser previamente caracterizado; caso não seja fornecido, o código adota o ganho como sendo igual a 1;    
    
Caso deseje saber quais os pontos do espectro estão dentro de um intervalo da curva de EQ, execute o comando:
         
          ./QEcompleto.py -d'Nome_arq_fotometro' -s'lambda_min,lambda_max,passo' -n'Numero_imagens' --range=vmin,vmax

#### Resultados:
![eficiencia quantica](https://cloud.githubusercontent.com/assets/23655702/22065991/ecfadd80-dd71-11e6-8dda-74eb8a75fe9d.png)
