// Datas em js
/*
const tresHoras = 60 * 60 * 3 * 1000
const umDia = 60 * 60 * 24 * 1000
const data = new Date(0 + tresHoras + umDia);
console.log(data.toString());
*/
// data atual
/*                    An    M  Di  Ho  Mi  Se  Milessimo de segundos
const data = new Date(2019, 3, 20, 15, 14, 27, 999); // se omitir as coisas, vai ser tudo zero, e o mes começa do 0-11
console.log(data.toString());
*/
/*
const data = new Date('2019-04-20 20:15:59.999');
console.log(data.toString());

console.log('Dia', data.getDate())
console.log('Mês', data.getMonth() + 1) // Mês começa no 0
console.log('Ano', data.getFullYear())
console.log('Hora', data.getHours())
console.log('Min', data.getMinutes())
console.log('Seg', data.getSeconds())
console.log('Ms', data.getDay()) // 0 - Domingo, 6 - Sábado
console.log('Dia semana', data.getDate())
console.log(Date.now())
*/
function zeroAesquerda(num) {
    return num >= 10 ? num : `0${num}`;
}

function formataData(data) {
    const dia = zeroAesquerda(data.getDate());
    const mes = zeroAesquerda(data.getMonth()) + 1;
    const ano = zeroAesquerda(data.getFullYear());
    const hora = zeroAesquerda(data.getHours());
    const min = zeroAesquerda(data.getMinutes());
    const seg = zeroAesquerda(data.getSeconds());
    return `${dia}/${mes}/${ano} ${hora}:${min}:${seg}`
}

const data = new Date(2020, 10, 10, 2, 5, 7);
const dataBrasil = formataData(data)
console.log(dataBrasil);