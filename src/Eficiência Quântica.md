# Roteiro:
> Neste roteiro é apresentado uma breve explicação e exemplo do código de Eficiência Quântica.

## EQ:
  - Código para caracterização da eficiência quântica;
  - O objetivo deste experimento é determinar a eficiência quântica do CCD para uma faixa do espectro de 300 nm a 1100 nm com um passo de 10 nm, para a menor temperatura permitida. Para cada comprimento de onda medido, devem ser adquiridas três imagens com o intuito evitar erros estatísticos. Para servir de referência da quantidade de luz incidente, este mesmo ensaio foi realizado para um fotômetro, de modo que a eficiência quântica pudesse ser obtida através de uma medida relativa entre os dados deste dispositivo e da câmera. Um gráfico da EQ em função do comprimento de onda será plotado, retornando algumas informações como a maior porcentagem de conversão e comprimento de onda associado e porcentagem de conversão total.
  
#### Exemplo:
  - Após baixar e extrair os arquivos, execute o comando via terminal sobre o diretório onde se encontram as imagens:
  
         ./QEcompleto.py      
    
Caso deseje saber quais os pontos do espectro estão dentro de um intervalo da curva de EQ, execute o comando:
         
          ./QEcompleto.py --range=vmin,vmax          



#### Resultados:
![eficiencia quantica](https://cloud.githubusercontent.com/assets/23655702/22292054/a85a9af6-e2f0-11e6-9e26-0fcb26909616.png)
