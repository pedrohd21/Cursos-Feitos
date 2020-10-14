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

# Aula 25 Estruturando Layouts com Semântica

* header Define o cabeçalho de uma página da web ou seção.
~~~ 
<header>
  <h1>HTML Reference</h1>
  <nav>
    <a>Home</a>
    <a>About</a>
    <a>Contact</a>
  </nav>
</header> 
~~~
* nav Define uma seção com links de navegação .
~~~
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
  </nav>
~~~
* main Define o conteúdo principal de uma página da web. Pode ser exibido com uma barra lateral.
~~~
<main>
  <h1>My blog post</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra nec nulla vitae mollis.</p>
  <p>etc.</p>
</main>

<aside>
  <h3>About the author</h3>
  <p>Frontend Designer from Bordeaux, currently working for Improbable in sunny London.</p>
</aside>
~~~
* footer Define o rodapé de uma página da web ou seção.
~~~
<footer>
  HTML Reference - A free reference to all HTML5 elements and attributes
</footer>
~~~
* Outras tags Semanticas
* section Define uma seção dentro de uma página da web.
~~~
<section>
  <h2>Section title</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra nec nulla vitae mollis.</p>
</section>
~~~
* article Define um bloco de conteúdo independente que pode existir em qualquer contexto.
Pode ter seu próprio cabeçalho, rodapé, seções ... Útil para uma lista de postagens do blog.
~~~
<article>
  <header>
    <h3>
      <a href="/my-blog-post">My blog post</a>
    </h3>
  </header>
  <section>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra nec nulla vitae mollis.</p>
  </section>
  <footer>
    <small>
      Posted on <time datetime="2017-04-29T19:00">Apr 29</time> in <a href="/category/code">Code</a>
    </small>
  </footer>
</article>
~~~
* aside Define um bloco de conteúdo relacionado ao conteúdo principal. Exibido como uma barra lateral normalmente.
~~~
<main>
  <h1>My blog post</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra nec nulla vitae mollis.</p>
  <p>etc.</p>
</main>

<aside>
  <h3>About the author</h3>
  <p>Frontend Designer from Bordeaux, currently working for Improbable in sunny London.</p>
</aside>
~~~

* Outras tags não Semanticas
* div
* span

# 29 Propriedade display, inline, block e inline-block

* display Define o comportamento de exibição do elemento.
    * display: none;
        * O elemento é completamente removido , como se não estivesse no código HTML em primeiro lugar.
    * display: inline;

        * O elemento é transformado em um elemento embutido : se comporta como texto simples.
        ![](im1.png)

    * display: block;

        * O elemento é transformado em um elemento de bloco : começa em uma nova linha e ocupa toda a largura.
        ![](im2.png)

    * display: inline-block;
        * O elemento compartilha propriedades de um elemento embutido e um bloco :

        * inline porque o elemento se comporta como texto simples e se insere em um bloco de texto
        Bloquear porque você pode aplicar heighte widthvalores
        Por exemplo, este elemento possui:
            ~~~
            .elemento{
            altura: 3em;
            largura: 60px;
            }
            ~~~
            ![](im3.png)

# 31 box-sizing
![](im4.png)
![](im5.png)

# 32 float
![](im6.png)
![](im7.png)
![](im8.png)


# Tags Html

* Tags HTML e seus Significados
* DOCTYPE: define o tipo de documento
* html: define o início do documento html, todos as demais tags devem estar dentro desta tag
* head: cabeçalho onde ficar os metadados do documento, como metatgs, css e javascript
* title: define o título do documento, mostrado na barra de títulos do navegador e como link nos mecanismos de busca
* base: define a url base do documento
* link: utilizado para linkar um arquivo de imagem ou css a página html
* script: utilizado para escrever ou anexar um arquivo normalmente javascript a página
* meta: metatags, como charset, description, viewport ou keywords
* style: utilizada para adicionar um código css a página
* body: corpo ou área principal do documento, dentro deste deve ficar o conteúdo da sua página
* header: define um cabeçalho da página ou de uma seção, normalmente pode conter um menu (nav), um logo ou link
* nav: define uma área de navegação contendo links, para a formação de menus com hiperlinks
* footer: define o rodapé de uma página ou seção
* main: define o conteúdo principal da página, deve ser utilizado apenas uma única vez em cada página
* section: define uma seção do documento
* article: pode ser um post ou notícia de um fórum ou blog, define um conteúdo independente
* h1 a h6: representam 6 níveis de títulos, sendo o h1 de maior importância
* p: define um parágrafo
* br: define uma quebra de linha
* div: define uma camada sem formatação, genérico
* ul: define uma lista não ordenada
* li: define um elemento ou item da lista não ordenada
* a: define um link que deve ser apontado com o atributo href
* img: define a utilização de uma imagem (JPG, GIF, PNG e outras). A imagem deve ser apontada com o uso do atributo src
* strong: apesar de deixar em negrito, representa a importância deste texto no meio da frase
* Exemplo de Utilização
<body>
  <header>
    <h1>Página do Burnes</h1>
  </header>
  <nav>
    <a href="index.html" title="Home">Home</a>
  </nav>
  <main>
    <h1>Olá! Bem vindo a minha Pagina!</h1>
  </main>
  <footer>
    <p>Desenvolvido por Burnes</p>
  </footer>
</body>