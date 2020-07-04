// let a = 'A'; //B
// let b = 'B'; // C
// let c = 'C'; // A

// const letras = [b, c, a];
// [a, b, c] = letras;

// console.log(a, b, c)

// ... rest, ... spread
// const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];
// // const [um, dois, ...resto] = numeros
// // console.log(resto);

// const [um, , dois, , tres, , ...resto] = numeros
// console.log(um, dois, tres, resto)

const numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
const [lista, lista2, lista3] = numeros
console.log(lista[1]);