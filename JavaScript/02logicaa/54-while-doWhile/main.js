// const nome = 'Pedro';
// let i = 0;

// while (i < nome.length) {
//     console.log(nome[i]);
//     i++;
// }

function random(min, max){
    const r = Math.random() * (max - min) + min;
    return Math.floor(r);
}

let rand = 10;

while (rand !== 10){
    rand = random(1, 50)
    console.log(rand)
}
console.log('##################')

do {
    rand = random(1, 50)
    console.log(rand)
} while (rand !== 10);