# Processamento Digital de Imagens

Dentro deste repositório possui 2 trabalhos que foram desenvolvidos durante a matéria de processamento digital de imagens no curso de Ciências da Computação - UEM

## Cubo RGB

O Objetivo do primeiro trabalho é implementar a geração de imagens coloridas que sejam "fatias" do cubo que representa o espaço de cor RGB, feito da seguinte forma:

    - a face escolhida à partir da qual será selecionada a "fatia" (a face deve ser indexada/rotulada por um valor de 1 a 6)

    - um valor i (de 0 a 255) para indexar a i-ésima fatia.

O programa gera e mostra a i-ésima "fatia" em relação à face escolhida como referência. Considere que o cubo RGB tem profundidade de 24 bits.

Foram utilizados para implementar: Python juntamente com a biblioteca OpenCV, mas poderia ser utilizado também a biblioteca scikit-image para carregar/salvar/mostrar as imagens.

Para compilar o algoritmo:

```
$py cubo/cubo.py
```

### Filtragem High-Boost

O objetivo do segundo trabalho é implementar e testar o método de filtragem conhecida como high-boost, utilizado para aumento de nitidez de imagens digitais. O método está descrito na seção 3.6.3 do livro do Gonzales&Woods, 3a. edição, na página 107. O trabalho reconhece imagens com nitidez reduzida e devolve outra imagem com nitidez aguçada, conforme descrita pelo método. A página do livro do Gonzalez oferece o download das imagens utilizadas no livro:

(https://www.imageprocessingplace.com/root_files_V3/image_databases.htm)

A filtragem passa-baixa utilizada neste trabalho foi realizada no domínio espacial (convolução, Seção 3.6.3). Foi priorizado a utilização de fatiamento (slicing) no lugar de estruturas de repetição.

para compilar o algoritmo:

```
$py high_boost/filtragem.py
```

Ao momento que o usuário rodar, certifique-se de que o caminho para a imagem esteja correta dentro do arquivo .py, para sim obter melhor análise da imagem.
