# 🖼️ Redução de Dimensionalidade em Imagens

Este projeto foi desenvolvido como parte de um desafio da **DIO**, com o objetivo de entender como o computador processa imagens em nível de matriz de pixels, sem o uso de bibliotecas externas (como Pillow ou OpenCV).

## 🎯 O Desafio
Transformar uma imagem colorida (RGB) em:
1.  **Escala de Cinza**: Redução de 3 canais de cor para 1 canal de intensidade.
2.  **Binarizada (Preto e Branco)**: Redução extrema para apenas dois valores (0 e 255) com base em um limiar (threshold).

## 🛠️ Lógica Implementada
* **Manipulação de Arquivos**: Leitura de arquivos binários no formato **PPM P6** e conversão para **PPM P3** (ASCII) para manipulação textual.
* **Cálculo de Média**: Cada pixel cinza é a média aritmética dos valores de Vermelho, Verde e Azul:  
  `cinza = (R + G + B) // 3`
* **Limiarização**: Se `cinza > 127`, o pixel torna-se branco (255), caso contrário, preto (0).
