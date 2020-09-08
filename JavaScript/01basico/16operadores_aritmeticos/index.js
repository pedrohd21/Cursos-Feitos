/**
 * Operadores aritmeticos
 * Adição / concatenação = unir valores
 * - / **
 * % Resto da divisão
 * Precedencia (), **, *, /, %, +, -
 * Incremento = ++ pré ou pós ++
 * Decremento = -- pré ou pós --
*/
let contador = 2;
console.log('Contador1', ++contador) //Add no final e por isso nn adiciona
console.log('Contador1', contador)

let contador1 = 1
console.log('Contador2', ++contador1) //Add no inicio
console.log('Contador2', contador1)

let contador3 = 1
contador3 += 2 // igual python
console.log(contador3)

// NaN - not a number, parseInt(inteiro), parseFloat(deciais) Namber comverte pra qualquer um deles

const num1 = 10;
const num2 = Number(5.10)
console.log(num1 + num2)