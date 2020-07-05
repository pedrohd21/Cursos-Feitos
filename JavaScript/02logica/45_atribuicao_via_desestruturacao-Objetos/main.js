const pessoa = {
    nome: 'Pedro',
    sobrenome: 'Henrique',
    idade: 23,
    endereco:{
        // rua: 'Av. Brasil',
        numero: 320}
    };

// const {endereco: {rua: r = 12345, numero}} = pessoa
// console.log(r, numero);

const {nome, ...resto} = pessoa;
console.log(nome, resto)
