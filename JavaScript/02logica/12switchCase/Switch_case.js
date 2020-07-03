// quase nunca deve usar
function getDiaSemanaTexto(diasemana) {
    switch (diaSemana) {

    }
}

const data = new Date('1996-04-21 00:00:00');
const diaSemana = data.getDay();
let diaSemanaTexto;

// if (diaSemana === 0) {
//     diaSemanaTexto = 'Domingo';
// } else if (diaSemana === 1) {
//     diaSemanaTexto = 'Segunda';
// } else if (diaSemana === 2) {
//     diaSemanaTexto = 'Terça';
// } else if (diaSemana === 3) {
//     diaSemanaTexto = 'Quarta';
// } else if (diaSemana === 4) {
//     diaSemanaTexto = 'Quinta';
// } else if (diaSemana === 5) {
//     diaSemanaTexto = 'Sexta';
// } else if (diaSemana === 6) {
//     diaSemanaTexto = 'Sábado';
// } else {
//     diaSemanaTexto = 'Data invalida'
// }
// console.log(diaSemana, diaSemanaTexto)
switch (diaSemana) {
    case 0:
        diaSemanaTexto = 'Domingo';
        break
    case 1:
        diaSemanaTexto = 'Segunda';
        break
    case 2:
        diaSemanaTexto = 'Terça';
        break
    case 3:
        diaSemanaTexto = 'Quarta';
        break
    case 4:
        diaSemanaTexto = 'Quinta';
        break
    case 5:
        diaSemanaTexto = 'Sexta';
        break
    case 6:
        diaSemanaTexto = 'Sábado';
        break
    default:
        diaSemanaTexto = 'Avb';
}
console.log(diaSemana, diaSemanaTexto);