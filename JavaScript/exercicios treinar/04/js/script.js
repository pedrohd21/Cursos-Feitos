




function meuEscopo() {
    const form = document.querySelector('.form');
    const resultado = document.querySelector('.resultado');

    const nomes = [];

    function recebeEventoForm(evento){
        evento.preventDefault();
        const nome = form.querySelector('.nome');
        nomes.push({
            nome: nome.value
        })

        console.log(nomes);
        resultado.innerHTML += `Nome Completo: ${nome.value} <br>`;
    }
    form.addEventListener('submit', recebeEventoForm);
}

meuEscopo();