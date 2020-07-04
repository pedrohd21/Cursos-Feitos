const frutas = ['Pera', 'Maça', 'Uva'];

const pessoa = { nome: 'Pedro', sobrenome: 'Henrique', idade: 23 }

//console.log(pessoa.nome);
//console.log(pessoa['nome']);


for (let i in pessoa) {
    console.log(i, ':', pessoa[i]);
};

// For in -> Lê os indices ou chaves do objeto
//for (let i in frutas) {
//    console.log(frutas[i]);
//};

//for (let i = 0; i < frutas.length; i++) {
//    console.log(frutas[i]);
//};