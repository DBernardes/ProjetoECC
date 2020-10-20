# Projeto da Caracterização dos CCDs do Observatório Pico dos Dias
este repositório é possível encontrar os códigos desenvolvidos em python para caracterização dos CCDs do OPD. São eles:

    Ruído de leitura;
    Corrente de escuro;
    Ganho;
    Eficiência quântica;

Para cada um dos scritps há um conjunto de imagens que podem ser utilizadas como exemplo de teste. Para tanto, faça o download das imagens e, também, de seu respectivo código. Siga as instruções e os resultados serão salvos no diretório atual. Compare os resultados obtidos com aqueles apresentados na página. 

## Descrição do código 


## Rodando as caracterizações

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Dependências:
Lista das bibliotecas que devem ser instaladas antes da execução dos códigos de cada caracterização 

  - numpy
  - matplotlib
  - astropy
  - optparse
  - scipy
  - math
  - os
  - sys
  
  Para instalar os pacotes apresentados, pode-se utilizar o comando pip, na forma  
  
```
pip install <package_name>
```

  - ccdproc
  
  Obs: uma das despendências do pacote ccdproc deve estar com problemas. Contudo, para a execução deste código, basta copiar o diretório ccdproc disponível no repositório GitHub do Projeto Astropy ([link](https://github.com/astropy/ccdproc)) e colar dentro da pasta das bibliotecas do python de seu computador.       



### Instalação
Clone este repositório utilizando o comando ``` git clone https://github.com/DBernardes/Artificial-Images-Generator.git ```

## Running the tests

To run a simple test, you only need to execute the run.py file and the image would be created in your current directory. The run.py file will provide to the AIG the basic information for its execution, that is the star flux, in photons/s; the sky flux, in photons/pix/s, the standard deviation of the Gaussian, in pixels, and the operation mode of the CCD. In particular, the CCD operation mode should be a python dictionary with the control parameters used to configure the acquisition of the SPARC4 cameras. They are the Electron Multiplying Mode (em_mode), the Electron Multiplying Gain (em_gain), the Pre-amplification (preamp), the Horizontal Shift Speed (hss), the Pixels Binning (bin), and the Exposure Time (texp). Below, it is presented the accepted values for each parameter previously described.

- em_mode: 0 or 1
- em_gain: from 2 to 300
- preamp: 1 or 2
- hss: 0.1, 1, 10, 20, and 30
- bin: 1 or 2
- texp: greater or equal than 1e-5

Beyond the paramaters presented before, there are a set of optional paramaters. They are the CCD temperature (ccd_temp), the CCD serial number (serial_number), the image bias level (bias_level), and the directory where the image should be saved (image_dir)

- ccd_temp: from 0 ºC to -70 ºC
- serial_number: 9914, 9915, 9916, or 9917
- bias_level: integer and greater or equal than 1
- image_dir: string

## Autores e contato

* **Denis Bernardes**: 

email: denis.bernardes099@gmail.com 

## License

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE.md] (LICENSE.md) para obter detalhes
