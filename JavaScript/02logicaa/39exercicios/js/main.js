function imc(){
    const form = document.querySelector('.form');
    const resultado = document.querySelector('.resultado');
    
    const array = []
    function recebeResultadoImc(evento){
        evento.preventDefault();
        const peso = form.querySelector('.peso');
        const altura = form.querySelector('.altura');
        array.push({
            peso = peso.value,
            altura = altura.value
        })
        console.log(array)
        resultado.innerHTML += `Imc: ${peso.value + altura.value} <br>`;
    }
    form.addEventListener('submit', recebeResultadoImc);
}
imc();
