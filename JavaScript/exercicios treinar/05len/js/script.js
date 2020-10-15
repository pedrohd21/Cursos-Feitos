const arquivo = document.querySelector('#arquivo');

arquivo.addEventListener('submit', function(e){
    e.preventDefault();
    const intQuantidade = e.target.querySelector('#quantidade');
    const quantidade = intQuantidade.value;
    const tamanho = tamanhoLen(quantidade)
    const msg = `${quantidade} <br> tamanho é: ${tamanho}`;
    setResultado(msg);
})

function tamanhoLen(quantidade){
    return quantidade.length
}


function setResultado(texto){
    const resultado = document.querySelector('#resultado');
    resultado.innerHTML = '';
    resultado.innerHTML = texto;
}