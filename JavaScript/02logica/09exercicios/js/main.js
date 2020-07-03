//Captar evento submit do formulario

const form = document.querySelector('#form'); //pega o form do index html

form.addEventListener('submit', function (e) { //passo 1
    e.preventDefault();  // chama a função setResultado
    const inputPeso = e.target.querySelector('#peso'); // vai me informa o elemento que ta recebendo o evento
    const inputAltura = e.target.querySelector('#altura'); // vai me informa o elemento que ta recebendo o evento
    const peso = Number(inputPeso.value);
    const altura = Number(inputAltura.value);
    console.log(peso, altura)

    if (!peso) {
        setResultado('Peso Invalido', false);
        return;
    } if (!altura) {
        setResultado('Altura invalida', false)
    }
    const imc = getImc(peso, altura);
    const nivelImc = getNivelImc(imc);
    const msg = `Seu Imc é ${imc} (${nivelImc}).`
    setResultado(msg, true);
});

function getNivelImc(imc) {
    const nivel = ['Abaxo do peso', 'Peso Normal', 'Sobrepeso', 'Obesidade grau 1°', 'Obesidade grau 2°', 'Obesidade grau 3°'];

    if (imc >= 39.9) return nivel[5];
    if (imc >= 34.9) return nivel[4];
    if (imc >= 29.9) return nivel[3];
    if (imc >= 24.9) return nivel[2];
    if (imc >= 18.5) return nivel[1];
    if (imc < 18.5) return nivel[0];
}

function getImc(peso, altura) {
    const imc = peso / altura ** 2;
    return imc.toFixed(2);
}

function criaP() { // uma função que cria um paragrafo no html
    const p = document.createElement('p'); // criando um paragrafo
    return p; // retorna o paragrafo
}

function setResultado(msg, isValid) { // passo 2 - vai ser exibido no resultado no index
    const resultado = document.querySelector('#resultado');
    resultado.innerHTML = ''; // zera o resultado


    const p = criaP();

    if (isValid) {
        p.classList.add('paragrafo-resultado');
    } else {
        p.classList.add('bad');
    }

    p.innerHTML = msg;
    resultado.appendChild(p);
}



//parou no 23:44