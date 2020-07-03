// condição ? 'Valor para verdadeiro': 'Valor para falso'
// como fazer um if else mais so com verdadeiro ou falso

const pontuacaoUsuario = 500;
const nivelUsuario = pontuacaoUsuario >= 1000 ? 'Usuário VIP' : 'Usuario Normal';
//if (pontuacaoUsuario >= 1000) {
//    console.log('Usuário VIP');
//} else {
//    console.log('Usuário Nornal');
//}
//console.log(nivelUsuario);

const corUsuario = null;
const corPadrao = corUsuario || 'Preta';

console.log(nivelUsuario, corPadrao)
