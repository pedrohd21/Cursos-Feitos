# Aula 12 Folhas de Estilos
* Color colore a letra 
* Background colore o fundo do texto
### Ex:
color: red; 

background: black; 

# Aula 13 Primeiras regras css

* font-family decide o formato da letra
* font-size define o tamanho do texto.
* font-style Define quanto o texto é inclinado ou seja italico.
* font-variant Define qual glifo usar para cada letra.
* font-weigth define a espessura do texto, dependendo do texto, nn faz muito efeito.
# ---------------------------------------------
* font-align Define como o conteúdo do texto do elemento é alinhado horizontalmente.
* font-decoration Define como o conteúdo do texto do elemento é decorado, usando o none tira a formatação do texto.
* text-indent Define o recuo da primeira linha de texto do elemento.
* text-transform Define como o conteúdo do texto deve ser transformado.

   * text-transform: capitalize;

      * Transforma a primeira letra de cada palavra em letra maiúscula .

   * text-transform: uppercase;

      * Transforma todas as letras em maiúsculas letras.

    * text-transform: lowercase;

        * Transforma todas as letras em minúsculas .


# Aula 14 classes e id
* class so colocar um ponto.
* id so colocar um #.

# Aula 16 Box Model
* padding-bottom Define o espaço dentro do elemento, na parte inferior.
* padding-left Define o espaço dentro do elemento, no lado esquerdo .
    * exemplo
    * Primeiro item
        * Alvo
    * Terceiro item
* padding-right Define o espaço dentro do elemento, no lado direito.
* padding-top Define o espaço dentro do elemento, na parte superior.
* padding Propriedade abreviada para padding-top padding-right padding-bottom e padding-left.
Ao usar 4 valores:

        o primeiro valor é para top
        o segundo valor é para a direita
        o terceiro valor é para baixo
        o quarto valor é para a esquerda
        Para lembrar a ordem , comece no topo e vá no sentido horário .

# ------------------------
* margin-bottom Define o espaço fora do elemento, na parte inferior.

    ![Exemplo](imagem.png)
* margin-left Define o espaço fora do elemento, no lado esquerdo.
* margin-right Define o espaço fora do elemento, no lado direito.
* margin-top Define o espaço fora do elemento, no parte superior .
* margin Propriedade abreviada para margin-top margin-right margin-bottom e margin-left.

* Ao usar 4 valores:
    * o primeiro valor é para top
    * o segundo valor é para a direita
    * o terceiro valor é para baixo
    * o quarto valor é para a esquerda
    * Para lembrar a ordem , comece no topo e vá no sentido horário .

# --------------------
* width Define a largura do elemento, da pra usar px, % ou auto.
* heigth Define a altura do elemento da pra usar px, % ou auto.

# --------------------
* border-color Define a cor das bordas do elemento.
* border-style Define o estilo das bordas do elemento da uma pesquisa pra ver qual a melhor pro momento.
* border-width Define a largura das bordas do elemento.

# Aula 19 link

* a:hover{Colocar cor no link, e um background quando passa o mouse em cima}
* a:active{Coloca cor quando clica} 
* list-style-type: disc; Define o tipo do marcador de um item da lista .

# Aula 24 Imagens

* background-image Define uma imagem como plano de fundo do elemento.
* background-repeat Define como a imagem de plano de fundo se repete no plano de fundo do elemento, iniciando na posição de plano de fundo.
    * background-repeat: repeat;

        * A imagem de fundo se repetirá horizontalmente e verticalmente .
        ![](imagem1.png)
    
* background-repeat: repeat-x;

        A imagem de fundo se repetirá apenas horizontalmente .
* background-repeat: repeat-y;

        A imagem de fundo será repetida apenas na vertical .

* background-repeat: no-repeat;

        A imagem de fundo aparecerá apenas uma vez .

* background-position Define a posição da imagem de fundo.
    * Você pode usar uma combinação de palavras-chave de posição : 
        * center
        * top
        * bottom
        * lefte 
        * right

* background-attachment Define como a imagem de fundo se comportará ao rolar a página.
background-attachment: scroll;

        A imagem de fundo será rolada com a página. Ele também se posicionará e se redimensionará de acordo com o elemento ao qual é aplicado.

* background-attachment: fixed;

        A imagem de fundo não rolará com a página e permanecerá posicionada de acordo com a janela de exibição. Ele também se posicionará e se redimensionará de acordo com a janela de exibição. Como resultado, a imagem de plano de fundo provavelmente será apenas parcialmente visível.

* background-size Define o tamanho da imagem de fundo.
    * background-size: contain;

        * A palavra contain- chave redimensionará a imagem de plano de fundo para garantir que ela permaneça totalmente visível.
        
            ![](img1.png)
    * background-size: cover;

        * A palavra cover- chave redimensionará a imagem de plano de fundo para garantir que o elemento esteja totalmente coberto .
            ![](img2.png)